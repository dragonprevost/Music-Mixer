

import librosa, librosa.display, numpy
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from pprint import pprint


# ratio is how much more the audio is. ratio = 2 -> double the length of the data
def rescale(data, ratio):
    return librosa.effects.time_stretch(data, 1 / ratio)

def convert_mp3_to_wav_mono(file_name):
    #Convert to mono and save
    # file_name ='if_i_were_a_boy.mp3'
    print("Converting", file_name)
    out_filename = file_name.replace('.mp3', "") + '.wav'
    y, sr = librosa.load(file_name, mono=False)
    y_mono = librosa.to_mono(y)
    librosa.output.write_wav(out_filename, y_mono, sr)

def resample_and_save(name):
    data, sr = librosa.load(name)
    data = librosa.resample(data, sr,44100)
    librosa.output.write_wav(name, data, 44100)


#start,end in frame
def slice_song_and_save(data, start, end, sr, name, idx=""):
    data = data[start:end]
    print(start, end, len(data),max(data))

    out_filename = name.replace(".wav", "") + "_" + str(idx) + ".wav"
    librosa.output.write_wav(out_filename, data, sr)


def slice_song(file_name):
    #slicing and save
    print("Slicing", file_name)
    start = 10
    duration = 150 + start
    out_filename = file_name.replace(".wav","") +  str(start) + "_" + str(duration) + '.wav'
    y, sr = librosa.load(file_name, mono=False)
    # print(len(y), len(y[:duration*sr]))
    y = y[start*sr: duration*sr]
    librosa.output.write_wav(out_filename, y, sr)

# convert_mp3_to_wav_mono("replay.mp3")
# slice_song("replay.wav")
# resample("just_a_dream_vocal_mono.wav")