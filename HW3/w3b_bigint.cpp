// AUTHOR BrianAppleton appleton@bu.edu
// AUTHOR AlexBennett gottbenn@bu.edu
// AUTHOR CathrynCallahan cathcal@bu.edu
// AUTHOR PreranaHaridoss preranah@bu.edu

// git repository https://github.com/gottben/EC602

#include<vector>
#include<string>
#include "w3a_polyops.cpp"
#include <sstream>
typedef string BigInt;
typedef vector<double> Poly;
unsigned long evaluate_poly(Poly &a, int x);
BigInt multiply_int(const BigInt &a,const BigInt &b);
Poly convertoPoly(const BigInt &x);

BigInt multiply_int(const BigInt &a,const BigInt &b) {

	Poly number_a;
	Poly number_b;	
	number_a = convertoPoly(a);
	number_b = convertoPoly(b);
	Poly multiplied_number = multiply_poly(number_a,number_b);
	unsigned long number = evaluate_poly(multiplied_number,10);
	//cout << number << endl;
	BigInt result;
	stringstream convert;
	convert << number;
	result = convert.str();
	return result;
	
}

Poly convertoPoly(const BigInt &x){

	Poly number_x(x.length(),0);

	for(int i=0;i<x.length();i++){
                number_x[i] = x[i] - '0';
        }
	return number_x;
	
}

unsigned long evaluate_poly(Poly &a, int x) {
        double result = 0;
        for (int i = 0; i<a.size(); i++) {
                result += a[i]*pow(x,i);
        }
        return result;
}

