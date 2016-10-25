# AUTHOR Alex Bennett gottbenn@bu.edu

import scipy.io.wavfile as wavfile
import time
import numpy as np
import math
import matplotlib.pyplot as pyplot




def loudest_band(music,frame_rate,bandwidth):

	#Take the fft of the music array and then shift it so the zero
	#frequency is in the center
	music_freq = np.fft.fftshift(np.fft.fft(music))
	freq_steps = frame_rate/len(music)
	#print(frame_rate,len(music),freq_steps)

	# pyplot.plot(music_freq)
	# pyplot.show()

	#find the zero frequency index
	f = np.arange(-frame_rate/2,frame_rate,freq_steps)
	freq_zero_index = np.absolute(f).argmin()

	#array I am doing my analysis on which is only the positive 
	#frequencies because it is conjugate symmetric 
	music_analysis = music_freq[freq_zero_index:]

	# pyplot.plot(music_analysis)
	# pyplot.show()

	# pyplot.plot(music_freq)
	# pyplot.show()

	#create arrays for the variety of values we need to output.
	low_freq = []
	high_freq = []

	#power of the signal
	signal = np.square(np.absolute(music_analysis))
	# pyplot.plot(signal)
	# pyplot.show()



	#bandwidth size in freq steps
	b_size = int(bandwidth/freq_steps)

	#print(b_size)

	#first filter 
	power = [sum(signal[0:b_size])]

	#get the difference between the music and the size of the bandwidth
	difference_between = len(music_analysis) - b_size


	for i in range(0,difference_between):
		# save the information of the different elements in these arrays. 
		# power += [sum(signal[i:i+b_size-1])]
		power += [power[i] + signal[i+b_size-1] - signal[i]]



	# pyplot.plot(power)
	# pyplot.show()


	max_index = np.argmax(power) 
	# print(max_index)
	
	if max_index != 0: 	
		#create the bandpass filter for the negative frequencies
		first_bp = np.append(np.ones(bandwidth+1),np.zeros(max_index-1))
		negative_bp = np.append(np.zeros(freq_zero_index - bandwidth - max_index), first_bp)

		#create the positive bandpass filter for the positive frequencies
		first_p_bp = np.append(np.zeros(max_index-1), np.ones(bandwidth+1))
		positive_bp = np.append(first_p_bp,np.zeros(freq_zero_index-bandwidth-max_index))
	else:
		#to handle the special case that the max index is zero
		negative_bp = np.append(np.zeros(freq_zero_index - bandwidth - max_index), np.ones(bandwidth))
		positive_bp = np.append(np.ones(bandwidth),np.zeros(freq_zero_index-bandwidth-max_index))

	#constrcut the final BP 
	final_bp = np.append(negative_bp,positive_bp)

	
	filt_music = np.multiply(music_freq,final_bp)
	time_music = np.fft.ifft(np.fft.ifftshift(filt_music))

	result = (max_index*freq_steps,(max_index+b_size)*freq_steps,time_music)
	# #print(result)

	return(result) 


def match(w,ref):
    "return the relative similarity of w and ref"
    #print(w)
    #print(ref)
    energy = (abs(ref)**2).sum()
    # print(energy)
    error = (abs(w-ref)**2).sum() 
    # print(error)
    return error/energy

def main():
	# frame_rate,T,ftest,bandwidth = 10000,1,100,10
	# t = np.linspace(0,T,T*frame_rate)
	# m = np.zeros_like(t)
	# for a,f in [(1,10),(1,11),(1,12),(2,30)]:
	# 	m += a*np.cos(2*np.pi*f*t)
	# low,high,filtered = loudest_band(m,frame_rate,bandwidth)

	# frame_rate,T,ftest,bandwidth = 1000,1,100,10
	# m = np.sin(2*np.pi*ftest * np.linspace(0,T,T*frame_rate))
	# low,high,filtered = loudest_band(m,frame_rate,bandwidth)



	# frame_rate,T,ftest,bandwidth = 10000,1,100,10
	# t = np.linspace(0,T,T*frame_rate)
	# m = np.sin(2*np.pi*ftest*t)+np.sin(2*np.pi*(ftest+0.8*bandwidth)*t)
	# low,high,filtered = loudest_band(m,frame_rate,bandwidth)

	frame_rate,T,ftest,bandwidth = 1000,1,100,20
	t = np.linspace(0,T,T*frame_rate)
	m = np.ones_like(t) + np.sin(2*np.pi*bandwidth//2)
	low,high,filtered = loudest_band(m,frame_rate,bandwidth)
	loudest_band(m,frame_rate,bandwidth)

	mat= match(filtered,m)
	print(low,high,mat)

if __name__=="__main__":
	main()
