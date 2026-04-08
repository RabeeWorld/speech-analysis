import numpy as np

def detect_pauses(rms, times, min_duration=0.3):
    threshold = np.mean(rms) * 0.5
    
    silent_segments = []
    start = None

    for i, energy in enumerate(rms):
        if energy < threshold:
            if start is None:
                start = times[i]
        else:
            if start is not None:
                end = times[i]
                if (end - start) >= min_duration:
                    silent_segments.append((start, end))
                start = None

    if start is not None:
        end = times[-1]
        if (end - start) >= min_duration:
            silent_segments.append((start, end))

    return silent_segments