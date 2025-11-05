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
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `[constructor] None Composer()`
- `void Initialize(KeyScale startKey)`
- `void AddInstrument(IInstrumentTrack track)`
- `void RemoveInstrument(string name)`
- `IInstrumentTrack GetInstrument(string name)`
- `void ClearInstruments()`
- `bool SetInstrumentTargetKey(string instrumentName, KeyScale target)`
- `List<MusicalEvent> ComposeBars(int numBars, int beatsPerBar, float? tempoOverride)`

### IInstrumentTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Methods:**
- `void SetCurrentKey(KeyScale key)`
- `void SetTargetKey(KeyScale key)`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`

### BaseInstrumentTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Inherits:** IInstrumentTrack

**Methods:**
- `[constructor] None BaseInstrumentTrack(string name, int channel, KeyScale startKey)`
- `void SetCurrentKey(KeyScale key)`
- `void SetTargetKey(KeyScale key)`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `bool KeyEquals(KeyScale a, KeyScale b)`
```mermaid
classDiagram
MonoBehaviour <|-- Composer
Composer ..> MusicalEvent
Composer ..> IInstrumentTrack
Composer ..> IReadOnlyCollection
Composer ..> IReadOnlyCollection
Composer ..> IInstrumentTrack>
Composer ..> MonoBehaviour
Composer ..> KeyScale
IInstrumentTrack ..> MusicalEvent
IInstrumentTrack ..> KeyScale
IInstrumentTrack <|-- BaseInstrumentTrack
BaseInstrumentTrack ..> IInstrumentTrack
BaseInstrumentTrack ..> MusicalEvent
BaseInstrumentTrack ..> KeyScale
```


### HarmonyTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\HarmonyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
- `[constructor] None HarmonyTrack(string name, int channel, KeyScale startKey, ChordProgressionLibrary library, bool useArpeggios, int velocity)`
- `void SetCurrentKey(KeyScale key)`
- `void SetTargetKey(KeyScale key)`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `new MusicalEvent()`
- `new MusicalEvent()`
```mermaid
classDiagram
BaseInstrumentTrack <|-- HarmonyTrack
HarmonyTrack ..> ChordProgressionLibrary
HarmonyTrack ..> MusicalEvent
HarmonyTrack ..> Chord
HarmonyTrack ..> BaseInstrumentTrack
HarmonyTrack ..> KeyScale
HarmonyTrack ..> HarmonyTimelineManager
```


### MelodyTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\MelodyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
- `[constructor] None MelodyTrack(string name, int channel, KeyScale startKey, INoteGenerator noteGen, RhythmPhraseGenerator rhythmGen, int hitsPerBar, int velocity, float mutationProb, float mutationIntensity)`
- `new PatternEvolution()`
- `List<MusicalEvent> ComposeBar(float secondsPerBeat, int beatsPerBar)`
- `new MusicalEvent()`
```mermaid
classDiagram
BaseInstrumentTrack <|-- MelodyTrack
MelodyTrack ..> PatternEvolution
MelodyTrack ..> MusicalEvent
MelodyTrack ..> Note
MelodyTrack ..> INoteGenerator
MelodyTrack ..> BaseInstrumentTrack
MelodyTrack ..> KeyScale
MelodyTrack ..> RhythmPhraseGenerator
```


### MusicDirector: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\MusicDirector.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void Awake()`
- `void StartMusic()`
- `void StopMusic()`
- `void SetTempo(float bpm)`
- `void ApplyKeyChangeToInstrument(string instrumentName, KeyScale targetKey, int transitionBars)`
- `void ApplyGlobalKeyChange(KeyScale targetKey, int transitionBars)`
```mermaid
classDiagram
MonoBehaviour <|-- MusicDirector
MusicDirector ..> KeyScale
MusicDirector ..> Composer
MusicDirector ..> MusicTimelineQueue
MusicDirector ..> MonoBehaviour
```


### HarmonySegment: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonySegment.cs`

**Methods:**
- `[constructor] None HarmonySegment(KeyScale key, List<Chord> chords, int bars, bool isTransition)`
```mermaid
classDiagram
HarmonySegment ..> KeyScale
HarmonySegment ..> Chord
```


### HarmonyTimelineManager: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonyTimelineManager.cs`

