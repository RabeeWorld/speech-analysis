import librosa
from preprocess import load_audio, normalize_audio
from features import compute_rms
from pause_detection import detect_pauses
from visualization import plot_waveform_with_pauses

from repetition_detection import (
    detect_repetitions,
    merge_segments,
    speech_to_text,
    detect_text_pattern
)


file_path = "../data/M_0030_16y4m_1.wav"

y, sr = load_audio(file_path)
y = normalize_audio(y)

rms = compute_rms(y)
times = librosa.frames_to_time(range(len(rms)), sr=sr)

pauses = detect_pauses(rms, times)

total = 0
print("Pause Segments:")
for s, e in pauses:
    duration = e - s
    total += duration
    print(f"[{s:.2f}s - {e:.2f}s]")

print(f"\nTotal Pause Duration: {total:.2f}s")

# -----------------------------
reps = detect_repetitions(y, sr)
merged_reps = merge_segments(reps)

# Convert speech to text
text = speech_to_text(file_path)

# Detect repetition pattern
pattern, count = detect_text_pattern(text)


if count == 0:
    print("\nRepetitions:")
    print("No repetition detected")
else:
    print("\nRepetitions:")
    print(f'Detected pattern: "{pattern}"')
    print(f"Repetition Count: {count}")
# -----------------------------

# ✅ Generate graph
plot_waveform_with_pauses(y, sr, pauses)