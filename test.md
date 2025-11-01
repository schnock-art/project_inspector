# ProjectDoc Output

Scanned folder: `C:\Users\jange\MusicGeneration\Assets\_Project`

📂 **Project Tree: _Project**

```
_Project
├── Audio
│   ├── Biomes
│   ├── MusicGen
│   │   ├── Composition
│   │   │   ├── Composer.cs
│   │   │   ├── Composer.cs.meta
│   │   │   ├── HarmonyTrack.cs
│   │   │   ├── HarmonyTrack.cs.meta
│   │   │   ├── MelodyTrack.cs
│   │   │   ├── MelodyTrack.cs.meta
│   │   │   ├── MusicDirector.cs
│   │   │   └── MusicDirector.cs.meta
│   │   ├── Core
│   │   │   ├── Chords
│   │   │   │   ├── Chord.cs
│   │   │   │   ├── Chord.cs.meta
│   │   │   │   ├── ChordType.cs
│   │   │   │   └── ChordType.cs.meta
│   │   │   ├── Events
│   │   │   │   ├── MusicalEvent.cs
│   │   │   │   └── MusicalEvent.cs.meta
│   │   │   ├── Melody
│   │   │   │   ├── MelodyPhrase.cs
│   │   │   │   ├── MelodyPhrase.cs.meta
│   │   │   │   ├── MelodyPhraseExtensions.Basic.cs
│   │   │   │   └── MelodyPhraseExtensions.Basic.cs.meta
│   │   │   ├── Notes
│   │   │   │   ├── Note.cs
│   │   │   │   ├── Note.cs.meta
│   │   │   │   ├── NoteMap.cs
│   │   │   │   ├── NoteMap.cs.meta
│   │   │   │   ├── NoteName.cs
│   │   │   │   ├── NoteName.cs.meta
│   │   │   │   ├── NotePitch.cs
│   │   │   │   ├── NotePitch.cs.meta
│   │   │   │   ├── NoteUtilities.cs
│   │   │   │   └── NoteUtilities.cs.meta
│   │   │   ├── Rythm
│   │   │   │   ├── RhythmPhrase.cs
│   │   │   │   ├── RhythmPhrase.cs.meta
│   │   │   │   ├── RhythmPhraseElement.cs
│   │   │   │   ├── RhythmPhraseElement.cs.meta
│   │   │   │   ├── RhythmPhraseExtensions.cs
│   │   │   │   ├── RhythmPhraseExtensions.cs.meta
│   │   │   │   ├── RhythmPhraseGenerator.cs
│   │   │   │   └── RhythmPhraseGenerator.cs.meta
│   │   │   ├── Scales
│   │   │   │   ├── KeyScale.cs
│   │   │   │   ├── KeyScale.cs.meta
│   │   │   │   ├── ScaleType.cs
│   │   │   │   ├── ScaleType.cs.meta
│   │   │   │   ├── ScaleUtils.cs
│   │   │   │   └── ScaleUtils.cs.meta
│   │   │   ├── Chords.meta
│   │   │   ├── Events.meta
│   │   │   ├── Melody.meta
│   │   │   ├── Notes.meta
│   │   │   ├── Rythm.meta
│   │   │   └── Scales.meta
│   │   ├── Generators
│   │   │   ├── Chord
│   │   │   │   ├── ChordProgressionGenerator.cs
│   │   │   │   ├── ChordProgressionGenerator.cs.meta
│   │   │   │   ├── ChordProgressionLibrary.cs
│   │   │   │   └── ChordProgressionLibrary.cs.meta
│   │   │   ├── Note
│   │   │   │   ├── INoteGenerator.cs
│   │   │   │   ├── INoteGenerator.cs.meta
│   │   │   │   ├── MarkovMelodyGenerator.cs
│   │   │   │   ├── MarkovMelodyGenerator.cs.meta
│   │   │   │   ├── RuleMelodyGenerator.cs
│   │   │   │   └── RuleMelodyGenerator.cs.meta
│   │   │   ├── Pattern
│   │   │   │   ├── PatternEvolution.cs
│   │   │   │   └── PatternEvolution.cs.meta
│   │   │   ├── Chord.meta
│   │   │   ├── Note.meta
│   │   │   └── Pattern.meta
│   │   ├── Harmony
│   │   │   ├── HarmonySegment.cs
│   │   │   ├── HarmonySegment.cs.meta
│   │   │   ├── HarmonyTimelineManager.cs
│   │   │   └── HarmonyTimelineManager.cs.meta
│   │   ├── Playback
│   │   │   ├── Editor
│   │   │   │   ├── MusicTimelineQueueEditor.cs
│   │   │   │   └── MusicTimelineQueueEditor.cs.meta
│   │   │   ├── Editor.meta
│   │   │   ├── MusicTimelineQueue.cs
│   │   │   └── MusicTimelineQueue.cs.meta
│   │   ├── Resources
│   │   │   ├── Forest.asset
│   │   │   ├── Forest.asset.meta
│   │   │   ├── MusicGenSettings.asset
│   │   │   └── MusicGenSettings.asset.meta
│   │   ├── Scenes
│   │   │   ├── TestScene.unity
│   │   │   └── TestScene.unity.meta
│   │   ├── Settings
│   │   │   ├── BiomeMusicSettings.cs
│   │   │   ├── BiomeMusicSettings.cs.meta
│   │   │   ├── MusicGenSettings.cs
│   │   │   ├── MusicGenSettings.cs.meta
│   │   │   ├── MusicGenSettingsLoader.cs
│   │   │   └── MusicGenSettingsLoader.cs.meta
│   │   ├── Test
│   │   │   ├── TestMusicSetup.cs
│   │   │   └── TestMusicSetup.cs.meta
│   │   ├── Composition.meta
│   │   ├── Core.meta
│   │   ├── Generators.meta
│   │   ├── Harmony.meta
│   │   ├── Playback.meta
│   │   ├── Resources.meta
│   │   ├── Scenes.meta
│   │   ├── Settings.meta
│   │   └── Test.meta
│   ├── Biomes.meta
│   └── MusicGen.meta
└── Audio.meta
```

