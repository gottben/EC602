# AUTHOR Cathryn Callahan cathcal@bu.edu
#
# Part A: Telephone Dialer
# Write a python function dialer which creates a WAV file of the sound of a telephone 
#	number being dialed

import scipy.io.wavfile as wavfile
import PyQt4.QtGui as qt
import time
import matplotlib.pyplot as pyplot
import numpy as np



def dialer(file_name,frame_rate,phone,tone_time):
	#file_name is a str rep. the name of the WAV file to be created
	#frame_rate is a number representing the number of samples per second to use in the sound
	#phone is a string of digits representing a phone number to dial
	#tone_time is a number representing the time in secons of each tone to generate
	wave = 0
	#wavfile.write('signal.wav', frame_rate, wave)
	
	# create dictionary of DTMF keypad frquencies
	key_tones = {'1':[697,1209], '2':[697,1336], '3':[697,1477], 'A':[697,1633],
		'4':[770,1209], '5':[770,1336], '6':[770,1477],'B':[770,1633], '7':[852,1209], 
		'8':[852,1336], '9':[852,1477], 'C':[852,1633],'*':[941,1209], '0':[941,1336], 
		'#':[941,1477], 'D':[941,1633]}
	#get number of samples, t, for the given tone_time and frame_rate
	t_samples = tone_time*frame_rate;

	for i in phone:
		f = key_tones[i]
		print (f[0], f[1])

		#for j in range(0,t_samples):
		t = np.linspace(0,tone_time,t_samples)
		tone = np.cos(2*np.pi*f[0]*t) + np.cos(2*np.pi*f[1]*t)
		wave = np.append(wave,tone)
			

	wavfile.write('signal.wav',frame_rate, wave)
	pyplot.plot(wave)
	pyplot.show()

	#wavfile.read('signal.wav')
	#qt.QSound.play('signal.wav')
	

	#frame_rate, t_samples = read_wave('signal.wav')
	# time.sleep(t_samples/frame_rate)


#def wavplay(file_name):
#	qt.QSound.play(file_name)
#	music, frame_rate, t_samples = read_wave(file_name)
#	time.sleep(t_samples/frame_rate)	#sleep while music is playing


def main():
	dialer('file',44100,'8675309',1)
	#wavplay('file')



if __name__=="__main__":
	main()
