"""
Example of using unittest to test a class. 
The class begin tested is Complex
"""
import unittest

class PolynomialTestCase(unittest.TestCase):
    """unit testing for polynomials"""

    def setUp(self):
        self.z = Polynomial([0,0,1,2,3,0,0,5])
        self.y = Polnomial([-3,4 - 1j, 2, 5-2j])
        self.w = Polynomial([1.005,2.00000768,3.12345,4,0,0,12.576])

    def test_init(self):
        self.assertIsInstance(self.z,Polynomial)

    def test_get_coeff_zero(self):
        self.assertEqual(self.z[1],0)

    def test_get_coeff_exist(self):
        self.assertEqual(self.z[4],2)

    def test_get_complex_coeff(self):
        self.assertEqual(self.y[2],4-1j)

    def test_set_value(self):
        self.z[1] = 4
        self.assertEqual(self.z[1],4)


    def test_eval_eq(self):
        z = Polynomial([1,2,3])
        w = 50
        self.assertEqual(z.eval(5),w)

    def test_poly_eq(self):
        z = Polynomial([1,2,3,0,0,0,5])
        w = Polynomial([0,0,1,2,3,0,0,0,5])
        self.assertEqual(z,w)


    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()