### Composer: 
> /// Orchestrates multiple instrument tracks, each with its own key and optional key transition.
    /// Returns bar-sized, time-relative MusicalEvents to be scheduled by MusicTimelineQueue.
    ///
    /// Responsibilities:
    /// - Track registry (add/remove) of instruments
    /// - Provide per-bar composition for all instruments
    /// - Assign MIDI channels (Program/Patch is NOT handled here)
    ///
    /// Non-responsibilities:
    /// - PatchChange / Program selection (handled by Director/Timeline)
    /// - Absolute scheduling (handled by MusicTimelineQueue)
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `None Composer()`
- `void Initialize(KeyScale startKey)`
  - */// Preferred runtime initializer (Director may call this).
        ///*
- `new ArgumentNullException(Composer needs, Key to)`
  - *<summary> Preferred runtime initializer (Director may call this). </summary>*
- `void AddInstrument(IInstrumentTrack track)`
  - */// Add a new instrument track. The track may define its own key and target key.
        ///*
- `new ArgumentNullException()`
  - *<summary> Preferred runtime initializer (Director may call this). </summary>*
- `new ArgumentException(Instrument must, have a, valid name)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `new InvalidOperationException(An instrument, already exists, in Composer)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `void RemoveInstrument(string name)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `new KeyNotFoundException(No instrument, exists in)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `IInstrumentTrack GetInstrument(string name)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `new KeyNotFoundException(No instrument, exists in)`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `void ClearInstruments()`
  - *<summary> Add a new instrument track. The track may define its own key and target key. </summary>*
- `bool SetInstrumentTargetKey(string instrumentName, KeyScale target)`
  - */// Set a target key for a named instrument. If it supports transitions, it will modulate over its configured number of bars.
        ///*
- `List<MusicalEvent> ComposeBars(int numBars, int beatsPerBar, float? tempoOverride)`
  - *<summary> Set a target key for a named instrument. If it supports transitions, it will modulate over its configured number of bars. </summary>*

### IInstrumentTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Methods:**
- `void SetCurrentKey(KeyScale key)`
  - *MIDI channel (0-15) to route this instrument's notes.</summary>
        int Channel { get; }

        /// <summary>Current working key for this instrument.</summary>
        KeyScale CurrentKey { get; }
        /// <summary>Does this instrument support key transitions over multiple bars?</summary>
        bool SupportsTransition { get; }

        /// <summary>Set the current working key immediately.*
- `void SetTargetKey(KeyScale key)`
  - *Request a target key; if supported, the track should gradually move over TransitionBars (or override).*
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
  - *Compose exactly one bar of material, relative to beat 0.*

### with: 
> <summary> Convenience base

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Methods:**
- `Concrete tracks()`
  - *Concrete*
- `protected BaseInstrumentTrack(string name, int channel, KeyScale startKey)`
  - *Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>*
- `void SetCurrentKey(KeyScale key)`
  - *Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>*
- `void SetTargetKey(KeyScale key)`
  - *Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>*
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
  - *Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>*
- `bool KeyEquals(KeyScale a, KeyScale b)`
  - *Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>*

### BaseInstrumentTrack: 
> <summary> Convenience base class with common key-transition plumbing. Concrete tracks (HarmonyTrack, MelodyTrack, PercussionTrack) can inherit from this. </summary>

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Inherits:** IInstrumentTrack

**Methods:**
- `None BaseInstrumentTrack(string name, int channel, KeyScale startKey)`
- `void SetCurrentKey(KeyScale key)`
- `void SetTargetKey(KeyScale key)`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `bool KeyEquals(KeyScale a, KeyScale b)`

### HarmonyTrack: 
> /// Harmony instrument track: outputs chords or arpeggios based on a chord progression timeline.
    /// Each HarmonyTrack has its own key and can modulate toward a target key over time.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\HarmonyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
- `None HarmonyTrack(string name, int channel, KeyScale startKey, ChordProgressionLibrary library, bool useArpeggios, int velocity)`
- `void SetCurrentKey(KeyScale key)`
- `void SetTargetKey(KeyScale key)`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `new MusicalEvent()`
- `new MusicalEvent()`

### MelodyTrack: 
> /// Melody instrument using PatternEvolution (melody + rhythm mutation over time).
    /// Each MelodyTrack has its own generator and its own evolving musical memory.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\MelodyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
- `None MelodyTrack(string name, int channel, KeyScale startKey, INoteGenerator noteGen, RhythmPhraseGenerator rhythmGen, int hitsPerBar, int velocity, float mutationProb, float mutationIntensity)`
- `new PatternEvolution()`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `new MusicalEvent()`

### MusicDirector: 
> /// High-level orchestration: builds instruments, assigns channels & programs,
    /// sets tempo, applies (global or per-instrument) key changes, and starts playback.
    ///
    /// - Composer: composition + channel routing (no PatchChange)
    /// - Timeline: playback & PatchChange scheduling at bar boundaries
    /// - Director: decides which instruments, sounds, tempo, and key transitions
    ///
    /// Default setup:
    ///   Harmony: ch 0, Program 0 (Piano), C Major
    ///   Melody : ch 1, Program 40 (Violin), C Major
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\MusicDirector.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `starting key(each instrument, can override, via Director)`
- `at StartMusic()`
- `void Awake()`
- `void StartMusic()`
  - */// One-call setup to get music going:
        /// - Initialize composer (start key)
        /// - Build HarmonyTrack + MelodyTrack
        /// - Assign programs to channels (scheduled at next bar)
        /// - Apply optional tempo
        /// - Start timeline playback
        ///*
- `new ArgumentNullException(MusicTimelineQueuw is, not set, in the)`
  - *<summary> One-call setup to get music going: - Initialize composer (start key) - Build HarmonyTrack + MelodyTrack - Assign programs to channels (scheduled at next bar) - Apply optional tempo - Start timeline playback </summary>*
- `new ArgumentNullException(Composer is, not set, in the)`
  - *<summary> One-call setup to get music going: - Initialize composer (start key) - Build HarmonyTrack + MelodyTrack - Assign programs to channels (scheduled at next bar) - Apply optional tempo - Start timeline playback </summary>*
- `void StopMusic()`
  - *Stop playback and clear queued data.*
- `void SetTempo(float bpm)`
  - *Convenience: set tempo at runtime.*
- `void ApplyKeyChangeToInstrument(string instrumentName, KeyScale targetKey, int transitionBars)`
  - */// Apply a key change to a single instrument (by name). Transition occurs over 'transitionBars' bars if supported by the track.
        ///*
- `void ApplyGlobalKeyChange(KeyScale targetKey, int transitionBars)`
  - */// Apply a key change to all instruments added by this Director.
        ///*

### HarmonySegment: 
> Represents a harmonic region in the timeline (key + chords + duration).

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonySegment.cs`

