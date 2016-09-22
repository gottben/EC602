# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu
# AUTHOR PreranaHaridoss preranah@bu.edu

# git repository https://github.com/gottben/EC602


import numpy
import sys




#Create a float array from the input
X = numpy.fromstring(input(), dtype=float, sep=' ')
H = numpy.fromstring(input(), dtype=float, sep=' ')

#print the convolution of the two inputs
print(" ".join(map(str,numpy.convolve(X,H))))


