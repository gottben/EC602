#include <iostream>
#include <cmath>
using namespace std;

#include "w3a_polyops.cpp"

void print_poly(Poly &a, char func);
double evaluate_poly(Poly &a, int x);

int main() {
	//test program
	
	//polynomials used for testing
	//zero-based index is the exponent for the term; the contents of the array at the respective index is the coefficient
	Poly a = {1,2,3};
	Poly b = {4,5,6,1,0};

	//print polynomials	
	print_poly(a,'a');
	cout << "a(10) = " << evaluate_poly(a,10) << endl;
	print_poly(b,'b');
	cout << "b(10) = " << evaluate_poly(b,10) << endl;

	//test addition
	cout << "c(x) = a(x) + b(x): " << endl;
	Poly c = add_poly(a,b);
	print_poly(c,'c');
	cout << "c(10) = " << evaluate_poly(c,10) << endl;

	//test multiplication
	cout << "d(x) = a(x) * b(x): " << endl;
	Poly d = multiply_poly(a,b);
	print_poly(d,'d');
	cout << "d(10) = " << evaluate_poly(d,10) << endl;

	return 0;
}

void print_poly(Poly &a, char func) {
	cout << func <<"(x) = ";
	for (int i=a.size()-1; i>0; i--) {
		cout << a[i] << "x^" << i << " + ";	
	}
	cout << a[0] << "x^" << "0" << endl;
}

double evaluate_poly(Poly &a, int x) {
	double result = 0;	
	for (int i = 0; i<a.size(); i++) {
		result += a[i]*pow(x,i);
	}
	return result;
}


