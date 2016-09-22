# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu
# AUTHOR PreranaHaridoss preranah@bu.edu

# git repository https://github.com/gottben/EC602

import numpy

#Input the vectors
a = input()
b = input()

#convert to numbers 
float_a = numpy.fromstring(a,dtype=float, sep=' ')
float_b = numpy.fromstring(b,dtype=float, sep=' ')

#convolve

result = numpy.convolve(float_a,float_b)

result_string = ' '.join(str(x) for x in result)
print(result_string)