**Methods:**
- `None HarmonySegment(KeyScale key, List<Chord> chords, int bars, bool isTransition)`

### HarmonyTimelineManager: 
> /// Manages harmonic segments, keeps 1–2 bars ahead and handles deterministic transitions.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonyTimelineManager.cs`

**Methods:**
- `None HarmonyTimelineManager(ChordProgressionLibrary library, KeyScale start)`
- `new ChordProgressionLibrary()`
- `new KeyScale()`
- `void RequestTransition(KeyScale newTarget)`
  - *Request a new target key/mode; will append a transition segment automatically.*
- `new HarmonySegment()`
- `new HarmonySegment()`
- `List<Chord> GetNextChords(int maxBars)`
  - *Gets next few chords (default 2 bars ahead).*
- `new HarmonySegment()`

### MusicTimelineQueueData: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Methods:**
- `public Scheduled(MusicalEvent e, bool isNoteOff)`
- `float GetNextBarStart(int beatsPerBar)`
- `void AddBar(IEnumerable<MusicalEvent> newEvents, int beatsPerBar)`
- `new Scheduled()`
- `void RemovePlayed(float elapsedSec)`
- `float ComputeBeatsAhead()`
- `void UpdateTransportGrid(float currentBeat, int beatsPerBar)`

### Scheduled: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Methods:**
- `None Scheduled(MusicalEvent e, bool isNoteOff)`

### MusicTimelineQueue: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `public Scheduled(MusicalEvent e, bool isNoteOff)`
- `float GetNextBarStart(int beatsPerBar)`
- `void AddBar(IEnumerable<MusicalEvent> newEvents, int beatsPerBar)`
- `new Scheduled()`
- `void RemovePlayed(float elapsedSec)`
- `float ComputeBeatsAhead()`
- `void UpdateTransportGrid(float currentBeat, int beatsPerBar)`

### BiomeMusicSettings: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Inherits:** ScriptableObject

**Methods:**
- `EmotionMapping GetEmotionMapping(string emotion)`
- `ScaleProfile GetRandomScale()`

### InstrumentPreset: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**

### ScaleProfile: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**

