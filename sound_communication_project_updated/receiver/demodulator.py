
import numpy as np
from scipy.io import wavfile

def load_wave_from_file(filename="output.wav"):
    sample_rate, data = wavfile.read(filename)
    return data

def wave_to_bits(wave, threshold=0.5, duration=0.1):
    sample_rate = 44100
    samples_per_bit = int(sample_rate * duration)
    bits = []

    for i in range(0, len(wave), samples_per_bit):
        segment = wave[i:i+samples_per_bit]
        if np.abs(segment).mean() > threshold:
            bits.append('1')
        else:
            bits.append('0')

    return ''.join(bits)

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
