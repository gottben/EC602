// AUTHOR BrianAppleton appleton@bu.edu
// AUTHOR AlexBennett gottbenn@bu.edu
// AUTHOR CathrynCallahan cathcal@bu.edu
// AUTHOR PreranaHaridoss preranah@bu.edu

// git repository https://github.com/gottben/EC602

#include<vector>

typedef vector<double> Poly;

Poly add_poly(const Poly &a,const Poly &b);
Poly multiply_poly(const Poly &a,const Poly &b);

Poly add_poly(const Poly &a,const Poly &b) {
	//add two polynomials and return the result
	Poly result;
	
	//cout << "sizes: " << a.size() << " " << b.size() << endl;
		
	//iterate through the shorter vector and add coefficients
	if (a.size() >= b.size()) {
		result = a;
		for(int i = 0; i<b.size(); i++) {
			result[i] += b[i];
			//cout << "here1 " << i << endl;		
		}
	}
	else {
		result = b;
		for(int i = 0; i<a.size(); i++) {
			result[i] += a[i];
			//cout << "here2 " << i << endl;	
		}
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

	//cout << "result size: " << result.size() << endl;
	//cout << "sizes: " << a.size() << " " << b.size() << endl;
		

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




