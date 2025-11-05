#%%
import re

METHOD_RE = re.compile(
    r"(?:\/\/\/\s*<summary>\s*(?P<summary>.*?)\s*<\/summary>\s*)?"
    r"(?:\[.*?\]\s*)*"
    r"(?:public|private|internal|protected)\s*"
    r"(?P<return>\w[\w<>?]*)\s+"
    r"(?P<name>\w+)\s*"
    r"\((?P<params>[^)]*)\)",
    re.DOTALL
)

class_block = """
public class Composer : MonoBehaviour
    {
        // -----------------------------
        // Public config (Editor-friendly)
        // -----------------------------
        [Header("Defaults")]
        [Tooltip("Default starting key if not provided by Director/Initialize().")]
        public KeyScale defaultStartKey = new KeyScale(NoteName.C, ScaleType.Major);

        /*[Header("Performance")]
        [Range(1, 32)] public int beatsPerBar = 4;
        [Range(1, 16)] public int barsPerBatch = 2;
        */
        // -----------------------------
        // Internal state
        // -----------------------------
        private readonly Dictionary<string, IInstrumentTrack> _tracks = new(StringComparer.OrdinalIgnoreCase);
        
        public IReadOnlyCollection<string> InstrumentNames => _tracks.Keys;

        // -----------------------------
        // Construction / Setup
        // -----------------------------
        public Composer() { /* Unity will call Awake/Start; prefer Initialize() for runtime */ }

        /// <summary>
        /// Preferred runtime initializer (Director may call this).
        /// </summary>
        public void Initialize(KeyScale startKey = null)
        {
            if (startKey == null)
               throw new ArgumentNullException("Composer needs Key to initialize.");
        }

        /// <summary>
        /// Add a new instrument track. The track may define its own key and target key.
        /// </summary>
        public void AddInstrument(IInstrumentTrack track)
        {
            if (track == null) return;

            if (track == null)
                throw new ArgumentNullException(nameof(track), "Cannot add null instrument to Composer.");

            if (string.IsNullOrWhiteSpace(track.Name))
                throw new ArgumentException("Instrument must have a valid name.", nameof(track));

            if (_tracks.ContainsKey(track.Name))
                throw new InvalidOperationException($"An instrument named '{track.Name}' already exists in Composer.");

            _tracks.Add(track.Name, track);
        }

        public void RemoveInstrument(string name)
        {
            if (!_tracks.Remove(name))
                throw new KeyNotFoundException($"No instrument named '{name}' exists in Composer.");
        }

        public IInstrumentTrack GetInstrument(string name)
        {
            if (_tracks.TryGetValue(name, out var track))
                return track;
            throw new KeyNotFoundException($"No instrument named '{name}' exists in Composer.");
        }

        public void ClearInstruments()
        {
            _tracks.Clear();
        }

        /// <summary>
        /// Set a target key for a named instrument. If it supports transitions, it will modulate over its configured number of bars.
        /// </summary>
        public bool SetInstrumentTargetKey(string instrumentName, KeyScale target)
        {
            var track = GetInstrument(instrumentName);

            track.SetTargetKey(target);
            return true;
        }

        // -----------------------------
        // Main API (called by MusicTimelineQueue)
        // -----------------------------
        public List<MusicalEvent> ComposeBars(int numBars, int beatsPerBar, float? tempoOverride = null)
        {
            // Tempo → seconds per beat (SPB)
            float tempo = tempoOverride ?? MusicGenSettings.Instance?.defaultTempo ?? 120f;
            float spb = 60f / Mathf.Max(1f, tempo);

            var batch = new List<MusicalEvent>(capacity: 128);

            for (int i = 0; i < numBars; i++)
            {
                // 2) Ask each track to compose one bar (relative to 0)
                foreach (var t in _tracks.Values)
                {
                    var evs = t.ComposeBar(secondsPerBeat: spb, beatsPerBar: beatsPerBar);

                    // Safety: normalize null → empty; ensure channel is set
                    if (evs != null && evs.Count > 0)
                    {
                        foreach (var e in evs) e.Channel = t.Channel;
                        batch.AddRange(evs);
                    }
                }
            }

            // Sort for stability (StartTimeSec is relative; TimelineQueue offsets to absolute)
            return batch
                .OrderBy(e => e.StartTimeSec)
                .ThenBy(e => e.Channel)
                .ToList();
        }
    }

    // ========================================================================
    // Track Abstractions (kept here so this single file is drop-in ready)
    // ========================================================================

    public interface IInstrumentTrack
    {
        string Name { get; }
        /// <summary>MIDI channel (0-15) to route this instrument's notes.</summary>
        int Channel { get; }

        /// <summary>Current working key for this instrument.</summary>
        KeyScale CurrentKey { get; }
        /// <summary>Does this instrument support key transitions over multiple bars?</summary>
        bool SupportsTransition { get; }

        /// <summary>Set the current working key immediately.</summary>
        void SetCurrentKey(KeyScale key);

        /// <summary>Request a target key; if supported, the track should gradually move over TransitionBars (or override).</summary>
        void SetTargetKey(KeyScale key);

        /// <summary>Compose exactly one bar of material, relative to beat 0.</summary>
        List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar);
    }

    /// <summary>
    /// Convenience base class with common key-transition plumbing.
    /// Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this.
    /// </summary>
    public abstract class BaseInstrumentTrack : IInstrumentTrack
    {
        public string Name { get; protected set; }
        public int Channel { get; protected set; }

        public KeyScale CurrentKey { get; protected set; }
        public bool SupportsTransition { get; protected set; } = true;

        // Transition state
        protected KeyScale TargetKey;
        protected int TransitionBars = 2; // default (configurable per track)
        protected int BarsIntoTransition = 0;
        protected bool IsTransitioning => TargetKey != null && !KeyEquals(TargetKey, CurrentKey);

        protected BaseInstrumentTrack(string name, int channel, KeyScale startKey)
        {
            Name = name;
            Channel = Mathf.Clamp(channel, 0, 15);
            CurrentKey = startKey;
        }

        public virtual void SetCurrentKey(KeyScale key)
        {
            CurrentKey = key;
        }

        public virtual void SetTargetKey(KeyScale key)
        {
            TargetKey = key;
        }

        public abstract List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar);

        protected static bool KeyEquals(KeyScale a, KeyScale b)
        {
            if (a == null || b == null) return false;
            return a.Root == b.Root && a.ScaleType == b.ScaleType;
        }
    }
}
"""
# 🚫 Noise filter
CS_KEYWORDS = {
    "var","return","yield","else","if","for","foreach","while","switch","case",
    "new","private","public","protected","internal","static","readonly","partial",
    "true","false","null","class","interface","struct","enum","void",
    "get","set","value","in","out","ref","using","params","override"
}
UNITY_EDITOR_WORDS = {
    "GUILayout","EditorGUILayout","GUILayoutOption","Editor","target","GUILayoutOption[]"
}
BUILTINS = {
    "int","float","double","string","bool","char","object","decimal","byte",
    "long","short","uint","ulong","ushort","float?","int?","void"
}
UNITY_ATTRIBUTES = {"Tooltip","Header","Range","Space","SerializeField", "HideInInspector"}

