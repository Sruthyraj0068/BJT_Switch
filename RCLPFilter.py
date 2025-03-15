import numpy as np
import matplotlib.pyplot as plt


def rc_lowpass_filter(frequency, R, C, t):
    
    fc = 1 / (2 * np.pi * R * C)
    H = 1 / (1 + 1j * frequency / fc)
    signal = np.sin(2 * np.pi * frequency * t)
    filtered_signal = np.abs(H) * signal
    return filtered_signal, fc

t = np.linspace(0, 1, 1000)
R = 1000  
C = 1e-6  
frequencies = [10, 100, 1000, 5000]  # in Hz


plt.figure(figsize=(9, 3))
for freq in frequencies:
    output_signal, cutoff = rc_lowpass_filter(freq, R, C, t)
    plt.plot(t, output_signal, label=f'{freq} Hz (f_c = {cutoff:.2f} Hz)')

plt.title('RC Low-Pass Filter Simulation')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
