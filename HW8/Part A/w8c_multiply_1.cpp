// AUTHOR Cathryn Callahan cathcal@bu.edu
// 
// Part A: Matrix Multiply with C++
// Write a C++ program that reads in two matricies from two text files, and outputs the
//	result in a third text file. 

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <typeinfo>
using namespace std;

typedef vector <vector<int>> int_matrix;
typedef vector <vector<double>> double_matrix;


void show_arguments(int argc, char const *argv[]);
void process_command(int argc, char const *argv[], int &M, int &N, int &L, string &dtype, string &file1, string &file2, string &file3);

int convert_int(string number);
int convert_double(string number);

//int_matrix read_in_int(string &file1, int &M, int &N);
int_matrix read_in_int(string &file1, int_matrix &matrix,int &M, int &N);
double_matrix read_in_double(string &file1, int &M, int &N);




int main(int argc, char const *argv[]) 	//add in file3 for multiply result txt file
{ 	// argc = argument count, the amount of arguments, separated by spaces, that
	// were entered  when the program was invoked.
	//argv = argument vector, contains the actual arguments themselves
		// argv[0] will always be the command used to invoke the program
	
	// SHOW ARGUMENTS
	/*int i, j;
	cout << "argc is "<< argc<< endl;
	for (i=0; i<argc; i++)
	{
		cout<< "argv of " << i << "is" << argv[i] <<endl;
		j = 0;
		while(argv[i][j]) 	// equivelant to (argv[i][j] != '\0')
			cout<<argv[i][j++];
		cout<<" len = " << j << endl;
	}*/
	string dtype, file1, file2, file3;
	int M, N, L;
	int_matrix matrix;

	show_arguments(argc, argv);
	process_command(argc, argv, M, N, L, dtype, file1, file2, file3);
	read_in_int(file1, matrix, M, N); 

return 0;
}

void show_arguments(int argc, char const *argv[])
{
	cout << "Aruguments: "<< argc << endl;
	for (int i=0; i<argc; i++)
	{
			cout<<argv[i] <<endl;
	}
}

int convert_int(string number)
{
	int conversion = stoi(number.c_str());
	return conversion;
}
int convert_double(string number)
{
	double conversion = stod(number.c_str());
	return conversion;
}



/*int_matrix multiply(const int_matrix& A,const int_matrix& B)
{

 int M = A.size();
 int N = A[0].size();
 int L = B[0].size();

 int_matrix c(M,vector<int>(L));

 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int k=0;k<N;k++)
            c[i][j] += A[i][k] * B[k][j];

 return c;
}*/


void process_command(int argc, char const *argv[], int &M, int &N, int &L, string &dtype, string &file1, string &file2, string &file3)
{
	
		// SQUARE NxN MATRIX
		if (argc == 6)
		{
			M = convert_int(argv[2]);
			N = L = M;
			/*if(convert_int(argv[2],M) == GOOD)
			{
				N = M;
				L = M;
			}*/
		}

		// GENERAL MxN and NxL MATRICES
		else if (argc ==8)
		{
			M = convert_int(argv[2]);
			N = convert_int(argv[3]);
			L = convert_int(argv[4]);
			//if(convert_int(argv[2],M)==GOOD)
		}
		else
		{	// COMMAND LINE ARGS INVALID - RETUN ERROR CODE 1
			cout<<"the comand line arguments are invalid" <<endl;
			cout<<"data does not conform to the expectations"<<endl;
		}
	
	if (strcmp (argv[1], "int") != 0 || strcmp (argv[1],"double")!=0)
	{
		// COMMAND LINE ARGS INVALID - RETUN ERROR CODE 1
		cout<<"the comand line arguments are invalid" <<endl;
	}
	
}

int_matrix read_in_int(string const &file1, int_matrix &matrix, const int &M, const int &N)
{
	ifstream thisfile;  // "i" stands for INPUT
	vector<int> elements,parts;
	int_matrix out;
	int numbers,i,j;

	thisfile.open(file1);
	while (thisfile >> numbers)
	{
		elements.push_back(numbers);
	}

	cout << elements.size() << endl;
	thisfile.close();
	if(elements.size() != M*N) {
		cout << "Did not find M*N elements in " << file1 << "." << endl;		
		//return ERR_BAD_MATRIX;
	}
	for (i=0; i<M; i++) {
		for(j=0; j<N; j++) {
			parts.push_back(elements[i*N+j]);	
		}
		matrix.push_back(parts);
	}
	return matrix;
}






