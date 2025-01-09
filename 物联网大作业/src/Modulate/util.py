import struct
import wave
import numpy as np


args = {'framerate': 44100, 'frequency': 10000, 'sample_width': 2, 'nchannels': 1,
        'volume': 1.0, 'phase': 0, 'wave_length': 0.1, 'preamble': "10101010", "payload_length": 248,"file_name":"sound.wav"}


def intToByteStr(num):
    '''
    将输入int转化为byte编码格式的01string
    :param num:
    :return:
    '''
    pass



def byteStrToInt(s: str):
    '''
    byte编码格式的01string转化为int
    :param s:01字符串
    :return:解码原文
    '''
    pass


def strEncode(s: str):
    '''
    将明文字符串按照ASCII格式转化为01字符串
    :param s: 待编码字符串
    :param rule: 编码方案 默认utf-8
    :return: 字符串对应01字符串
    '''
    pass


def strDecode(s: str):
    '''
    将01字符串（不加任何标识符和纠错码）根据ASCII格式转化为对应的明文字符串
    :param s:01字符串
    :return:解码原文
    '''
    pass



def generateWave(framerate, frequency, volume, phase, wave_length):
    pass



def cut(obj, length):
    '''
    将obj切分成长为length的子片段
    :param obj:
    :param length:
    :return: 子片段的列表
    '''
    pass



def saveWaveAsFile(wav, args, filename="sound.wav"):
    '''
    将生成的波保存为wav文件
    :param wav:
    :param args:
    :param filename:
    :return:
    '''
    pass



def translateRawStringToContext(raw_string, args):
    '''
    将多个包的01序列转换为有语义的字符串
    :param raw_string:
    :param args:
    :return:
    '''
    pass