### EmotionMapping: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**

### MelodyPaceMapping: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**

### MusicGenSettings: 
> /// Global settings for the procedural music engine.
    /// Defines tuning, tempo defaults, and rhythm feel parameters.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettings.cs`

**Inherits:** ScriptableObject

**Methods:**
- `for A4()`
- `for A4(usually 69)`
- `Default tempo()`
- `void OnEnable()`
- `void OnValidate()`
- `void SubscribeToTempoChange(Action<float> listener)`
- `void Apply()`
  - */// Call this at runtime to apply settings programmatically (if loaded manually).
        ///*
- `void SetTempo(float newTempo)`
  - *<summary> Call this at runtime to apply settings programmatically (if loaded manually). </summary>*

### MusicGenSettingsLoader: 
> /// Automatically loads and applies MusicGenSettings from Resources folder.
    /// Ensures global tuning and defaults are initialized at startup.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettingsLoader.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void Awake()`
- `Settings loaded()`
- `void SetTempo(float newTempo)`

### TestMusicSetup: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Test\TestMusicSetup.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void Awake()`
- `void Play()`
- `void Update()`

### Chord: 
> /// Represents a musical chord built from a root note and chord type.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Chords\Chord.cs`

**Methods:**
- `List<Note> GetArpeggio(ArpeggioStyle style, int octaves)`
  - *Scale degree (1..7) if diatonic; 0 if undefined. </summary>
        public int ScaleDegree { get; private set; }

        /// <summary> Root MIDI note (int). </summary>
        public int RootMidi => Root?.MidiNote ?? 60;

        private static readonly Dictionary<ChordType, int[]> ChordIntervals = new()
        {
            
            { ChordType.Major, new [] { 0, 4, 7 } },
            { ChordType.Minor, new [] { 0, 3, 7 } },
            { ChordType.Diminished, new [] { 0, 3, 6 } },
            { ChordType.Augmented, new [] { 0, 4, 8 } },

            
            { ChordType.Major7, new [] { 0, 4, 7, 11 } },
            { ChordType.Minor7, new [] { 0, 3, 7, 10 } },
            { ChordType.Dominant7, new [] { 0, 4, 7, 10 } },
            { ChordType.HalfDiminished7, new [] { 0, 3, 6, 10 } },
            { ChordType.Diminished7, new [] { 0, 3, 6, 9 } },

            
            { ChordType.Major6, new [] { 0, 4, 7, 9 } },
            { ChordType.Minor6, new [] { 0, 3, 7, 9 } },
            { ChordType.Add9, new [] { 0, 4, 7, 14 } },
            { ChordType.MinorAdd9, new [] { 0, 3, 7, 14 } },

            
            { ChordType.Sus2, new [] { 0, 2, 7 } },
            { ChordType.Sus4, new [] { 0, 5, 7 } }
        };

        public Chord(Note root, ChordType type, int scaleDegree = 0)
        {
            Root = root;
            Type = type;
            ScaleDegree = scaleDegree;
            BuildNotes();
        }

        private void BuildNotes()
        {
            Notes.Clear();
            if (!ChordIntervals.TryGetValue(Type, out var intervals))
                return;

            foreach (var i in intervals)
            {
                int midi = Root.MidiNote + i;
                if (midi > 127) midi -= 12; 
                Notes.Add(new Note(midi));
            }
        }

        public int[] GetPitches()
        {
            var pitches = new List<int>();
            foreach (var n in Notes)
                pitches.Add(n.MidiNote);
            return pitches.ToArray();
        }

        
        
        
        public Chord GetInversion(int inversion)
        {
            if (Notes.Count == 0 || inversion <= 0) return this;
            var newNotes = new List<Note>(Notes);
            for (int i = 0; i < inversion && newNotes.Count > 0; i++)
            {
                var lowest = newNotes[0];
                newNotes.RemoveAt(0);
                newNotes.Add(new Note(lowest.MidiNote + 12)); 
            }

            var inv = new(/*...*/);
            inv.Notes = newNotes;
            return inv;
        }

        public Chord AddExtension(int semitone)
        {
            var extNote = new(/*...*/);
            var newChord = new(/*...*/);
            newChord.Notes = new List<Note>(Notes) { extNote };
            return newChord;
        }

        public enum ArpeggioStyle { Up, Down, UpDown, Random }

        /// <summary>
        /// Returns a sequence of notes forming an arpeggio pattern from this chord.
        ///*
- `new Note()`
- `string ToString()`
  - *<summary> Returns a sequence of notes forming an arpeggio pattern from this chord. </summary>*

### MusicalEvent: 
> /// Represents a scheduled musical event (note or chord) with timing in beats and seconds.
    /// Used by PatternBuilder, playback systems, and MIDI export.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Events\MusicalEvent.cs`

**Methods:**
- `None MusicalEvent(float startBeat, float durationBeats, int velocity, int channel, int? program)`
- `string ToString()`

### MelodyPhrase: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhrase.cs`

