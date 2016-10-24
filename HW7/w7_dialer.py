# AUTHOR Alex Bennett gottbenn@bu.edu


import scipy.io.wavfile as wavfile
#import PyQt4.QtGui as qt
import time
import numpy as np
import math
#import matplotlib.pyplot as pyplot

def dialer(file_name,frame_rate,phone,tone_time):

	dial_tones = {'1':[697,1209],'2':[697,1336],'3':[697,1477],'A':[697,1633],'4':[770,1209],'5':[770,1336],'6':[770,1477],'B':[770,1633],'7':[852,1209],'8':[852,1336],'9':[852,1477],'C':[852,1633],'*':[941,1209],'0':[941,1336],'#':[941,1477],'D':[941,1633]}
	total_samples = tone_time*frame_rate
	tones = []

	for c in phone:
		freq = dial_tones[c]
		for i in range(0,total_samples):
			sound = np.cos(2*np.pi*(i/frame_rate)*freq[0]) + np.cos(2*np.pi*(i/frame_rate)*freq[1])
			tones += [sound]

	tone = np.array(tones)
	print(tone)
	wavfile.write(file_name,frame_rate,tone)
