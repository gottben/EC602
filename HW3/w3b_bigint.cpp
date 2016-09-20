#include<vector>
#include<string>

typedef string BigInt;

BigInt multiply_int(const BigInt &a,const BigInt &b);


BigInt multiply_int(const BigInt &a,const BigInt &b) {
	
	unsigned long long int c,d;
	
	c = stoull(a);
	d = stoull(b);
	
	return to_string(c*d);
}

//string b = "111111";
//string c = "1111111";
//can i use modulus somehow??