**Methods:**
- `None MelodyPhrase()`
- `None MelodyPhrase(IEnumerable<Note> notes)`
- `MelodyPhrase Clone()`
- `new Note()`
- `string ToString()`

### MelodyPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhraseExtensions.Basic.cs`

**Methods:**
- `MelodyPhrase Transpose(this MelodyPhrase, int semitones)`
  - *Clone & return mutated*
- `MelodyPhrase SwapAdjacent(this MelodyPhrase, float probability)`
  - *Clone & return mutated*
- `MelodyPhrase InvertAround(this MelodyPhrase, Note axis)`
  - *Clone & return mutated*
- `MelodyPhrase ConstrainToScale(this MelodyPhrase, KeyScale scale, int min, int max)`
  - *Snap all notes to nearest valid notes in scale*
- `specific index(clamped safe)`
  - *<summary> Insert a note at a specific*
- `void InsertNote(this MelodyPhrase, int index, Note note)`
  - *<summary> Insert a note at a specific index (clamped safe). </summary>*
- `new InvalidOperationException(MelodyPhrase is, null or)`
  - *<summary> Insert a note at a specific index (clamped safe). </summary>*
- `new Note()`
  - *Clone & return mutated*
- `void AddNote(this MelodyPhrase, Note note)`
  - *<summary> Append a note to the end. </summary>*
- `new ArgumentNullException()`
  - *<summary> Append a note to the end. </summary>*
- `new Note()`
  - *Clone & return mutated*
- `given index()`
  - *<summary> Insert a note at a specific*
- `void RemoveNoteAt(this MelodyPhrase, int index)`
  - *<summary> Remove a note at the given index (safe). </summary>*
- `random note(returns false, if only, one note)`
  - *Snap all*
- `bool RemoveRandomNote(this MelodyPhrase, Random rng)`
  - *<summary> Remove a random note (returns false if only one note left). </summary>*
- `void RemoveNotes(this MelodyPhrase, int count, Random rng)`
  - *<summary> Remove a random note (returns false if only one note left). </summary>*
- `new ArgumentNullException()`
  - *<summary> Append a note to the end. </summary>*
- `given index(diatonic step)`
  - *<summary> Insert a note at a specific*
- `void InsertNeighborNote(this MelodyPhrase, int index, KeyScale scale, int minStep, int maxStep, Random rng)`
  - *<summary> Insert a random note near a given index (diatonic step up/down) </summary>*
- `void AddMultipleNotes(this MelodyPhrase, int count, KeyScale scale, Random rng)`
  - *<summary> Insert a random note near a given index (diatonic step up/down) </summary>*
- `new ArgumentNullException()`
  - *<summary> Append a note to the end. </summary>*
- `void InsertMusicalNote(this MelodyPhrase, KeyScale scale, Random rng)`
  - *<summary> Insert a random note near a given index (diatonic step up/down) </summary>*
- `else if(< 0)`
  - *Clone & return mutated*

### Note: 
> /// Represents a single musical note (with MIDI number, octave, and name).
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\Note.cs`

**Methods:**
- `None Note(int midiNote)`
- `None Note(NoteName noteName, int octave)`
- `None Note(NotePitch pitch)`
- `string ToString()`

### NoteMap: 
> /// Provides fast lookups between MIDI numbers and Note objects.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteMap.cs`

**Methods:**
- `None NoteMap()`
- `Note GetNote(int midiNote)`

### for: 
> <summary> Utility

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteUtilities.cs`

**Methods:**
- `for A4(usually 69)`
  - *<summary> Current reference frequency for*
- `float MidiToFrequency(int midiNote)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `int FrequencyToMidi(float frequency)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `Note Transpose(Note note, int semitones)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `new Note()`
  - *Provides frequency conversion, transposition, and interval helpers. </summary>*
- `int Interval(Note a, Note b)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `string GetNoteNameFromMidi(int midiNote)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `List<string> RangeNames(int startMidi, int endMidi)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*

### NoteUtilities: 
> <summary> Utility class for note calculations and transformations. Provides frequency conversion, transposition, and interval helpers. </summary>

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteUtilities.cs`

**Methods:**
- `for A4(usually 69)`
  - *<summary> Current reference frequency for*
- `float MidiToFrequency(int midiNote)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `int FrequencyToMidi(float frequency)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `Note Transpose(Note note, int semitones)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `new Note()`
- `int Interval(Note a, Note b)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `string GetNoteNameFromMidi(int midiNote)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*
- `List<string> RangeNames(int startMidi, int endMidi)`
  - *<summary> Current reference MIDI note for A4 (usually 69). </summary>*

### RhythmPhrase: 
> /// A rhythm phrase: a sequence of durations (hits) that fill one or more bars.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhrase.cs`

**Methods:**
- `string ToString()`
- `RhythmPhrase Clone()`
  - */// Creates a deep copy of this rhythm phrase and all its elements.
        ///*
- `new RhythmPhraseElement()`
- `IEnumerable<RhythmPhraseElement> LongestElements()`
  - *<summary> Creates a deep copy of this rhythm phrase and all its elements. </summary>*
