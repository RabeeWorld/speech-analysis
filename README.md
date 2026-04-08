# speech-analysis

This project analyzes a speech audio file to detect:

⏸️ Pause Segments — Silent regions in speech
🔁 Repetitions — Stuttered speech patterns such as "ba-ba-ball" or "I-I-I want"

The system is designed with a modular pipeline that processes audio, extracts meaningful features, and applies detection logic to produce structured results.

🧠 Approach

The overall pipeline is:

Audio → Preprocessing → Feature Extraction → Detection → Output + Visualization
⚙️ Audio Preprocessing
Audio is loaded using librosa

Normalization is applied to ensure consistent amplitude:

→ This helps improve reliability of feature extraction and threshold-based detection

Basic noise robustness is achieved through:
RMS-based filtering
Minimum duration constraints
🎧 Feature Extraction
🔹 Pause Detection
RMS Energy (Root Mean Square) is used
Represents loudness over time
Low RMS values indicate silence
🔹 Repetition Detection
MFCC (Mel-Frequency Cepstral Coefficients) are used
MFCCs are derived from the spectrogram and capture speech characteristics
Each audio segment is converted into a compact feature vector
⏸️ Pause Detection Logic
Audio is divided into frames
RMS energy is computed for each frame

A dynamic threshold is used:

threshold = mean(RMS) × factor
Frames below threshold are considered silent
Consecutive silent frames are grouped into segments
Very short pauses are removed using a minimum duration filter
✅ Output:
Start and end time of each pause
Total pause duration
🔁 Repetition Detection Logic
🔹 Step 1: Segmentation
Audio is split into small overlapping segments
Helps capture short stutter patterns
🔹 Step 2: Feature Comparison
MFCC features are extracted for each segment
Cosine similarity is used to compare consecutive segments
Similarity = 1 - cosine distance
High similarity → possible repetition
🔹 Step 3: Segment Merging
Overlapping repetition detections are merged
Avoids duplicate detections
🔹 Step 4: Speech-to-Text Enhancement
Google Speech Recognition API is used to convert audio to text
Text is analyzed to detect repetition patterns like:
"I-I-I want"
"ba-ba-ball"
🔹 Step 5: Pattern Detection
Consecutive repeated words are identified
Pattern is constructed and repetition count is calculated
📊 Visualization
Waveform is plotted using matplotlib
Pause regions are highlighted for visual understanding
Output saved as:
plots/waveform.png
📦 Output Example
Pause Segments:
[0.50s – 1.20s]
[2.10s – 2.80s]

Total Pause Duration: 1.40s

Repetitions:
Detected pattern: "I-I-I want"
Repetition Count: 3
🧪 Libraries Used
librosa → audio processing
numpy → numerical operations
matplotlib → visualization
scipy → similarity computation
speech_recognition → speech-to-text
⚠️ Challenges Faced
1. Noise Sensitivity
Low-level noise can affect pause detection
Mitigated using thresholding and duration filtering
2. Repetition Detection Complexity
Similar sounds ≠ actual repetition
Addressed using MFCC + similarity + text validation
3. Speech Recognition Limitations
Accuracy depends on audio quality and internet API
Handled using error handling and fallback logic
4. Overlapping Detections
Multiple detections for same repetition
Solved using segment merging
