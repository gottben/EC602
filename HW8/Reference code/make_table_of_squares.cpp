// Make a new file with first ten numbers and their squares

#include <iostream>


#include <fstream>

using namespace std;


int main ()
{
	ofstream filewithnumbers; // note: this is an OFSTREAM, "O" stands for OUTPUT

	
	filewithnumbers.open("table_of_squares.txt");

	for (int i=1; i <= 10; i++)
       filewithnumbers << i << " " << i*i << endl;

    filewithnumbers.close();


  return 0;
}