- `IEnumerable<RhythmPhraseElement> ShortestElements()`
  - *<summary> Creates a deep copy of this rhythm phrase and all its elements. </summary>*

### RhythmPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseExtensions.cs`

**Methods:**
- `void NormalizeToBeats(this RhythmPhrase, float targetBeats)`
  - *<summary> Scales all durations so the phrase fills exactly targetBeats. </summary>*

### RhythmPhraseGenerator: 
> /// Generates musically coherent rhythm phrases that fill a bar exactly,
    /// using discrete note values and adaptive deterministic/stochastic adjustment.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseGenerator.cs`

**Methods:**
- `RhythmPhrase GenerateSmart(int beatsPerBar, int numBars, int numHits, FillStrategy strategy, int seed, bool randomizeOrder)`
  - */// Generates a rhythm that fills the bar exactly using discrete durations.
        ///*
- `new ArgumentException(numHits must, > 0)`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `else ApplyStochasticAdjustment()`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `new RhythmPhraseElement()`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `RhythmPhrase GenerateSubdividedVariation(RhythmPhrase basePhrase, float intensity, int seed)`
  - */// Creates a simple variation by subdividing one or more hits into smaller values.
        /// Keeps total bar duration constant.
        ///*
- `new RhythmPhraseElement()`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `List<float> InitializeDurations(int numHits, float target)`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `void ApplyDeterministicCorrection(List<float> durations, float diff)`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `void ApplyStochasticAdjustment(List<float> durations, float diff)`
  - *<summary> Generates a rhythm that fills the bar exactly using discrete durations. </summary>*
- `float SnapToClosestMusicalValue(float val)`
  - *<summary> Creates a simple variation by subdividing one or more hits into smaller values. Keeps total bar duration constant. </summary>*
- `float TryHalve(float dur)`
  - *<summary> Creates a simple variation by subdividing one or more hits into smaller values. Keeps total bar duration constant. </summary>*
- `float TryDouble(float dur)`
  - *<summary> Creates a simple variation by subdividing one or more hits into smaller values. Keeps total bar duration constant. </summary>*

### KeyScale: 
> /// Represents a musical scale defined by a root note and scale type.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\KeyScale.cs`

**Methods:**
- `None KeyScale(NoteName root, ScaleType scaleType)`
- `void BuildNotes()`
- `new Note()`
- `List<Note> GetNotes()`
- `Note GetTonic()`
  - *Return the tonic note of this key (octave anchored around middle C).*
- `new Note()`
- `Note GetNoteByDegreeOffset(Note from, int diatonicSteps, int midiMin, int midiMax)`
  - */// Move a diatonic number of steps (can be negative) from a given note,
        /// staying within the scale, across a safe MIDI range.
        ///*
- `new Note()`
- `List<int> BuildDiatonicLadder(int midiMin, int midiMax)`
  - *<summary> Move a diatonic number of steps (can be negative) from a given note, staying within the scale, across a safe MIDI range. </summary>*
- `List<Chord> GetDiatonicChords(bool useSevenths)`
  - */// Returns the 7 diatonic triads (I..vii°) for the current scale.
        ///*
- `else if()`
- `else if()`
- `else if()`
- `new Chord()`
  - *<summary> Returns the 7 diatonic triads (I..vii°) for the current scale. </summary>*
- `Chord GetChord(int degree, bool useSevenths)`
  - *<summary> Returns the 7 diatonic triads (I..vii°) for the current scale. </summary>*
- `new Chord(new Note)`
  - *<summary> Returns the 7 diatonic triads (I..vii°) for the current scale. </summary>*
- `string ToString()`
  - *<summary> Returns the 7 diatonic triads (I..vii°) for the current scale. </summary>*

### ScaleIntervals: 
> <summary> Defines scale interval sets for common Western and exotic modes. Each value is a sequence of semitone offsets from the root. </summary>

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleType.cs`

**Methods:**

### sets: 
> <summary> Utilities for working with scales, pitch-

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleUtils.cs`

**Methods:**
- `pitch classes()`
  - *<summary>Return pitch*
- `HashSet<int> PitchClasses(KeyScale ks)`
  - *<summary>Return pitch classes (0..11) in a KeyScale.</summary>*
- `HashSet<int> PitchClassIntersection(KeyScale a, KeyScale b)`
  - *<summary>Pitch-class intersection between two KeyScales.</summary>*
- `MIDI range()`
- `List<int> NotesInRange(KeyScale ks, int midiMin, int midiMax)`
  - *<summary> Expand a KeyScale across a MIDI range (inclusive), returning MIDI note numbers whose pitch-classes are in the scale. </summary>*
- `dest MIDI(same octave, if possible, else nearest, down in)`
  - *<summary> Expand a KeyScale across a*
- `int NearestCommonTone(int sourceMidi, KeyScale src, KeyScale dst, int midiMin, int midiMax)`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `return NearestScaleNote()`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `int NearestScaleNote(int sourceMidi, KeyScale ks, int midiMin, int midiMax)`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `bool ContainsPitchClass(this KeyScale, int pitchClass)`
  - *<summary>Nearest note of a target scale to a given MIDI note.</summary>*

