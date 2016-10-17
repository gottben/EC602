# AUTHOR Alex Bennett gottbenn@bu.edu



import unittest
import sys
import numpy as np
import random



authors=['gottbenn@bu.edu']

class DFTTestCase(unittest.TestCase):
    """unit testing for polynomials"""

    def setUp(self):
        self.w = 'abc'
        self.l = {1:2,3:4}
        self.x = [1,2,3,4,5]
        self.y = [1-1j, 2-2j, 3-3j, 4-4j]
        self.z = ['1', 'apple', 1, 2 ,3, 'orange']



    def test_type_and_shape(self):
        a = DFT(self.x)
        b = np.array(self.x)
        c = np.array([1-1j,2-2j,3-3j,4-4j,5-5j])
        if (a.dtype != c.dtype) & (a.shape != b.shape):
            self.assertEqual(1,0)
        else: 
            self.assertEqual(1,1)



    def test_value_error(self):
        self.assertRaises(ValueError,DFT,self.z)
        self.assertRaises(ValueError,DFT,self.l)
        self.assertRaises(ValueError,DFT,self.w)


    def test_np_fft_fft(self):
        a = [0.4-0.5j]
        for i in range(0,19):
            if i%2 == 0:
                a += [random.random() - 1j*random.random()]
            else:
                a += [-random.random() + 1j*random.random()]
            self.assertEqual(DFT(a).all(),np.fft.fft(a).all())


    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()