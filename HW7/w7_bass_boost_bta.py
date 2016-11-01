# AUTHOR BrianAppleton appleton@bu.edu

import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np

def loudest_band(music,frame_rate,bandwidth):
	#returns a tuple(low,high,loudest)
	#low and high are frequencies with difference bandwidth, loudest is a filtered signal in the time domain	
	
	#Set up. f will contain the fft frequency data for fft_power
	Fs = frame_rate
	N  = len(music)
	f  = np.arange(-Fs/2, Fs/2, Fs/N) #0 Hz is at element N/2
	zero_Hz_index = np.absolute(f).argmin()

	#Take fft of input signal. Shift it so 0Hz is in the center. Set fft_power to the squared magnitude of fft.
	fft       = np.fft.fftshift(np.fft.fft(music))
	fft_power = np.square(np.absolute(fft))
	
	#Plot fft_power vs frequency	
	#plt.plot(f,fft_power)
	#plt.show()
	
	#Search for window in fft_power with largest average
	window_width = int(bandwidth/(Fs/N))
	max_sum   = 0
	max_sum_i = 0	
	for i in range(zero_Hz_index, N-window_width): #Loop over positive frequencies
		this_sum = np.sum(fft_power[i:i+window_width])
		if this_sum > max_sum:
			max_sum   = this_sum
			max_sum_i = i
			#print(i, ": ", max_sum, '; f = ', f[i])
	low_Hz  = (max_sum_i-zero_Hz_index)*Fs/N
	high_Hz = (max_sum_i-zero_Hz_index+window_width)*Fs/N
	
	
	#Create a first-order low-pass filter
	s   = 2*np.pi*f*1j
	tau = 3.183e-3 #50Hz fc
	H   = 1/(tau*s-1)
	
	
	#Plot window function versus frequency
	plt.plot(f,np.absolute(H))
	plt.show()
	
	#Apply window function to fft
	fft_filtered = fft*H

	#Plot filtered fft vs frequency
	#plt.plot(f,np.absolute(fft_filtered))
	#plt.show()	
			
	#Convert back to time domain
	loudest = np.real(np.fft.ifft(np.fft.ifftshift(fft_filtered)))

	#Plot time domain signal
	#plt.plot(loudest)
	#plt.show()
	
	
	return (low_Hz, high_Hz, loudest)


def read_wave(fname,debug=False):
	frame_rate,music = wavfile.read(fname)
	if music.ndim>1:
		nframes,nchannels = music.shape
	else:
		nchannels = 1
		nframes = music.shape[0]
	if debug:
		print(frame_rate,type(music),music.shape,nframes)
	return music,frame_rate,nframes,nchannels

def plot_fft(tone, Fs, fmin, fmax):
	'''
	Plot fft of a signal "tone", ndarray of shape (N,)
	Fs is sampling frequency
	Plot will be cenetered at zero frequency.
	'''
	fft = np.fft.fft(tone)
	N = len(tone)
	#the frequency axis of the shifted fft goes from -Fs/2 to Fs/2, in intervals of Fs/N
	#The point Fs/2 is excluded
	f = np.arange(-Fs/2, Fs/2, Fs/N)
	
	plt.plot(f,np.fft.fftshift(np.absolute(fft)))
	ax = plt.subplot(111)
	ax.set_xlim(xmin=fmin, xmax=fmax)
	plt.xlabel('Frequency, Hz')
	plt.ylabel('|X|')
	plt.show()

def main():
	
	#Select filename
	filename = 'scary.wav'	

	#Test loudest_band with bach, send only one of the two channels	
	music, frame_rate, nframes, nchannels = read_wave(filename, False)

	#Plot FFT of input signal
	plot_fft(music[:,0], frame_rate, -5000, 5000)	

	(low, high, loudest) = loudest_band(music[:,0], frame_rate, 1000)

	print("low:  ", low,  " Hz")
	print("high: ", high, " Hz")	
	
	#Plot FFT of output signal
	plot_fft(loudest, frame_rate, -5000, 5000)
	
	#Write file
	loudest = loudest/np.max(loudest) #normalize to amplidue one
	loudest = loudest.astype(np.float32) #convert to 32-bit float
	wavfile.write(filename[0:-4]+'_filtered.wav', frame_rate, loudest)
	
if __name__ == '__main__':
	main()
