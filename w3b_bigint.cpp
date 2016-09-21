#include <string> 

typedef string BigInt;
BigInt multiply_int(const BigInt &a,const BigInt &b);




BigInt multiply_int(const BigInt &a, const BigInt &b)
{
	int a_int;
	int b_int; 
	int length_a; 
	int length_b;

	length_a = a.length();
	length_b = b.length();

	int ar_len = length_a+length_b -1; 

	int number_array[ar_len]; 
	int tens_array[1] = {0}; 

	string returnstring = "";

	// initializes the number_array values to all zeros. Helpful when your memory is filled with junk.
	for(int f = 0; f < ar_len; f++)
	{
		number_array[f] = 0;
	}

	// the product of the sizes of the two polynomials being multiplied
	// keeps track of how many times we have performed the multiplication
	// multiply vales in this manner a[1]*b[1] + a[1]*b[2] etc. etc. 
	for(int i = 0; i < length_a ; i++)
	{

		for(int j = 0; j < length_b; j++)
		{
			a_int = a[i] - '0';
			//cout <<"this is a_int=" << a_int << endl;
			b_int = b[j] - '0';
			//cout << "this is b_int=" << b_int << endl;
			int product_a_b = a_int*b_int; 
			number_array[i+j] += product_a_b; 
			//cout << number_array[i+j] << endl;
		}
	}


	for(int k = ar_len-1; k > -1; k--)
	{
		//cout << k << endl;
		//cout << number_array[k] << endl;
		if(number_array[k] >= 10){
			if(k < 1){
				//cout << "here" << endl; 
				tens_array[1] = number_array[k]/10; 
				number_array[k] = number_array[k]%10;
			}
			else{
				//cout << "here1" << k-1 << endl;
				number_array[k-1] += number_array[k]/10;
				//cout << number_array[k]/10 << endl;

			}
			number_array[k] = number_array[k]%10;
		}
	}



	// convert the number_array back into a string. 
	if(tens_array[1] <= 0)
	{
		for(int s = 0; s < ar_len; s++)
		{
			//cout << number_array[k] << endl;
			returnstring += number_array[s] + '0';
			//cout << returnstring << endl;
		}
	}
	else{
		returnstring += tens_array[1] + '0';

		//cout << "is it returning anything=" <<returnstring << endl;

		for(int l = 0; l < ar_len; l++)
		{
			//cout << number_array[k] << endl;
			returnstring += number_array[l] + '0';
		}	
	}


		return returnstring; 
}


