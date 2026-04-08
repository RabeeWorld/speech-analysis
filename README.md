# 🎙️ Speech Analysis: Pause & Repetition Detection

## 📌 Overview

This project analyzes a speech audio file to detect:

* ⏸️ **Pause Segments** — Silent regions in speech
* 🔁 **Repetitions** — Stuttered patterns such as *"ba-ba-ball"* or *"I-I-I want"*

The goal is to design a clear and explainable pipeline using signal processing techniques rather than focusing on perfect accuracy.

---

## 🧠 Approach

The system follows a modular pipeline:

```
Audio → Preprocessing → Feature Extraction → Detection → Output + Visualization
```

---

## 📂 Project Structure

```
speech-analysis/
│
├── data/                  # Input audio files
├── src/                   # Source code
│   ├── preprocess.py
│   ├── features.py
│   ├── pause_detection.py
│   ├── repetition_detection.py
│   ├── visualization.py
│   └── main.py
│
├── plots/                 # Generated graphs
├── results/               # Output files
├── requirements.txt
└── README.md
```

---

## ⚙️ Audio Preprocessing

* Audio is loaded using `librosa`
* Normalization is applied to ensure consistent amplitude levels

This improves:

* Feature extraction reliability
* Threshold-based detection accuracy

---

## 🎧 Feature Extraction

### 🔹 Pause Detection

* Uses **RMS Energy (Root Mean Square)**
* Represents loudness over time
* Low RMS → silence

---

### 🔹 Repetition Detection

* Uses **MFCC (Mel-Frequency Cepstral Coefficients)**
* Derived from spectrogram
* Captures speech characteristics effectively

---

## ⏸️ Pause Detection Logic

1. Compute RMS energy for audio frames
2. Apply dynamic threshold:

   ```
   threshold = mean(RMS) × factor
   ```
3. Identify low-energy regions as silence
4. Group consecutive silent frames
5. Filter short pauses using minimum duration

### ✅ Output:

* Start & end time of pauses
* Total pause duration

---

## 🔁 Repetition Detection Logic

### 🔹 1. Segmentation

* Audio is split into small overlapping segments

---

### 🔹 2. Feature Extraction

* MFCC features extracted for each segment

---

### 🔹 3. Similarity Comparison

* Cosine similarity used:

  ```
  similarity = 1 - cosine distance
  ```
* High similarity → repetition

---

### 🔹 4. Segment Merging

* Overlapping detections are merged
* Prevents duplicate results

---

### 🔹 5. Speech-to-Text Enhancement

* Converts audio to text using Google Speech API
* Helps identify repetition patterns like:

  * "I-I-I want"
  * "ba-ba-ball"

---

### 🔹 6. Pattern Detection

* Detects consecutive repeated words
* Generates pattern + repetition count

---

## 📊 Visualization

* Waveform plotted using `matplotlib`
* Pause regions highlighted
* Saved as:

```
plots/waveform.png
```

---

## 📦 Example Output

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

## 🧪 Requirements

Install dependencies:

```
pip install -r requirements.txt
```

---

## ⚠️ Challenges Faced

### 🔴 1. Speech Recognition Limitations

* Struggles with stuttering like "b-b-b-ball"
* May return incorrect text

---

### 🔴 2. Stuttering vs Clean Repetition

* Irregular and fragmented patterns
* Required smaller segments and tuning

---

### 🔴 3. Threshold Sensitivity

* High → missed detections
* Low → false positives

---

### 🔴 4. Noise & Audio Quality

* Background noise affects MFCC
* Poor recordings reduce accuracy

---

### 🔴 5. Dataset Complexity

* Real-world imperfect speech (UCLASS dataset)
* Required tuning for realistic behavior


--
