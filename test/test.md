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
- `void Initialize(KeyScale startKey)`
- `void AddInstrument(IInstrumentTrack track)`
- `void RemoveInstrument(string name)`
- `IInstrumentTrack GetInstrument(string name)`
- `void ClearInstruments()`
- `bool SetInstrumentTargetKey(string instrumentName, KeyScale target)`
- `List<MusicalEvent> ComposeBars(int numBars, int beatsPerBar, float? tempoOverride)`
```mermaid
classDiagram
MonoBehaviour <|-- Composer
Composer ..> IInstrumentTrack>
Composer ..> IReadOnlyCollection
Composer ..> KeyScale
Composer ..> MusicalEvent
Composer ..> MonoBehaviour
Composer ..> IReadOnlyCollection
Composer ..> IInstrumentTrack
```


### IInstrumentTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Methods:**
```mermaid
classDiagram
```


### BaseInstrumentTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\Composer.cs`

**Inherits:** IInstrumentTrack

**Methods:**
```mermaid
classDiagram
IInstrumentTrack <|-- BaseInstrumentTrack
BaseInstrumentTrack ..> KeyScale
BaseInstrumentTrack ..> IInstrumentTrack
```


### HarmonyTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\HarmonyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
```mermaid
classDiagram
BaseInstrumentTrack <|-- HarmonyTrack
HarmonyTrack ..> HarmonyTimelineManager
HarmonyTrack ..> BaseInstrumentTrack
HarmonyTrack ..> ChordProgressionLibrary
HarmonyTrack ..> Chord
```


### MelodyTrack: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Composition\MelodyTrack.cs`

**Inherits:** BaseInstrumentTrack

**Methods:**
```mermaid
classDiagram
BaseInstrumentTrack <|-- MelodyTrack
MelodyTrack ..> RhythmPhraseGenerator
MelodyTrack ..> BaseInstrumentTrack
MelodyTrack ..> Note
MelodyTrack ..> PatternEvolution
MelodyTrack ..> INoteGenerator
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
MusicDirector ..> Composer
MusicDirector ..> KeyScale
MusicDirector ..> MusicTimelineQueue
MusicDirector ..> MonoBehaviour
```


### HarmonySegment: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonySegment.cs`

**Methods:**
```mermaid
classDiagram
HarmonySegment ..> KeyScale
HarmonySegment ..> Chord
```


### HarmonyTimelineManager: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Harmony\HarmonyTimelineManager.cs`

**Methods:**
- `void RequestTransition(KeyScale newTarget)`
- `List<Chord> GetNextChords(int maxBars)`
```mermaid
classDiagram
HarmonyTimelineManager ..> HarmonySegment
HarmonyTimelineManager ..> KeyScale
HarmonyTimelineManager ..> ChordProgressionLibrary
HarmonyTimelineManager ..> Queue
HarmonyTimelineManager ..> Chord
```


### MusicTimelineQueueData: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Methods:**
- `float GetNextBarStart(int beatsPerBar)`
- `void AddBar(IEnumerable<MusicalEvent> newEvents, int beatsPerBar)`
- `void RemovePlayed(float elapsedSec)`
- `float ComputeBeatsAhead()`
- `void UpdateTransportGrid(float currentBeat, int beatsPerBar)`
```mermaid
classDiagram
MusicTimelineQueueData ..> Scheduled
MusicTimelineQueueData ..> MusicalEvent
MusicTimelineQueueData ..> IEnumerable
MusicTimelineQueueData ..> IEnumerable
```


### Scheduled: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Methods:**
```mermaid
classDiagram
Scheduled ..> MusicalEvent
```


### MusicTimelineQueue: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\MusicTimelineQueue.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `float GetNextBarStart(int beatsPerBar)`
- `void AddBar(IEnumerable<MusicalEvent> newEvents, int beatsPerBar)`
- `void RemovePlayed(float elapsedSec)`
- `float ComputeBeatsAhead()`
- `void UpdateTransportGrid(float currentBeat, int beatsPerBar)`
```mermaid
classDiagram
MonoBehaviour <|-- MusicTimelineQueue
MusicTimelineQueue ..> Scheduled
MusicTimelineQueue ..> MusicalEvent
MusicTimelineQueue ..> IEnumerable
MusicTimelineQueue ..> IEnumerable
MusicTimelineQueue ..> MonoBehaviour
```


### BiomeMusicSettings: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Inherits:** ScriptableObject