### ScaleUtils: 
> <summary> Utilities for working with scales, pitch-class sets, ranges, and modulations. </summary>

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleUtils.cs`

**Methods:**
- `pitch classes()`
  - *<summary>Return pitch*
- `HashSet<int> PitchClasses(KeyScale ks)`
  - *<summary>Return pitch classes (0..11) in a KeyScale.</summary>*
- `HashSet<int> PitchClassIntersection(KeyScale a, KeyScale b)`
  - *<summary>Pitch-class intersection between two KeyScales.</summary>*
- `MIDI range()`
  - *<summary> Expand a KeyScale across a MIDI*
- `List<int> NotesInRange(KeyScale ks, int midiMin, int midiMax)`
  - *<summary> Expand a KeyScale across a MIDI range (inclusive), returning MIDI note numbers whose pitch-classes are in the scale. </summary>*
- `dest MIDI(same octave, if possible, else nearest, down in)`
  - *<summary> Expand a KeyScale across a*
- `int NearestCommonTone(int sourceMidi, KeyScale src, KeyScale dst, int midiMin, int midiMax)`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `return NearestScaleNote()`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `int NearestScaleNote(int sourceMidi, KeyScale ks, int midiMin, int midiMax)`
  - *<summary> Find a common-tone pivot in the destination scale close to a source MIDI note. Returns dest MIDI (same octave if possible; else nearest up/down in range). </summary>*
- `bool ContainsPitchClass(this KeyScale, int pitchClass)`
  - *<summary>Nearest note of a target scale to a given MIDI note.</summary>*

### intersection: 
> <summary>Pitch-

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleUtils.cs`

**Methods:**
- `HashSet<int> PitchClassIntersection(KeyScale a, KeyScale b)`

### ChordProgressionGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionGenerator.cs`

**Methods:**
- `target key(phase generation)`
- `multiple Generate()`
- `List<Chord> Generate(KeyScale startKey, int numChords, int seed, KeyScale targetKey, float modulationBias)`
- `new KeyScale()`
- `void ResetState()`
  - */// Reset stateful memory (useful when restarting piece or switching biome instantly).
        ///*
- `List<Chord> GenerateGradualModulation(KeyScale currentKey, KeyScale targetKey, int numChords, float modulationBias)`
- `List<Chord> GenerateForceArrival(KeyScale fromKey, KeyScale toKey, int numChords, float modulationBias)`
- `Chord FindPivotChord(KeyScale a, KeyScale b)`
  - *<summary> Reset stateful memory (useful when restarting piece or switching biome instantly). </summary>*
- `Chord PickNextChord(Chord current, List<Chord> pool, KeyScale currentKey, KeyScale targetKey, float modulationBias)`
  - *<summary> Reset stateful memory (useful when restarting piece or switching biome instantly). </summary>*
- `Chord ApplyVariations(Chord chord)`
  - *<summary> Reset stateful memory (useful when restarting piece or switching biome instantly). </summary>*
- `float BaseFunctionalScore(int from, int to)`
  - *<summary> Reset stateful memory (useful when restarting piece or switching biome instantly). </summary>*

### ChordProgressionLibrary: 
> /// Deterministic modal chord progressions and transitions.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionLibrary.cs`

**Methods:**
- `None ChordProgressionLibrary()`
- `List<Chord> GetProgression(KeyScale key, int variant, bool useSevenths)`
  - *Generate a modal progression for a key.*
- `List<Chord> GetTransition(KeyScale from, KeyScale to)`
  - *Determines a simple deterministic 1–2 chord modulation bridge.*

### INoteGenerator: 
> /// Common interface for melodic generators (Markov, Rule-based, etc.).
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\INoteGenerator.cs`

**Methods:**
- `List<Note> Generate(KeyScale scale, int length, Note minNote, Note maxNote, int seed)`
  - */// Generate a melodic note sequence constrained to a scale and range.
        ///*
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
  - *Generate ONE continuation note based on context.*

### MarkovMelodyGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\MarkovMelodyGenerator.cs`

**Inherits:** INoteGenerator

**Methods:**
- `None MarkovMelodyGenerator(KeyScale scale)`
- `None MarkovMelodyGenerator()`
- `void Rebuild(KeyScale scale)`
- `void SetSigma(float newSigma)`
- `List<Note> Generate(KeyScale scale, int length, Note minNote, Note maxNote, int seed)`
- `new Note()`
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
- `new Note()`
- `int SampleNext(int current, int prev, int midiMin, int midiMax)`
- `return GetFirst()`
- `void BuildMatrices()`
- `void InterpolateTo(KeyScale other, float alpha)`
  - */// Blend this generator toward another scale (0→this, 1→other), in-place.
        ///*
- `None MarkovMelodyGenerator()`
- `else for(int j, < 128)`

