// AUTHOR BrianAppleton appleton@bu.edu
// AUTHOR AlexBennett gottbenn@bu.edu
// AUTHOR CathrynCallahan cathcal@bu.edu
// AUTHOR PreranaHaridoss preranah@bu.edu

// git repository https://github.com/gottben/EC602

#include<vector>
#include<string>

typedef string BigInt;
typedef vector<double> Poly;

BigInt multiply_int(const BigInt &a,const BigInt &b);

//polynomial multiplication function from HW3 part A
Poly multiply_poly(const Poly &a,const Poly &b);

//conversion functions
Poly BigInt_to_Poly(const BigInt &a);
BigInt Poly_to_BigInt(const Poly &a);

//coefficient formatting function
Poly format_poly(Poly &a, unsigned int x);


BigInt multiply_int(const BigInt &a,const BigInt &b) {
	
	Poly Poly_a, Poly_b, Poly_ab, Poly_ab_formatted;
	
	unsigned int x = 10; //hard-code decimal behavior
	
	//Convert BigInts a and b to their polynomial representations Poly_a and Poly_b		
	Poly_a = BigInt_to_Poly(a);
	Poly_b = BigInt_to_Poly(b);

	//Multiply the polynomials using the functionality developed in HW3 part A
	//The coefficients we get won't necessarily be in decimal format (i.e., they might be greater than 9)
	Poly_ab = multiply_poly(Poly_a, Poly_b);
	
	//Format the polynomials given the desired base (x)
	Poly_ab_formatted = format_poly(Poly_ab,x);
	
	//Convert the formatted polynomial back to a BigInt format and return it
	return Poly_to_BigInt(Poly_ab_formatted);
	
}

Poly format_poly(Poly &a, unsigned int x) {
	//reformat polynomial so coeffecients are <x
	
	Poly result;
	result = a;	
	
	for(int i=0; i<result.size(); i++) {
		if(result[i]>(x-1)) {			
			//we need to carry
			if(i==result.size()-1) {				
				//we need a higher-order term in order to carry
				result.push_back((int)result[i]/x);			
			}
			else {			
				//higher-order term is available to carry into				
				result[i+1] += (int)result[i]/x;
			}
			//set a[i] to what's left after the carry
			result[i] = ((int)result[i])%x;
		}
	}
	return result;
}

Poly BigInt_to_Poly(const BigInt &a) {
	//convert string representation of decimal number (e.g., "123") to a Poly vector
	//  (e.g., {3,2,1} - lowest order terms first)
	
	Poly result;
	result.clear();
	result.resize(a.size());

	for(int i=0; i<a.size(); i++) {
		result[i]=a[a.size()-1-i]-'0';
	}
	
	return result;

}

BigInt Poly_to_BigInt(const Poly &a) {
	//convert Poly vector representation of number (e.g., {3,2,1} - lowest order terms first)
	//  to string representation of number (e.g., "123")

	BigInt result;
	result.clear();
	result.resize(a.size());

	for(int i=0; i<a.size(); i++) {
		result[i]=(int)a[a.size()-1-i]+'0';
	}
	
	return result;
}


Poly multiply_poly(const Poly &a,const Poly &b) {
	//multiply two polynomials and return the result

	//for every element in a, multiply the coefficient with each term in b
	//add the exponents for both terms and store in the appropriate position in the result vector

	int i,j;
	int coeff, exp;

	//initialize, clear, and size the result vector
	Poly result;
	result.clear();
	result.resize(a.size()+b.size()-1,0);

	for(i=0; i<a.size(); i++) {
		for(j=0; j<b.size(); j++) {
			coeff = a[i]*b[j];
			exp = i+j;
			result[exp] += coeff;
			//cout << i << " " << j << endl;
		}
	}
	return result;
}
