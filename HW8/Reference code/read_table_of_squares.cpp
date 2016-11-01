#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
	ifstream thisfile; // note: this is an IFSTREAM, "I" stands for INPUT

	int one,two;
	vector<int> squares;       
    

	thisfile.open("table_of_squares.txt");

	while (thisfile >> one >> two)
	{ 
		cout << one << " " << two << endl;
		squares.push_back(two);
    }

    thisfile.close(); 

    for (auto s: squares){
    	cout << s << endl;
    }
  return 0;
}
