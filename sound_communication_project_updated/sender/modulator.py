
import numpy as np

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_wave(bits, duration=0.1, frequency=1000):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    modulated_wave = np.array([])

    for bit in bits:
        if bit == '1':
            modulated_wave = np.concatenate([modulated_wave, wave])
        else:
            modulated_wave = np.concatenate([modulated_wave, np.zeros(len(wave))])

    return modulated_wave

def save_wave_to_file(wave, filename="output.wav"):
    from scipy.io.wavfile import write
    sample_rate = 44100
    write(filename, sample_rate, wave.astype(np.float32))
