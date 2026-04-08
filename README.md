# 🎙️ Speech Analysis: Pause & Repetition Detection

## 📌 Overview

This project analyzes a speech audio file to detect:

* ⏸️ **Pause Segments** — Silent regions in speech
* 🔁 **Repetitions** — Stuttered speech patterns such as "ba-ba-ball" or "I-I-I want"

The system is designed with a modular pipeline that processes audio, extracts meaningful features, and applies detection logic to produce structured results.

---

## 🧠 Approach

The overall pipeline is:

```
Audio → Preprocessing → Feature Extraction → Detection → Output + Visualization
```

---

## ⚙️ Audio Preprocessing

* Audio is loaded using `librosa`

* Normalization is applied to ensure consistent amplitude:

  → This helps improve reliability of feature extraction and threshold-based detection

* Basic noise robustness is achieved through:

  * RMS-based filtering
  * Minimum duration constraints

---

## 🎧 Feature Extraction

### 🔹 Pause Detection

* **RMS Energy (Root Mean Square)** is used
* Represents loudness over time
* Low RMS values indicate silence

---

### 🔹 Repetition Detection

* **MFCC (Mel-Frequency Cepstral Coefficients)** are used
* MFCCs are derived from the spectrogram and capture speech characteristics
* Each audio segment is converted into a compact feature vector

---

## ⏸️ Pause Detection Logic

1. Audio is divided into frames
2. RMS energy is computed for each frame
3. A **dynamic threshold** is used:

   ```
   threshold = mean(RMS) × factor
   ```
4. Frames below threshold are considered silent
5. Consecutive silent frames are grouped into segments
6. Very short pauses are removed using a **minimum duration filter**

### ✅ Output:

* Start and end time of each pause
* Total pause duration

---

## 🔁 Repetition Detection Logic

### 🔹 Step 1: Segmentation

* Audio is split into **small overlapping segments**
* Helps capture short stutter patterns

---

### 🔹 Step 2: Feature Comparison

* MFCC features are extracted for each segment
* Cosine similarity is used to compare consecutive segments

```
Similarity = 1 - cosine distance
```

* High similarity → possible repetition

---

### 🔹 Step 3: Segment Merging

* Overlapping repetition detections are merged
* Avoids duplicate detections

---

### 🔹 Step 4: Speech-to-Text Enhancement

* Google Speech Recognition API is used to convert audio to text
* Text is analyzed to detect repetition patterns like:

  * "I-I-I want"
  * "ba-ba-ball"

---

### 🔹 Step 5: Pattern Detection

* Consecutive repeated words are identified
* Pattern is constructed and repetition count is calculated

---

## 📊 Visualization

* Waveform is plotted using `matplotlib`
* Pause regions are highlighted for visual understanding
* Output saved as:

```
plots/waveform.png
```

---

## 📦 Output Example

```
Pause Segments:
[0.50s – 1.20s]
[2.10s – 2.80s]

Total Pause Duration: 1.40s

Repetitions:
Detected pattern: "I-I-I want"
Repetition Count: 3
```

---

## 🧪 Libraries Used

* `librosa` → audio processing
* `numpy` → numerical operations
* `matplotlib` → visualization
* `scipy` → similarity computation
* `speech_recognition` → speech-to-text

---

## ⚠️ Challenges Faced

### 🔴 1. Speech Recognition Limitations

* Speech-to-text struggles with stuttering patterns like **"b-b-b-ball"**
* May return incorrect or incomplete text
* Performance depends on external API accuracy

---

### 🔴 2. Stuttering vs Clean Repetition

* Stuttering is often **irregular and fragmented**, unlike clean repetition
* Required:

  * Smaller segment sizes
  * Lower similarity thresholds
* Increased complexity in detecting true repetition patterns

---

### 🔴 3. Threshold Sensitivity

* Detection heavily depends on threshold values:

  * High threshold → **missed detections**
  * Low threshold → **false positives**
* Required careful tuning for different audio samples

---

### 🔴 4. Noise & Audio Quality

* Background noise affects MFCC feature extraction
* Poor-quality recordings reduce detection accuracy
* Addressed partially through normalization and filtering

---

### 🔴 5. Dataset Complexity

* UCLASS dataset contains **real-world imperfect speech**
* Includes:

  * Irregular pauses
  * Natural stuttering patterns
* Required tuning to handle realistic and noisy conditions

---

---
