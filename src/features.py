import librosa

def compute_rms(y):
    return librosa.feature.rms(y=y)[0]