COLLECTION_TYPES = {"List", "Dictionary", "HashSet", "Queue", "Stack", "IReadOnlyCollection"}

IGNORE_TYPES = CS_KEYWORDS | UNITY_EDITOR_WORDS | \
                BUILTINS | UNITY_ATTRIBUTES | COLLECTION_TYPES

def _filter_type(t: str):
    """
    Extract meaningful type names (handles generics like List<Note>)
    """
    # Remove symbols
    t = re.sub(r"[^\w<>]", "", t)

    # Extract classes inside generics: List<Chord> → Chord
    parts = re.findall(r"[A-Z]\w+", t)

    # Add raw if it looks like a type
    if re.match(r"[A-Z]\w+", t):
        parts.append(t)

    return [p for p in parts if p not in IGNORE_TYPES]

PARAM_RE = re.compile(r"(?P<type>[\w<>?]+)\s+(?P<name>\w+)")

FIELD_RE = re.compile(
    r"(?:public|private|protected|internal|static)+\s+(readonly\s+)?"
    r"(?P<type>\w+(<\w+(,\s+\w+)?>)?)\s+"
    r"(?P<name>\w+)"
    r"(?:\s*=\s*[^;]+)?;",
    re.MULTILINE
)

class_block_clean = re.sub(
    r"=\s*new\s+[A-Za-z_]\w*\s*\([^;]*?\);",
    "= new(/*...*/);",
    class_block
)
fields=[]
class_name="Composer"
# ✅ Fields
fields=[]
for f in FIELD_RE.finditer(class_block_clean):
    f_type = f.group("type")
    print(f_type)
    fields.append({"name": f.group("name"), "type": f_type.strip(">")})
    #for t in _filter_type(f_type):


for f in fields:
    print(f)