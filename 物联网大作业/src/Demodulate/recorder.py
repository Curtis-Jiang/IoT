import pyaudio
import wave
import audioop
import time


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
AUDIO_MIN_RMS = 50
STOP_THRESHOLD = 100

frames = []
detect_time = 0

# total process steps:
# 1. detect the start of the signal
# 2. save the recorded wave
# 3. translate to 0s and 1s


def callback(in_data, frame_count, time_info, status):

    # record when sound is larger than a threshold

        detect_time = 0



def save_record():
    """
        record the wave file and save it, wait to analyze, using no-blocking mode
        :return: None
    """


