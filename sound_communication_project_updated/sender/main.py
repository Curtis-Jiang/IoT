
from modulator import text_to_bits, bits_to_wave, save_wave_to_file

def main():
    text = input("请输入要发送的文本：")
    bits = text_to_bits(text)
    wave = bits_to_wave(bits)
    save_wave_to_file(wave)

if __name__ == "__main__":
    main()
