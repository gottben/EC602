# AUTHOR Brian Appleton appleton@bu.edu
# AUTHOR Alex Bennett gottbenn@bu.edu
# AUTHOR Cathryn Callahan cathcal@bu.edu


import unittest
import sys

authors=['appleton@bu.edu', 'gottbenn@bu.edu', 'cathcal@bu.edu']

class PolynomialTestCase(unittest.TestCase):
    """unit testing for polynomials"""

    def setUp(self):
        self.x = Polynomial([1,2,3])
        self.z = Polynomial([0,0,1,2,3,0,0,5])
        self.y = Polynomial([-3,4 - 1j, 2, 5-2j])
        self.w = Polynomial([1.005,2.00000768,3.12345,4,0,0,12.576])
        test = self.z+self.w
        test = self.w+self.z
        test = self.z*self.w
        test = self.w*self.z
        test = self.z.eval(3)
        test = self.z-self.w
        test = self.w-self.z
        test = self.z.deriv()
        test = self.z[1500]
        test = self.z[2] + self.z[1]


    def test_get_coeff_zero(self):
        self.assertEqual(self.z[50000],0)

    def test_get_coeff_exist(self):
        self.assertEqual(self.z[4],2)

    def test_get_complex_coeff(self):
        self.assertEqual(self.y[2],4-1j)

    def test_set_value(self):
        #test if a Polynomial created using set value is equivalent to a Polynomial that used the constructor
        poly = Polynomial()
        for i in range(0,3):
            poly[i] = 3-i
        self.assertEqual(self.x,poly)

    def test_set_value_zero(self):
        #test if set value sets a value to zero
        self.x[0] = 0
        self.assertEqual(self.x[0],0)

    def test_modification(self):
        #test if the polynomial is modified because add, subtract, or multiply
        poly = Polynomial([0,0,1,2,3,0,0,5])
        self.assertEqual(self.z,poly)

    def test_poly_eval(self):
        #test if the evaluation function works
        self.assertEqual(self.x.eval(5),38)

    def test_addition(self):
        #test Polynomial addition
        self.assertEqual((self.x+self.w).eval(10),self.x.eval(10)+self.w.eval(10))

    def test_efficient_addition(self):
        #these Polynomials are not handling addition correctly 
        #as in the subtraction of these values should remove coefficients of zero
        poly = Polynomial([-1,-2,-3])
        poly2 = Polynomial()
        a = self.x + poly
        self.assertEqual(a,poly2)

    def test_subtraction(self):
        #test if polynomial properly subtracts
        self.assertEqual((self.x-self.w).eval(10),self.x.eval(10)-self.w.eval(10))

    def test_efficient_subtraction(self):
        #test efficient subtraction
        poly = Polynomial([1,2,3])
        a = self.x-poly
        self.assertEqual(a,Polynomial())

    def test_multiplication(self):
        #test if multiplication works
        self.assertEqual((self.x*self.w).eval(10),self.x.eval(10)*self.w.eval(10))


    def test_eq(self):
        #test to see if they handle equality
        poly = Polynomial([1,2,3])
        poly2 = Polynomial([5])
        poly2[3] = 3
        poly2[4] = 2
        poly2[5] = 1
        # self.assertEqual(self.x,poly)
        if self.x == poly:
            # self.assertEqual(1,1)
            if poly2 == self.z:
                self.assertEqual(1,1)
            else:
                self.assertEqual(1,0)
        else:
            self.assertEqual(1,0)
        Poly1    = Polynomial([10,9,8,7])
        Poly2 = Polynomial([11,10,9,8,7])
        self.assertNotEqual(Poly1, Poly2)
        self.assertNotEqual(Poly2,Poly1)
  
    def test_sparse(self):
        #test to see if they handle zeros
        n = 1000
        p = Polynomial([0]*n)
        q = Polynomial()
        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))

    def test_deriv(self):
        #test to see if they handle the basic derivative
        t = self.x.deriv()
        p = Polynomial([2,2])
        self.assertEqual(t,p)

    def test_negative_powers(self):
        #test to see if the class handles negative powers
        self.x[-1] = 2
        self.assertEqual(self.x.eval(10),123.2)

    def test_add_negative_powers(self):
        #add polynomials with negative powers
        self.x[-1] = 5
        self.x[-2] = 5
        self.z[-1] = 5
        a = self.z+self.x
        self.assertEqual(a.eval(10),123129.05)

    def test_init(self):
        #test to see if the polynomial was initialized correctly and if the 
        #correct number of input arguments were used
        self.assertIsInstance(self.x,Polynomial)

        try:
            Polynomial([],{})
            raise Exception('Error')
        except Exception as e:
            if str(e) == 'Error':
                raise Exception('Too many input arguments')

    def test_is_boolean(self):
        #check to see if the polynomial returns a boolean
        poly = Polynomial([])
        self.assertNotIsInstance(poly[1],bool)



    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()
