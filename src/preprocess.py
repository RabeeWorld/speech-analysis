import librosa

def load_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

def normalize_audio(y):
    return librosa.util.normalize(y)