**Methods:**
- `EmotionMapping GetEmotionMapping(string emotion)`
- `ScaleProfile GetRandomScale()`
```mermaid
classDiagram
ScriptableObject <|-- BiomeMusicSettings
BiomeMusicSettings ..> ScaleProfile
BiomeMusicSettings ..> InstrumentPreset
BiomeMusicSettings ..> ScriptableObject
BiomeMusicSettings ..> EmotionMapping
BiomeMusicSettings ..> MelodyPaceMapping
```


### InstrumentPreset: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**
```mermaid
classDiagram
```


### ScaleProfile: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**
```mermaid
classDiagram
ScaleProfile ..> ScaleType
```


### EmotionMapping: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**
```mermaid
classDiagram
EmotionMapping ..> ScaleType
```


### MelodyPaceMapping: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\BiomeMusicSettings.cs`

**Methods:**
```mermaid
classDiagram
```


### MusicGenSettings: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettings.cs`

**Inherits:** ScriptableObject

**Methods:**
- `void OnEnable()`
- `void OnValidate()`
- `void Apply()`
- `void SetTempo(float newTempo)`
```mermaid
classDiagram
ScriptableObject <|-- MusicGenSettings
MusicGenSettings ..> ScriptableObject
```


### MusicGenSettingsLoader: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Settings\MusicGenSettingsLoader.cs`

**Inherits:** MonoBehaviour

**Methods:**
- `void SetTempo(float newTempo)`
```mermaid
classDiagram
MonoBehaviour <|-- MusicGenSettingsLoader
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
- `void BuildNotes()`
- `Chord GetInversion(int inversion)`
- `Chord AddExtension(int semitone)`
- `List<Note> GetArpeggio(ArpeggioStyle style, int octaves)`
```mermaid
classDiagram
Chord ..> ArpeggioStyle
Chord ..> Note
```


### MusicalEvent: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Events\MusicalEvent.cs`

**Methods:**
```mermaid
classDiagram
```


### MelodyPhrase: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhrase.cs`

**Methods:**
- `MelodyPhrase Clone()`
```mermaid
classDiagram
MelodyPhrase ..> Note
```


### MelodyPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Melody\MelodyPhraseExtensions.Basic.cs`

**Methods:**
```mermaid
classDiagram
MelodyPhraseExtensions ..> Note
```


### Note: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\Note.cs`

**Methods:**
```mermaid
classDiagram
```


### NoteMap: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteMap.cs`

**Methods:**
- `Note GetNote(int midiNote)`
```mermaid
classDiagram
NoteMap ..> Note>
NoteMap ..> Note
```


### NoteUtilities: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Notes\NoteUtilities.cs`

**Methods:**
```mermaid
classDiagram
```


### RhythmPhrase: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhrase.cs`

**Methods:**
- `RhythmPhrase Clone()`
- `IEnumerable<RhythmPhraseElement> LongestElements()`
- `IEnumerable<RhythmPhraseElement> ShortestElements()`
```mermaid
classDiagram
RhythmPhrase ..> IEnumerable
RhythmPhrase ..> IEnumerable
RhythmPhrase ..> RhythmPhraseElement
```


### RhythmPhraseExtensions: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseExtensions.cs`

**Methods:**
```mermaid
classDiagram
```


### RhythmPhraseGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Rythm\RhythmPhraseGenerator.cs`

**Methods:**
- `RhythmPhrase GenerateSmart(int beatsPerBar, int numBars, int numHits, FillStrategy strategy, int seed, bool randomizeOrder)`
- `RhythmPhrase GenerateSubdividedVariation(RhythmPhrase basePhrase, float intensity, int seed)`
```mermaid
classDiagram
RhythmPhraseGenerator ..> FillStrategy
RhythmPhraseGenerator ..> RhythmPhrase
```


### KeyScale: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Core\Scales\KeyScale.cs`

**Methods:**
- `void BuildNotes()`
- `List<Note> GetNotes()`
- `Note GetTonic()`
- `Note GetNoteByDegreeOffset(Note from, int diatonicSteps, int midiMin, int midiMax)`
- `List<int> BuildDiatonicLadder(int midiMin, int midiMax)`
- `List<Chord> GetDiatonicChords(bool useSevenths)`
- `Chord GetChord(int degree, bool useSevenths)`
```mermaid
classDiagram
KeyScale ..> ChordType
KeyScale ..> Note
KeyScale ..> Chord
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
```mermaid
classDiagram
```


### ChordProgressionGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionGenerator.cs`

