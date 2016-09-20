#include <iostream>
using namespace std;

#include "w3b_bigint.cpp"

int main() {
	
	string b = "111111";
	string c = "1111111";
	string d = multiply_int(b,c);
	cout << d << endl;
	
	/*	
	//testing	
	string e = to_string(52);
	cout << e << endl;
	int p = atoi(b.c_str());
	cout << p << endl;
	*/

	return 0;
	

}
