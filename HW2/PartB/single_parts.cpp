// single_parts
#include <iostream>
#include <iomanip>
#include <cassert> 
using namespace std;

typedef unsigned long int raw32; // need to figure out what this shall // ..

// A structure which mimics exactly the internal representation of single float
// Single Parts uses 32 bits of storage 

struct Single_Parts { 
	raw32 fraction : 23 ; // use 23 for this
	raw32 exponent : 8 ; // use 8 for this 
	raw32 sign : 1;     // use 1 for this 
	}; 

// these represent the position of the SIGN, EXPONENET, and FRACTION of double.
const raw32 MASK_SIGN = 1UL << 31;
const raw32 MASK_BEXP = 0xffUL << 23; 
const raw32 MASK_FRAC = 0x7fffffUL; 
// print out the parts of the structure Single_Parts


void print_sp(Single_Parts sp) 
{ 
  if (sp.sign==1)
		 cout << "negative"  << endl;
  else 
  		cout << "positive" << endl;

 cout << hex  
      << setfill('0') 
      << "expo: " << sp.exponent << endl
      << "frac: " << sp.fraction << endl
      << dec;
}

// build and take_apart are inverse functions. 
Single_Parts take_apart(float f)
{
	Single_Parts fl;
	raw32 x = *reinterpret_cast<raw32*>(&f);

	fl.sign = (x bitand MASK_SIGN) >> 31; 
	fl.exponent = (x bitand MASK_BEXP) >> 23;
	fl.fraction = (x bitand MASK_FRAC); 

	return fl;
}

float build(Single_Parts fl)
{
	//read this from inside out:
	//this means get the address of fl, then think of it as a pointer to a float
	// then get the float and return it.
	return *reinterpret_cast<float*>(&fl);
}


// define Single_Parts, build(), and take_apart() for float
const int EXAMPLES = 5; 
int main()
{
	//assert(sizeof(raw32)==4); // make sure this is actually an 4-byte object.
	double num_from_build;

	double numbers[EXAMPLES]={1.0/3,2,1.3e10,3e11,6};
	
	// show the structure of the numbers 
	for (int i=0;i<EXAMPLES;i++)
	{   
		// take apart the numbers, then re-build to test that it works.
		
		Single_Parts s = take_apart(numbers[i]);
	 	num_from_build = build(s);

	 	cout << endl;
	    print_sp(s);
	 	cout << numbers[i] << " " << num_from_build  << endl;
	}

    // example of a weird number, negative zero.
    double neg_zero{-0.0};

    cout << endl; 
    cout << neg_zero << endl;

    print_sp(take_apart(neg_zero));

    return 0;
}