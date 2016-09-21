#include <iostream>
#include <cmath>
using namespace std;

#include "w3b_bigint.cpp"




int main() {
	//test program

	string b = "5";
	string a = "-5";

	//test addition
	//cout << "c(x) = a(x) + b(x): " << endl;
	string d = multiply_int(a,b);
	cout << d << endl;
	//print_poly(c,'c');
	//cout << "c(10) = " << evaluate_poly(c,10) << endl;

	//test multiplication
	//cout << "d(x) = a(x) * b(x): " << endl;
	//Poly d = multiply_poly(a,b);
	//print_poly(d,'d');
	//cout << "d(10) = " << evaluate_poly(d,10) << endl;

	return 0;
}


