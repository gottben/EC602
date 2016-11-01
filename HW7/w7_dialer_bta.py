# AUTHOR BrianAppleton	appleton@bu.edu

import numpy as np
import scipy.io.wavfile as wav

def dialer(file_name, frame_rate, phone, tone_time):
	#file_name --> file_name.wav
	#frame_rate --> number of samples per second
	#phone --> string of phone number
	#tone_time --> length in seconds of each tone
	
	#Create a 1D numpy array for the time axis
	#stop_time = len(phone)*tone_time
	t = np.linspace(0, tone_time, tone_time*frame_rate, dtype='float32') 

	#Tones
	tones = {
		'1': [697,1209],
		'2': [697,1336],
		'3': [697,1477],
		'4': [770,1209],
		'5': [770,1336],
		'6': [770,1477],
		'7': [852,1209],
		'8': [852,1336],
		'9': [852,1477],
		'0': [941,1336]	
		}

	dial_signal = np.array([], dtype='float32');

	for tone in phone:
		f = tones[tone]
		tone_signal = (np.cos(2*np.pi*f[0]*t) + np.cos(2*np.pi*f[1]*t))/2
		dial_signal=np.append(dial_signal,tone_signal)
	

	#Write the wav file	
	wav.write(file_name, frame_rate, dial_signal)


def main():
	dialer('dial_signal.wav', 5000, '6108675309', 0.1)

if __name__ == '__main__':
	main()
	
