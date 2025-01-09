import numpy as np

from util import strEncode, cut, generateWave, saveWaveAsFile, args, byteStrToInt, \
    intToByteStr


def input2Packets(input, preamble, payload_length):
    '''
    将输入串转化为若干个包的列表
    :param input: 输入串 str
    :preamble: 前导码
    :return: 包的列表，包已转化为0-1编码 list

    Bluetooth: 前导码（8bit）、有效载荷长度（8bit）、有效载荷（0bit，248bit]
    协议规定小于256，因为是按字节转化，我觉得没必要把最后一个字节拆分放到两个包中
    '''




def modulate(packet_list, args):
    '''
    调制信号
    :param packet_list:
    :return: 调制后的信号列表，对应于packet_list list[np.array]
    '''


def processInput(input_str):
    '''
    处理输入
    :param input_str:
    :return:
    '''


