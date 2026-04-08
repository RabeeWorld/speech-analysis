import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_waveform_with_pauses(y, sr, silent_segments, save_path="../plots/waveform.png"):
    
    # Time axis for waveform
    wave_times = np.linspace(0, len(y)/sr, num=len(y))

    plt.figure(figsize=(12, 4))
    
    # Plot waveform
    plt.plot(wave_times, y, label="Waveform")

 # Highlight pauses (only first one gets label)
    for i, (s, e) in enumerate(silent_segments):
        label = "Pause" if i == 0 else None
        plt.axvspan(s, e, alpha=0.3, label=label)

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Waveform with Pause Detection")
    plt.legend()

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    print(f"Graph saved at: {save_path}")