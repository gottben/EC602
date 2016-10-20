# AUTHOR Alex Bennett gottbenn@bu.edu



import unittest
import sys
import numpy as np
import random



authors=['gottbenn@bu.edu']

class DFTTestCase(unittest.TestCase):
    """unit testing for DFTTestCase"""

    def setUp(self):
        self.w = 'Whooo'
        self.l = {1:2,3:4,4:'key'}
        self.x = [1,2,3,4,5]
        self.b = bytearray([1,2,3,4,5,6,7])
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
        DFT(self.b)


    def test_np_fft_fft(self):
        for i in range(2,20):
            for j in range(0,10):
                a = []
                for k in range(0,i):
                    a += [(random.random() -0.5)*2 + 1j*(random.random() -0.5)*2]
                np.testing.assert_array_almost_equal(DFT(a),np.fft.fft(a))


    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    from w6_dft import DFT
    unittest.main()