**Methods:**
- `List<Chord> Generate(KeyScale startKey, int numChords, int seed, KeyScale targetKey, float modulationBias)`
- `void ResetState()`
- `List<Chord> GenerateGradualModulation(KeyScale currentKey, KeyScale targetKey, int numChords, float modulationBias)`
- `List<Chord> GenerateForceArrival(KeyScale fromKey, KeyScale toKey, int numChords, float modulationBias)`
- `Chord FindPivotChord(KeyScale a, KeyScale b)`
- `Chord PickNextChord(Chord current, List<Chord> pool, KeyScale currentKey, KeyScale targetKey, float modulationBias)`
- `Chord ApplyVariations(Chord chord)`
```mermaid
classDiagram
ChordProgressionGenerator ..> KeyScale
ChordProgressionGenerator ..> Chord
```


### ChordProgressionLibrary: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Chord\ChordProgressionLibrary.cs`

**Methods:**
- `List<Chord> GetProgression(KeyScale key, int variant, bool useSevenths)`
- `List<Chord> GetTransition(KeyScale from, KeyScale to)`
```mermaid
classDiagram
ChordProgressionLibrary ..> List>
ChordProgressionLibrary ..> KeyScale
ChordProgressionLibrary ..> Chord
```


### INoteGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\INoteGenerator.cs`

**Methods:**
```mermaid
classDiagram
```


### MarkovMelodyGenerator: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Note\MarkovMelodyGenerator.cs`

**Inherits:** INoteGenerator

**Methods:**
- `void Rebuild(KeyScale scale)`
- `void SetSigma(float newSigma)`
- `List<Note> Generate(KeyScale scale, int length, Note minNote, Note maxNote, int seed)`
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
- `int SampleNext(int current, int prev, int midiMin, int midiMax)`
- `void BuildMatrices()`
- `void InterpolateTo(KeyScale other, float alpha)`
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
- `Note GenerateNext(KeyScale scale, Note previous, Note minNote, Note maxNote)`
- `int ClosestIndexSteps(List<int> pool, int currentMidi, int scaleSteps)`
```mermaid
classDiagram
INoteGenerator <|-- RuleMelodyGenerator
RuleMelodyGenerator ..> KeyScale
RuleMelodyGenerator ..> Note
RuleMelodyGenerator ..> INoteGenerator
```


### PatternEvolution: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Generators\Pattern\PatternEvolution.cs`

**Methods:**
- `void Initialize(KeyScale key, int bars, int beatsPerBar, int melodyHits, int melodyOctaves)`
- `void Mutate(KeyScale key, int bars, int beatsPerBar, int melodyHits)`
- `RhythmPhrase MutateRhythm(RhythmPhrase basePhrase)`
- `MelodyPhrase MutateMelody(MelodyPhrase baseMelody, KeyScale key)`
```mermaid
classDiagram
PatternEvolution ..> MelodyPhrase
PatternEvolution ..> RhythmPhraseGenerator
PatternEvolution ..> KeyScale
PatternEvolution ..> RhythmPhrase
PatternEvolution ..> Note
PatternEvolution ..> INoteGenerator
```


### MusicTimelineQueueEditor: 
**File:** `C:\Users\jange\MusicGeneration\Assets\_Project\Audio\MusicGen\Playback\Editor\MusicTimelineQueueEditor.cs`

**Inherits:** Editor

**Methods:**
```mermaid
classDiagram
Editor <|-- MusicTimelineQueueEditor
```


## Global Architecture Diagram
```mermaid
classDiagram
BaseInstrumentTrack --> IInstrumentTrack
BaseInstrumentTrack --> KeyScale
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
IInstrumentTrack <|-- BaseInstrumentTrack
INoteGenerator <|-- MarkovMelodyGenerator
INoteGenerator <|-- RuleMelodyGenerator
KeyScale --> Chord
KeyScale --> Note
MarkovMelodyGenerator --> INoteGenerator
MarkovMelodyGenerator --> KeyScale
MarkovMelodyGenerator --> Note
MelodyPhrase --> Note
MelodyPhraseExtensions --> Note
MelodyTrack --> BaseInstrumentTrack
MelodyTrack --> INoteGenerator
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
Scheduled --> MusicalEvent
TestMusicSetup --> MusicDirector
