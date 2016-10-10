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

	//result of a^2 given by wolfram alpha
	string a2_answer = "11908183402892448565615714461053536103843181587412471415422999469652270736";
	
	print_test_case(d,e);
	print_test_case(f,b);
	print_test_case(a,f);
	print_test_case(a,a);
	
	if(multiply_int(a,a)==a2_answer) {
		cout << ";)" << endl;	
	}
	
	return 0;
	

}

void print_test_case(string a, string b) {
	cout << a << " * " << b << " = " << multiply_int(a,b) << endl;
}