**Methods:**
- `[constructor] None HarmonyTimelineManager(ChordProgressionLibrary library, KeyScale start)`
- `new ChordProgressionLibrary()`
- `new KeyScale()`
- `void RequestTransition(KeyScale newTarget)`
- `new HarmonySegment()`
- `new HarmonySegment()`
- `List<Chord> GetNextChords(int maxBars)`
- `new HarmonySegment()`
```mermaid
classDiagram
HarmonyTimelineManager ..> HarmonySegment
HarmonyTimelineManager ..> ChordProgressionLibrary
HarmonyTimelineManager ..> KeyScale
HarmonyTimelineManager ..> Chord
```


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
- `[constructor] None Scheduled(MusicalEvent e, bool isNoteOff)`

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
```mermaid
classDiagram
MusicTimelineQueueData ..> Scheduled
MusicTimelineQueueData ..> MusicalEvent
Scheduled ..> MusicalEvent
MonoBehaviour <|-- MusicTimelineQueue
MusicTimelineQueue ..> Scheduled
MusicTimelineQueue ..> MonoBehaviour
MusicTimelineQueue ..> MusicalEvent
```


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
```mermaid
classDiagram
ScriptableObject <|-- BiomeMusicSettings
BiomeMusicSettings ..> InstrumentPreset
BiomeMusicSettings ..> EmotionMapping
BiomeMusicSettings ..> ScriptableObject
BiomeMusicSettings ..> MelodyPaceMapping
BiomeMusicSettings ..> ScaleProfile
ScaleProfile ..> ScaleType
EmotionMapping ..> ScaleType
```


### MusicGenSettings: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettings.cs`

**Inherits:** ScriptableObject

**Methods:**
- `void OnEnable()`
- `void OnValidate()`
- `void SubscribeToTempoChange(Action<float> listener)`
- `void Apply()`
- `void SetTempo(float newTempo)`
```mermaid
classDiagram
ScriptableObject <|-- MusicGenSettings
MusicGenSettings ..> Action
MusicGenSettings ..> ScriptableObject
MusicGenSettings ..> Action
```


### MusicGenSettingsLoader: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettingsLoader.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void Awake()`
- `Settings loaded()`
- `void SetTempo(float newTempo)`
```mermaid
classDiagram
MonoBehaviour <|-- MusicGenSettingsLoader
MusicGenSettingsLoader ..> Settings
MusicGenSettingsLoader ..> MonoBehaviour
```


### TestMusicSetup: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Test\TestMusicSetup.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void Awake()`
- `void Play()`
- `void Update()`
```mermaid
classDiagram
MonoBehaviour <|-- TestMusicSetup
TestMusicSetup ..> MonoBehaviour
TestMusicSetup ..> MusicDirector
```


### Chord: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Chords\Chord.cs`

**Methods:**
- `[constructor] None Chord(Note root, ChordType type, int scaleDegree)`
- `void BuildNotes()`
- `new Note()`
- `Chord GetInversion(int inversion)`
- `new Note()`
- `Chord AddExtension(int semitone)`
- `List<Note> GetArpeggio(ArpeggioStyle style, int octaves)`
- `new Note()`
- `string ToString()`
```mermaid
classDiagram
Chord ..> ChordType
Chord ..> ArpeggioStyle
Chord ..> Note
```

```mermaid
classDiagram
```


### MusicalEvent: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Events\MusicalEvent.cs`

**Methods:**
- `[constructor] None MusicalEvent(float startBeat, float durationBeats, int velocity, int channel, int? program)`
- `string ToString()`
```mermaid
classDiagram
```


### MelodyPhrase: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhrase.cs`

**Methods:**
- `[constructor] None MelodyPhrase()`
- `[constructor] None MelodyPhrase(IEnumerable<Note> notes)`
- `MelodyPhrase Clone()`
- `new Note()`
- `string ToString()`
```mermaid
classDiagram
MelodyPhrase ..> Note
```


### MelodyPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhraseExtensions.Basic.cs`

