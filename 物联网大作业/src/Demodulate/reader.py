import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

ascii_dict = {
    '00000000': '',
    '00001010': '\n',
    '00100000': ' ',
    '00100001': '!',
    '00100010': '"',
    '00100011': '#',
    '00100100': '$',
    '00100101': '%',
    '00100110': '&',
    '00100111': '\'',
    '00101000': '(',
    '00101001': ')',
    '00101010': '*',
    '00101011': '+',
    '00101100': ',',
    '00101101': '-',
    '00101110': '.',
    '00101111': '/',
    '00110000': '0',
    '00110001': '1',
    '00110010': '2',
    '00110011': '3',
    '00110100': '4',
    '00110101': '5',
    '00110110': '6',
    '00110111': '7',
    '00111000': '8',
    '00111001': '9',
    '00111010': ':',
    '00111011': ';',
    '00111100': '<',
    '00111101': '=',
    '00111110': '>',
    '00111111': '?',
    '01000000': '@',
    '01000001': 'A',
    '01000010': 'B',
    '01000011': 'C',
    '01000100': 'D',
    '01000101': 'E',
    '01000110': 'F',
    '01000111': 'G',
    '01001000': 'H',
    '01001001': 'I',
    '01001010': 'J',
    '01001011': 'K',
    '01001100': 'L',
    '01001101': 'M',
    '01001110': 'N',
    '01001111': 'O',
    '01010000': 'P',
    '01010001': 'Q',
    '01010010': 'R',
    '01010011': 'S',
    '01010100': 'T',
    '01010101': 'U',
    '01010110': 'V',
    '01010111': 'W',
    '01011000': 'X',
    '01011001': 'Y',
    '01011010': 'Z',
    '01011011': '[',
    '01011100': '\\',
    '01011101': ']',
    '01011110': '^',
    '01011111': '_',
    '01100000': '`',
    '01100001': 'a',
    '01100010': 'b',
    '01100011': 'c',
    '01100100': 'd',
    '01100101': 'e',
    '01100110': 'f',
    '01100111': 'g',
    '01101000': 'h',
    '01101001': 'i',
    '01101010': 'j',
    '01101011': 'k',
    '01101100': 'l',
    '01101101': 'm',
    '01101110': 'n',
    '01101111': 'o',
    '01110000': 'p',
    '01110001': 'q',
    '01110010': 'r',
    '01110011': 's',
    '01110100': 't',
    '01110101': 'u',
    '01110110': 'v',
    '01110111': 'w',
    '01111000': 'x',
    '01111001': 'y',
    '01111010': 'z',
    '01111011': '{',
    '01111100': '|',
    '01111101': '}',
    '01111110': '~',
    '01111111': 'DEL'
}

PATH = 'output.wav'
FREQUENCY_0 = 5000
FREQUENCY_1 = 10000
BIT_LENGTH = 0.1
WAYS = "lowpass"
0

def read_wave(path):
    # read file and show in plt
    framerate, wave_data = wavfile.read(path)

    # wf = wave.open(path, 'rb')
    # params = wf.getparams()
    # nchannels, sampwidth, framerate, nframes = params[:4]
    # t = int(nframes / framerate)
    # str_data = wf.readframes(nframes)
    # wf.close()
    # wave_data = np.fromstring(str_data, dtype=np.short)
    # plt.title('wave_data')
    # plt.plot(wave_data)
    # plt.show()
    # noise = noise_gen(0, wave_data)
    # wave_data = wave_data + noise

    # start decode
    strings = decode_1(wave_data, framerate)

    print("answer: ", strings)
    return strings


def decode_1(data, framerate):
    """
        decode the wave data, using modified 0 pass method
    :param data: sound file read in read_wave function
    :param framerate: framerate of the sound file
    :return: translated string
    """
    ans = ""

    # filter by the frequency

    # normalize the data

    # plt.title('data_0')
    # plt.plot(data_0)
    # plt.show()
    # plt.title('data_1')
    # plt.plot(data_1)
    # plt.show()

    # get data's cover

    # plt.title('rapped data_0')
    # plt.plot(amplitude_envelope_0)
    # plt.show()
    # plt.title('rapped data_1')
    # plt.plot(amplitude_envelope_1)
    # plt.show()

    # filter noise
    # 8表示滤波器的阶数

    # plt.title('filtered_data_0')
    # plt.plot(filtered_data_0)
    # plt.show()

    # plt.title('filtered_data_1')
    # plt.plot(filtered_data_1)
    # plt.show()

    # get answer wave to be sampled

    # plt.title('ans_wave')
    # plt.plot(ans_wave)
    # plt.show()

    # sample ans_wave to decode

    # write to file

    # print(len(ans_wave) / framerate / BIT_LENGTH)
    # print(len(ans))