### RuleMelodyGenerator: 
> /// Lightweight contour-based generator:
    /// - stays in scale
    /// - prefers stepwise motion
    /// - supports occasional leaps
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\RuleMelodyGenerator.cs`

**Inherits:** INoteGenerator

**Methods:**
- `List<Note> Generate(KeyScale scale, int length, Note minNote, Note maxNote, int seed)`
- `new Note()`
- `new Note()`
- `new Note()`
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
- `new Note(?? midiMin)`
- `new Note()`
- `new Note()`
- `new Note()`
- `int ClosestIndexSteps(List<int> pool, int currentMidi, int scaleSteps)`

### PatternEvolution: 
> /// Maintains and mutates the currently active melody & rhythm phrases.
    /// Keeps short-term musical memory for coherent evolution.
    ///

**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Pattern\PatternEvolution.cs`

**Methods:**
- `None PatternEvolution(INoteGenerator noteGen, RhythmPhraseGenerator rhythmGen)`
- `void Initialize(KeyScale key, int bars, int beatsPerBar, int melodyHits, int melodyOctaves)`
- `void Mutate(KeyScale key, int bars, int beatsPerBar, int melodyHits)`
  - */// Mutate rhythm and melody slightly, creating variation but preserving coherence.
        ///*
- `RhythmPhrase MutateRhythm(RhythmPhrase basePhrase)`
  - *<summary> Mutate rhythm and melody slightly, creating variation but preserving coherence. </summary>*
- `new InvalidOperationException(RythmPhrase has, no elements)`
  - *<summary> Mutate rhythm and melody slightly, creating variation but preserving coherence. </summary>*
- `new RhythmPhraseElement()`
  - *<summary> Mutate rhythm and melody slightly, creating variation but preserving coherence. </summary>*
- `new RhythmPhraseElement()`
  - *<summary> Mutate rhythm and melody slightly, creating variation but preserving coherence. </summary>*
- `else if(< 0, > 1)`
- `MelodyPhrase MutateMelody(MelodyPhrase baseMelody, KeyScale key)`
  - *<summary> Mutate rhythm and melody slightly, creating variation but preserving coherence. </summary>*
- `else if(< 0)`

### MusicTimelineQueueEditor: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\Editor\MusicTimelineQueueEditor.cs`

**Inherits:** Editor

**Methods:**
- `void OnInspectorGUI()`
```mermaid
classDiagram
Editor <|-- MusicTimelineQueueEditor
MusicTimelineQueueEditor ..> float?
MusicTimelineQueueEditor ..> List<float>
MusicTimelineQueueEditor ..> ??
MusicTimelineQueueEditor ..> IReadOnlyCollection<string>
MusicTimelineQueueEditor ..> Composer
MusicTimelineQueueEditor ..> int[]>
MusicTimelineQueueEditor ..> int[]
MusicTimelineQueueEditor ..> List<string>
MusicTimelineQueueEditor ..> else
MusicTimelineQueueEditor ..> List<ScaleProfile>
MusicTimelineQueueEditor ..> float[]
MusicTimelineQueueEditor ..> List<int[]>>
MusicTimelineQueueEditor ..> MusicTimelineQueue
MusicTimelineQueueEditor ..> Chord
MusicTimelineQueueEditor ..> Editor
MusicTimelineQueueEditor ..> PatternEvolution
MusicTimelineQueueEditor ..> KeyScale
MusicTimelineQueueEditor ..> List<Chord>
MusicTimelineQueueEditor ..> MusicalEvent
MusicTimelineQueueEditor ..> InstrumentPreset
MusicTimelineQueueEditor ..> float[]>
MusicTimelineQueueEditor ..> int?
MusicTimelineQueueEditor ..> ChordProgressionLibrary
MusicTimelineQueueEditor ..> ScaleType
MusicTimelineQueueEditor ..> MusicDirector
MusicTimelineQueueEditor ..> FillStrategy
MusicTimelineQueueEditor ..> protected
MusicTimelineQueueEditor ..> >
MusicTimelineQueueEditor ..> Note
MusicTimelineQueueEditor ..> yield
MusicTimelineQueueEditor ..> <
MusicTimelineQueueEditor ..> List<RhythmPhraseElement>
MusicTimelineQueueEditor ..> INoteGenerator
MusicTimelineQueueEditor ..> IInstrumentTrack>
MusicTimelineQueueEditor ..> List<Note>
MusicTimelineQueueEditor ..> target
MusicTimelineQueueEditor ..> var
MusicTimelineQueueEditor ..> Queue<HarmonySegment>
MusicTimelineQueueEditor ..> private
MusicTimelineQueueEditor ..> if
MusicTimelineQueueEditor ..> Note>
MusicTimelineQueueEditor ..> HarmonyTimelineManager
MusicTimelineQueueEditor ..> return
MusicTimelineQueueEditor ..> MelodyPaceMapping
MusicTimelineQueueEditor ..> List<Scheduled>
MusicTimelineQueueEditor ..> ChordType
MusicTimelineQueueEditor ..> RhythmPhraseGenerator
MusicTimelineQueueEditor ..> List<EmotionMapping>
```