**Methods:**
- `MelodyPhrase Transpose(this MelodyPhrase, int semitones)`
- `MelodyPhrase SwapAdjacent(this MelodyPhrase, float probability)`
- `MelodyPhrase InvertAround(this MelodyPhrase, Note axis)`
- `MelodyPhrase ConstrainToScale(this MelodyPhrase, KeyScale scale, int min, int max)`
- `void InsertNote(this MelodyPhrase, int index, Note note)`
- `new Note()`
- `void AddNote(this MelodyPhrase, Note note)`
- `new Note()`
- `void RemoveNoteAt(this MelodyPhrase, int index)`
- `bool RemoveRandomNote(this MelodyPhrase, Random rng)`
- `void RemoveNotes(this MelodyPhrase, int count, Random rng)`
- `void InsertNeighborNote(this MelodyPhrase, int index, KeyScale scale, int minStep, int maxStep, Random rng)`
- `void AddMultipleNotes(this MelodyPhrase, int count, KeyScale scale, Random rng)`
- `void InsertMusicalNote(this MelodyPhrase, KeyScale scale, Random rng)`
- `else if(< 0)`
```mermaid
classDiagram
MelodyPhraseExtensions ..> KeyScale
MelodyPhraseExtensions ..> Random
MelodyPhraseExtensions ..> MelodyPhrase
MelodyPhraseExtensions ..> Note
```


### Note: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\Note.cs`

**Methods:**
- `[constructor] None Note(int midiNote)`
- `[constructor] None Note(NoteName noteName, int octave)`
- `[constructor] None Note(NotePitch pitch)`
- `string ToString()`
```mermaid
classDiagram
Note ..> NotePitch
Note ..> NoteName
```


### NoteMap: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteMap.cs`

**Methods:**
- `[constructor] None NoteMap()`
- `Note GetNote(int midiNote)`
```mermaid
classDiagram
NoteMap ..> Note>
NoteMap ..> Note
```

```mermaid
classDiagram
```

```mermaid
classDiagram
```


### NoteUtilities: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteUtilities.cs`

**Methods:**
- `float MidiToFrequency(int midiNote)`
- `int FrequencyToMidi(float frequency)`
- `Note Transpose(Note note, int semitones)`
- `new Note()`
- `int Interval(Note a, Note b)`
- `string GetNoteNameFromMidi(int midiNote)`
- `List<string> RangeNames(int startMidi, int endMidi)`
```mermaid
classDiagram
NoteUtilities ..> Note
```


### RhythmPhrase: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhrase.cs`

**Methods:**
- `string ToString()`
- `RhythmPhrase Clone()`
- `new RhythmPhraseElement()`
- `IEnumerable<RhythmPhraseElement> LongestElements()`
- `IEnumerable<RhythmPhraseElement> ShortestElements()`
```mermaid
classDiagram
RhythmPhrase ..> RhythmPhraseElement
```

```mermaid
classDiagram
```


### RhythmPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseExtensions.cs`

**Methods:**
- `void NormalizeToBeats(this RhythmPhrase, float targetBeats)`
```mermaid
classDiagram
```


### RhythmPhraseGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseGenerator.cs`

**Methods:**
- `RhythmPhrase GenerateSmart(int beatsPerBar, int numBars, int numHits, FillStrategy strategy, int seed, bool randomizeOrder)`
- `else ApplyStochasticAdjustment()`
- `new RhythmPhraseElement()`
- `RhythmPhrase GenerateSubdividedVariation(RhythmPhrase basePhrase, float intensity, int seed)`
- `new RhythmPhraseElement()`
- `List<float> InitializeDurations(int numHits, float target)`
- `void ApplyDeterministicCorrection(List<float> durations, float diff)`
- `void ApplyStochasticAdjustment(List<float> durations, float diff)`
- `float SnapToClosestMusicalValue(float val)`
- `float TryHalve(float dur)`
- `float TryDouble(float dur)`
```mermaid
classDiagram
RhythmPhraseGenerator ..> RhythmPhrase
RhythmPhraseGenerator ..> FillStrategy
```


### KeyScale: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\KeyScale.cs`

**Methods:**
- `[constructor] None KeyScale(NoteName root, ScaleType scaleType)`
- `void BuildNotes()`
- `new Note()`
- `List<Note> GetNotes()`
- `Note GetTonic()`
- `new Note()`
- `Note GetNoteByDegreeOffset(Note from, int diatonicSteps, int midiMin, int midiMax)`
- `new Note()`
- `List<int> BuildDiatonicLadder(int midiMin, int midiMax)`
- `List<Chord> GetDiatonicChords(bool useSevenths)`
- `else if()`
- `else if()`
- `else if()`
- `new Chord()`
- `Chord GetChord(int degree, bool useSevenths)`
- `new Chord(new Note)`
- `string ToString()`
```mermaid
classDiagram
KeyScale ..> ScaleType
KeyScale ..> Chord
KeyScale ..> Note
KeyScale ..> NoteName
KeyScale ..> ChordType
```


