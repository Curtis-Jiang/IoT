
from demodulator import load_wave_from_file, wave_to_bits, bits_to_text

def main():
    wave = load_wave_from_file()
    bits = wave_to_bits(wave)
    text = bits_to_text(bits)
    print("接收到的文本:", text)

if __name__ == "__main__":
    main()
