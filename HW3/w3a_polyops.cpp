// AUTHOR BrianAppleton appleton@bu.edu
// AUTHOR AlexBennett gottbenn@bu.edu
// AUTHOR CathrynCallahan cathcal@bu.edu
// AUTHOR PreranaHaridoss preranah@bu.edu

#include <vector>
using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b);
// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a,const Poly &b);

Poly add_poly(const Poly &a,const Poly &b){
	Poly result;
	Poly number;
	//checkw hich number is larger
	if(a.size() > b.size()){
		result = a;
		number = b;
	}
	else{
		result = b;
		number = a;
	}

	//addition of the two numbers
	for(int i=0;i<number.size();i++){
		result[i] = result[i]+number[i];
	}

	return result;
}

Poly multiply_poly(const Poly &a,const Poly &b){
	
	Poly result((a.size()+b.size()-1),0);
	//for(int x=0;x<(a.size()+b.size()-1);x++)
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++){
			result[i+j] = result[i+j]+ (b[j]*a[i]);
			
		}			
	}
	return result;	
}