### ScaleIntervals: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleType.cs`

**Methods:**
```mermaid
classDiagram
```


### ScaleUtils: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\ScaleUtils.cs`

**Methods:**
- `HashSet<int> PitchClasses(KeyScale ks)`
- `HashSet<int> PitchClassIntersection(KeyScale a, KeyScale b)`
- `List<int> NotesInRange(KeyScale ks, int midiMin, int midiMax)`
- `int NearestCommonTone(int sourceMidi, KeyScale src, KeyScale dst, int midiMin, int midiMax)`
- `return NearestScaleNote()`
- `int NearestScaleNote(int sourceMidi, KeyScale ks, int midiMin, int midiMax)`
- `bool ContainsPitchClass(this KeyScale, int pitchClass)`
```mermaid
classDiagram
ScaleUtils ..> KeyScale
```


### ChordProgressionGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionGenerator.cs`

**Methods:**
- `List<Chord> Generate(KeyScale startKey, int numChords, int seed, KeyScale targetKey, float modulationBias)`
- `new KeyScale()`
- `void ResetState()`
- `List<Chord> GenerateGradualModulation(KeyScale currentKey, KeyScale targetKey, int numChords, float modulationBias)`
- `List<Chord> GenerateForceArrival(KeyScale fromKey, KeyScale toKey, int numChords, float modulationBias)`
- `Chord FindPivotChord(KeyScale a, KeyScale b)`
- `Chord PickNextChord(Chord current, List<Chord> pool, KeyScale currentKey, KeyScale targetKey, float modulationBias)`
- `Chord ApplyVariations(Chord chord)`
- `float BaseFunctionalScore(int from, int to)`
```mermaid
classDiagram
ChordProgressionGenerator ..> KeyScale
ChordProgressionGenerator ..> Chord
```


### ChordProgressionLibrary: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionLibrary.cs`

**Methods:**
- `[constructor] None ChordProgressionLibrary()`
- `List<Chord> GetProgression(KeyScale key, int variant, bool useSevenths)`
- `List<Chord> GetTransition(KeyScale from, KeyScale to)`
```mermaid
classDiagram
ChordProgressionLibrary ..> KeyScale
ChordProgressionLibrary ..> Chord
```


### INoteGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\INoteGenerator.cs`

**Methods:**
- `List<Note> Generate(KeyScale scale, int length, Note minNote, Note maxNote, int seed)`
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
```mermaid
classDiagram
INoteGenerator ..> KeyScale
INoteGenerator ..> Note
```


### MarkovMelodyGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\MarkovMelodyGenerator.cs`

**Inherits:** INoteGenerator

**Methods:**
- `[constructor] None MarkovMelodyGenerator(KeyScale scale)`
- `[constructor] None MarkovMelodyGenerator()`
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
- `[constructor] None MarkovMelodyGenerator()`
- `else for(int j, < 128)`
```mermaid
classDiagram
INoteGenerator <|-- MarkovMelodyGenerator
MarkovMelodyGenerator ..> KeyScale
MarkovMelodyGenerator ..> INoteGenerator
MarkovMelodyGenerator ..> Note
```


### RuleMelodyGenerator: 
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
```mermaid
classDiagram
INoteGenerator <|-- RuleMelodyGenerator
RuleMelodyGenerator ..> KeyScale
RuleMelodyGenerator ..> INoteGenerator
RuleMelodyGenerator ..> Note
```


### PatternEvolution: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Pattern\PatternEvolution.cs`

