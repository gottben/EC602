// double_parts
#include <iostream>
#include <iomanip>
#include <cassert>

using namespace std;

typedef unsigned long long int raw64; // raw64 is a pseudonym for unsigned long long int

// A structure which mimics exactly the internal representation of double
// Double Parts uses  64-bits of storage

struct Double_Parts {
	raw64 fraction : 52;  // use 52 bits for this
	raw64 exponent : 11; // then 11 bits for this
	raw64 sign : 1;      // then 1 bit for this
} ;


// these represent the positions of the SIGN, EXPONENT, and FRACTION of double.

const raw64 MASK_SIGN = 1ULL << 63;
const raw64 MASK_BEXP = 0x7ffULL << 52;
const raw64 MASK_FRAC = 0xfffffffffffffULL;


// print out the parts of the structure Double_Parts
void print_dp(Double_Parts dp) 
{ 
  if (dp.sign==1)
		 cout << "negative"  << endl;
  else 
  		cout << "positive" << endl;

 cout << hex  
      << setfill('0') 
      << "expo: " << dp.exponent << endl
      << "frac: " << dp.fraction << endl
      << dec;
}


// build and take_apart are inverse functions.

Double_Parts take_apart(double d)
{
 Double_Parts dp;
 raw64 x =  *reinterpret_cast<raw64*>(&d); 

 dp.sign = (x bitand MASK_SIGN) >> 63;
 dp.exponent = (x bitand MASK_BEXP) >> 52;
 dp.fraction = (x bitand MASK_FRAC);

 return dp;

}

double build(Double_Parts dp)
{ 
	   // read this from inside out:
	   // this means get the address of dp, then think of it as a pointer to a double
	   // then get the double and return it.
       return *reinterpret_cast<double*>(&dp);
}

double build_alt(Double_Parts dp)
{   
	raw64 c=0;

    // explicitly move the double parts to their correct locations, and add.

	c = ( (raw64)dp.sign << 63) + ( (raw64)dp.exponent << 52) + dp.fraction;
	   
	// read this from inside out:
	// this means get the address of c, then think of it as a pointer to a double
	// then get the double and return it.
	return *reinterpret_cast<double*>(&c) ;
}


// We will show 5 examples
const int EXAMPLES = 5;

int main()
{
	assert(sizeof(raw64)==8); // make sure this is actually an 8-byte object.

	double num_from_build, num_from_build_alt;

	double numbers[EXAMPLES]={1.0/3,2,1e100,-5e-200,6};
	
	// show the structure of the numbers 
	for (int i=0;i<EXAMPLES;i++)
	{   
		// take apart the numbers, then re-build to test that it works.
		
		Double_Parts dp= take_apart(numbers[i]);
	 	num_from_build = build(dp);
	 	num_from_build_alt = build_alt(dp);

	 	cout << endl;
	    print_dp(dp);
	 	cout << numbers[i] << " " << num_from_build << " " << num_from_build_alt << endl;
	}

    // example of a weird number, negative zero.
    double neg_zero{-0.0};

    cout << endl; 
    cout << neg_zero << endl;

    print_dp(take_apart(neg_zero));

    return 0;
}