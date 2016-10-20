import scipy.io.wavfile as wavfile
import PyQt4.QtGui as qt
import time
import numpy
import matplotlib.pyplot as pyplot

def read_wave(fname,debug=False):
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels

def wavplay(fname):
    qt.QSound.play(fname)
    music,frame_rate,nframes,nchannels = read_wave(fname)
    time.sleep(nframes/frame_rate)


fname = "bach10sec.wav"

music,frame_rate,nframes,nchannels = read_wave(fname)


wavplay('bach10sec.wav')
if nchannels > 1:
    music = music.sum(axis=1)

pyplot.plot(music)
pyplot.show()