**Methods:**
- `[constructor] None PatternEvolution(INoteGenerator noteGen, RhythmPhraseGenerator rhythmGen)`
- `void Initialize(KeyScale key, int bars, int beatsPerBar, int melodyHits, int melodyOctaves)`
- `void Mutate(KeyScale key, int bars, int beatsPerBar, int melodyHits)`
- `RhythmPhrase MutateRhythm(RhythmPhrase basePhrase)`
- `new RhythmPhraseElement()`
- `new RhythmPhraseElement()`
- `else if(< 0, > 1)`
- `MelodyPhrase MutateMelody(MelodyPhrase baseMelody, KeyScale key)`
- `else if(< 0)`
```mermaid
classDiagram
PatternEvolution ..> RhythmPhrase
PatternEvolution ..> Note
PatternEvolution ..> INoteGenerator
PatternEvolution ..> KeyScale
PatternEvolution ..> MelodyPhrase
PatternEvolution ..> RhythmPhraseGenerator
```


### MusicTimelineQueueEditor: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\Editor\MusicTimelineQueueEditor.cs`

**Inherits:** Editor

**Methods:**
- `void OnInspectorGUI()`
```mermaid
classDiagram
Editor <|-- MusicTimelineQueueEditor
```


## Global Architecture Diagram
```mermaid
classDiagram
BaseInstrumentTrack --> IInstrumentTrack
BaseInstrumentTrack --> KeyScale
BaseInstrumentTrack --> MusicalEvent
BaseInstrumentTrack <|-- HarmonyTrack
BaseInstrumentTrack <|-- MelodyTrack
BiomeMusicSettings --> EmotionMapping
BiomeMusicSettings --> InstrumentPreset
BiomeMusicSettings --> MelodyPaceMapping
BiomeMusicSettings --> ScaleProfile
Chord --> Note
ChordProgressionGenerator --> Chord
ChordProgressionGenerator --> KeyScale
ChordProgressionLibrary --> Chord
ChordProgressionLibrary --> KeyScale
Composer --> IInstrumentTrack
Composer --> KeyScale
Composer --> MusicalEvent
HarmonySegment --> Chord
HarmonySegment --> KeyScale
HarmonyTimelineManager --> Chord
HarmonyTimelineManager --> ChordProgressionLibrary
HarmonyTimelineManager --> HarmonySegment
HarmonyTimelineManager --> KeyScale
HarmonyTrack --> BaseInstrumentTrack
HarmonyTrack --> Chord
HarmonyTrack --> ChordProgressionLibrary
HarmonyTrack --> HarmonyTimelineManager
HarmonyTrack --> KeyScale
HarmonyTrack --> MusicalEvent
IInstrumentTrack --> KeyScale
IInstrumentTrack --> MusicalEvent
IInstrumentTrack <|-- BaseInstrumentTrack
INoteGenerator --> KeyScale
INoteGenerator --> Note
INoteGenerator <|-- MarkovMelodyGenerator
INoteGenerator <|-- RuleMelodyGenerator
KeyScale --> Chord
KeyScale --> Note
MarkovMelodyGenerator --> INoteGenerator
MarkovMelodyGenerator --> KeyScale
MarkovMelodyGenerator --> Note
MelodyPhrase --> Note
MelodyPhraseExtensions --> KeyScale
MelodyPhraseExtensions --> MelodyPhrase
MelodyPhraseExtensions --> Note
MelodyTrack --> BaseInstrumentTrack
MelodyTrack --> INoteGenerator
MelodyTrack --> KeyScale
MelodyTrack --> MusicalEvent
MelodyTrack --> Note
MelodyTrack --> PatternEvolution
MelodyTrack --> RhythmPhraseGenerator
MusicDirector --> Composer
MusicDirector --> KeyScale
MusicDirector --> MusicTimelineQueue
MusicTimelineQueue --> MusicalEvent
MusicTimelineQueue --> Scheduled
MusicTimelineQueueData --> MusicalEvent
MusicTimelineQueueData --> Scheduled
NoteMap --> Note
NoteUtilities --> Note
PatternEvolution --> INoteGenerator
PatternEvolution --> KeyScale
PatternEvolution --> MelodyPhrase
PatternEvolution --> Note
PatternEvolution --> RhythmPhrase
PatternEvolution --> RhythmPhraseGenerator
RhythmPhraseGenerator --> RhythmPhrase
RuleMelodyGenerator --> INoteGenerator
RuleMelodyGenerator --> KeyScale
RuleMelodyGenerator --> Note
ScaleUtils --> KeyScale
Scheduled --> MusicalEvent
TestMusicSetup --> MusicDirector