def decode_2(data, framerate):
    """
        decode the wave data, using chopping wave to each bit method, similar to decode_1
    :param data: sound file read in read_wave function
    :param framerate: framerate of the sound file
    :return:
    """
    ans = ""
    # filter by frequency

    # normalize the data

    # plt.title('data_0')
    # plt.plot(data_0)
    # plt.show()
    # plt.title('data_1')
    # plt.plot(data_1)
    # plt.show()

    # get data's cover

    # plt.title('rapped data_0')
    # plt.plot(amplitude_envelope_0)
    # plt.show()
    # plt.title('rapped data_1')
    # plt.plot(amplitude_envelope_1)
    # plt.show()

    # filter noise

    # plt.title('filtered_data_0')
    # plt.plot(filtered_data_0)
    # plt.show()

    # plt.title('filtered_data_1')
    # plt.plot(filtered_data_1)
    # plt.show()

    # get answer wave to be sampled

    # plt.title('ans_wave')
    # plt.plot(ans_wave)
    # plt.show()

    # chop ans_wave to each bit to decode

    # print(len(ans_wave) / framerate / BIT_LENGTH)
    # print(len(ans))



def lowpass(wav, framerate, l_bound):



def highpass(wav, framerate, u_bound):


def bandpass(wav, framerate, l_bound, u_bound):


def noise_gen(SNR: int, wav):



def get_translate_rate(raw_string, start, length, end):
    """
    test how many ascii characters can be translated correctly in the raw string from start to end
    :param raw_string: the raw string to be tested in 0s and 1s
    :return: rate of correct translation
    """

    # print("try rate: ", able_num / total_asc)


def translate(raw_string):
    """
    translate the raw string to ascii string
    :param raw_string: the raw string to be translated in 0s and 1s
    :return: translated ascii string
    """

        # if preamble error

                # print()

            # print()

        # preamble is right

        # judge whether package length is right

        # if package length is wrong

            # whether there is "10101010" near the next package start

                # decode first, let the next package handle this in previous code

        # if package length is right or is last package


        # start decoding payload

                # if payload is wrong

                        # print("wrong")

                        # print("missing")

                            # print("extra")

                            # print("extra and wrong")

                            # print("unknown")

                    # print()

                # if payload is right

                    # continue decoding



def validate(ans_string, standard_string):
    """
    for test. get right bit rate
    :param ans_string:
    :param standard_string:
    :return:
    """

                # error

                # extra

                # missing

    # with open("judge.txt", "a") as f:
    #     f.write(altered_string + "\n")
    #     f.close()
    # print(util.translateRawStringToContext(altered_string, util.args))



def ascii_validate(str_send, str_receive):
    """
    for test. get right ascii character rate
    :param str_send:
    :param str_receive:
    :return:
    """



if __name__ == '__main__':
    """
    for test
    """
    read_wave(PATH)

    with open("judge.txt", "r") as f:
        standard_string = f.readline()
        ans_string = f.readline()
        f.close()
    rate = validate(ans_string, standard_string)
    print("right rate: ", rate)

    # with open("string.txt", "r") as f:
    #     standard = f.readline()
    #     ans = f.readline()
    #     f.close()
    # rate = ascii_validate(ans, standard)
    # print("ascii right rate: ", rate)

    # my_string = translate(
    #     "101010111110000110100001100110110100001100110011100010011000101100100001100010111000101100010011010010011100101101111011110010011001101100111011101010111000100110011011101110110011101101000011010100110011001101011001101010011011000110111011110100110011101100110101010101111100001100111011010100011010001100101001101010011011001110101011110010111010000110111001110000110100101110010011100100111010001100100011001100110011101100110011000110110011101110010011101000111011100110100001101010011011000110111001101000011010100110100101010100010100000110111001110000111100101110101011001110"
    # )
    # print(my_string)
