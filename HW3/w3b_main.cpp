#include <iostream>
using namespace std;

#include "w3b_bigint.cpp"

void print_test_case(string a, string b);

int main() {
	string a = "3450823583275802374528348572384562356";
	string b = "6032";
	string c = "596"; 
	string d = "111111";
	string e = "1111111";
	string f = "999999";
	
	print_test_case(d,e);
	print_test_case(f,b);
	print_test_case(a,f);
	
	return 0;
	

}

void print_test_case(string a, string b) {
	cout << a << " * " << b << " = " << multiply_int(a,b) << endl;
}
