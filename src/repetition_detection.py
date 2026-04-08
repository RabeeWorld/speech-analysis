import librosa
import numpy as np
from scipy.spatial.distance import cosine
import speech_recognition as sr


# 🔹 MFCC extraction
def extract_mfcc(segment, sr):
    mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)


# 🔹 Detect repetition (IMPROVED for short stuttering)
def detect_repetitions(y, sr, segment_duration=0.1, step_duration=0.05, threshold=0.75):

    segment_length = int(segment_duration * sr)
    step = int(step_duration * sr)

    segments = []

    for i in range(0, len(y) - segment_length, step):
        segments.append(y[i:i + segment_length])

    repetitions = []

    for i in range(len(segments) - 1):
        mfcc1 = extract_mfcc(segments[i], sr)
        mfcc2 = extract_mfcc(segments[i + 1], sr)

        sim = 1 - cosine(mfcc1, mfcc2)

        # DEBUG (optional)
        # print(sim)

        if sim > threshold:
            start = i * step / sr
            end = (i + 1) * step / sr + segment_duration
            repetitions.append((start, end))

    return repetitions


# 🔹 Merge overlapping repetition segments
def merge_segments(segments):
    if not segments:
        return []

    segments.sort()
    merged = [segments[0]]

    for current in segments[1:]:
        prev = merged[-1]

        if current[0] <= prev[1]:
            merged[-1] = (prev[0], max(prev[1], current[1]))
        else:
            merged.append(current)

    return merged


# 🔹 Speech-to-text (SAFE VERSION)
def speech_to_text(audio_file):
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return ""
    except sr.RequestError:
        print("⚠️ API error")
        return ""


# 🔹 Detect repetition pattern (FIXED LOGIC)
def detect_text_pattern(text):
    words = text.split()

    if not words:
        return None, 0

    i = 0

    while i < len(words) - 1:
        count = 1

        # count consecutive repeats
        while i + 1 < len(words) and words[i] == words[i + 1]:
            count += 1
            i += 1

        if count > 1:
            # build pattern like ba-ba-ball
            if i + 1 < len(words):
                pattern_list = [words[i]] * count + [words[i + 1]]
            else:
                pattern_list = [words[i]] * count

            pattern = "-".join(pattern_list)

            return pattern, count - 1

        i += 1

    return None, 0



# import librosa
# import numpy as np
# from scipy.spatial.distance import cosine
# import speech_recognition as sr


# # 🔹 MFCC extraction
# def extract_mfcc(segment, sr):
#     mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)
#     return np.mean(mfcc, axis=1)


# # 🔹 Detect repetition (sound level)
# def detect_repetitions(y, sr, segment_duration=0.3, step_duration=0.15, threshold=0.9):

#     segment_length = int(segment_duration * sr)
#     step = int(step_duration * sr)

#     segments = []

#     for i in range(0, len(y) - segment_length, step):
#         segments.append(y[i:i + segment_length])

#     repetitions = []

#     for i in range(len(segments) - 1):
#         mfcc1 = extract_mfcc(segments[i], sr)
#         mfcc2 = extract_mfcc(segments[i + 1], sr)

#         sim = 1 - cosine(mfcc1, mfcc2)

#         if sim > threshold:
#             start = i * step / sr
#             end = (i + 1) * step / sr + segment_duration
#             repetitions.append((start, end))

#     return repetitions


# # 🔹 Merge overlapping repetition segments
# def merge_segments(segments):
#     if not segments:
#         return []

#     segments.sort()
#     merged = [segments[0]]

#     for current in segments[1:]:
#         prev = merged[-1]

#         if current[0] <= prev[1]:
#             merged[-1] = (prev[0], max(prev[1], current[1]))
#         else:
#             merged.append(current)

#     return merged


# # 🔹 Speech-to-text
# def speech_to_text(audio_file):
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = r.record(source)
#     return r.recognize_google(audio)


# # 🔹 Detect repetition pattern from text
# def detect_text_pattern(text):
#     words = text.split()

#     repeated_words = []
#     count = 0

#     i = 0
#     while i < len(words) - 1:
#         if words[i] == words[i + 1]:
#             repeated_words.append(words[i])
#             count += 1
#         i += 1

#     # If no repetition
#     if count == 0:
#         return None, 0

#     # Build pattern like ba-ba-ball
#     pattern = "-".join(repeated_words + [words[i]])

#     return pattern, count