#include <iostream>
#include<cmath>
using namespace std;

#include "w3b_bigint.cpp"

int main() {

	BigInt x = "111111";
        BigInt y = "1111111";	
	
	cout << "d(x) = a(x) * b(x): " << endl;
        BigInt d = multiply_int(x,y);
	cout << d << endl;
	return 0;
	

}


