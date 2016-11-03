// AUTHOR Cathryn Callahan cathcal@bu.edu
// AUTHOR Matthew Brawley mbrawley@bu.edu
//
// Part A: Matrix Multiply with C++
// Write a C++ program that reads in two matricies from two text files, and outputs the
//	result in a third text file. 

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

typedef vector<vector<int>> int_matrix;
typedef vector<vector<double>> double_matrix;

void show_arguments(int argc, char const *argv[]);
void process_command(int argc, char const *argv[], int &M, int &N, int &L, string &dtype, string &file1, string &file2, string &file3);

int convert_int(string str_number, int &int_number);
int convert_double(string str_number, double &double_number);

int read_in_int(string file, int_matrix &matrix, int M, int N);
int read_in_double(string file, double_matrix &matrix, int M, int N);

int_matrix multiply_int(const int_matrix &A, const int_matrix &B);
double_matrix multiply_double(const double_matrix &A, const double_matrix &B);

int write_out_int(string file, int_matrix &matrix);
int write_out_double(string file, double_matrix &matrix);


// ERRORS:
// 1 - Command Line Arguments Invalid
// 2 - One or more of the input files do not exist
// 3 - Data in file does not conform to expectation
// 4 - the result matrix cannot be created

int main(int argc, char const *argv[]) 	
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
	int r_code;
	int_matrix int_matrix_1, int_matrix_2, int_matrix_3;
	double_matrix double_matrix_1, double_matrix_2, double_matrix_3;

	try{
		process_command(argc, argv, M, N, L, dtype, file1, file2, file3);
	}
	catch(...){
		cout << "Invalid Command Line Arguments." << endl;
		return 1;
	}

	if (dtype == "int")
	{
		//show_arguments(argc, argv);
		r_code=read_in_int(file1, int_matrix_1, M, N);
		if(r_code !=0){return r_code;}
		r_code=read_in_int(file2, int_matrix_2, N, L);
		if(r_code !=0){return r_code;}

		// MULTIPLY
		int_matrix_3 = multiply_int(int_matrix_1, int_matrix_2);

		r_code=write_out_int(file3, int_matrix_3);
		if(r_code !=0){return r_code;}
	}
	else if(dtype == "double")
	{
		//show_arguments(argc, argv);
		r_code=read_in_double(file1, double_matrix_1, M, N);
		if(r_code !=0){return r_code;}
		r_code=read_in_double(file2, double_matrix_2, N, L);
		if(r_code !=0){return r_code;}

		// MULTIPLY
		double_matrix_3 = multiply_double(double_matrix_1, double_matrix_2);

		r_code=write_out_double(file3, double_matrix_3);
		if(r_code !=0){return r_code;}
	}
	//else
	//{
	//	cout << "incorect data type." << endl;
	//}
	
	//cout << int_matrix_1 <<endl;

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

int convert_int(string str_number, int &int_number)
{
	for(int i=0; i<str_number.length(); i++)
	{	
		if(!isdigit(str_number[i]) && str_number[i] !='-')
		{
			return 3;
		}
	}
	int_number = stoi(str_number.c_str());
	//cout<< "str_number " << str_number << endl;
	return 0;
}

int convert_double(string str_number, double &double_number)
{
	for(int i=0; i<str_number.length(); i++)
	{	
		if(!isdigit(str_number[i]) && str_number[i] !='-' && str_number[i] !='.')
		{
			return 3;
		}
	}
	double_number = stod(str_number.c_str());
	return 0;
}


void process_command(int argc, char const *argv[], int &M, int &N, int &L, string &dtype, string &file1, string &file2, string &file3)
{
	
		// SQUARE NxN MATRIX
		if (argc == 6)
		{
			if(convert_int(argv[2],M)==0)
			{
				//M = convert_int(argv[2],M);
				N = L = M;
			}
			else {throw 1;}
			
			//convert_int(argv[2],M);
			//cout<< "M =" << M << "and N= " << N<< endl;

			file1 = argv[3];	//First Input Matrix File
			file2 = argv[4];	//Second Input Matrix File
			file3 = argv[5];	//Output Matrix File
		}

		// GENERAL MxN and NxL MATRICES
		else if (argc == 8)
		{
			if(convert_int(argv[2],M)==0 && convert_int(argv[3],N)==0 && convert_int(argv[4],L)==0)
			{
				//M = convert_int(argv[2],M);
				//N = convert_int(argv[3],N);
				//L = convert_int(argv[4],L);
			}
			else
				{throw 1;}
			/*if (convert_int(argv[2],M)!=0 || convert_int(argv[3],N)!=0 || convert_int(argv[4],L)!=0) 
			{
				throw 1;
				//if(convert_int(argv[2],M)==GOOD)
			}*/
			//convert_int(argv[2],M);
			//convert_int(argv[3],N);
			//convert_int(argv[4],L);
			//cout<< "M =" << M << "and N= " << N<< endl;

			file1 = argv[5];	//First Input Matrix File
			file2 = argv[6];	//Second Input Matrix File
			file3 = argv[7];	//Output Matrix File
		}
		else
		{	// COMMAND LINE ARGS INVALID - RETUN ERROR CODE 1
			cout<<"the comand line arguments are invalid" <<endl;
			//cout<<"data does not conform to the expectations"<<endl;
			throw 1;
		}
	
	dtype = argv[1];
	if( dtype != "int" && dtype != "double")
	//if (strcmp (dtype, "int") != 0 || strcmp (dtype,"double")!=0)
	{
		// COMMAND LINE ARGS INVALID - RETUN ERROR CODE 1
		cout<<"the comand line arguments are invalid - not int or double" <<endl;
		throw 1;
	}
}

int read_in_int(string file, int_matrix &matrix, int M, int N)
{
	//cout << "M is" << M << "N is" << N << endl;
	ifstream thisfile;  // "i" stands for INPUT
	vector<int> elements,parts;
	int_matrix out;
	int numbers, i,j;
	string mat_string;

	thisfile.open(file);
	while (thisfile >> mat_string)
	{
		if(convert_int(mat_string, numbers)==0)
		{
			elements.push_back(numbers);
		}
		else
		{
			return 3;
		}
	}
	//cout << elements.size() << endl;
	thisfile.close();

	if(elements.size() != M*N) 
	{
		cout << "Did not find M*N elements in " << file << "." << endl;		
		return 3;
	}

	for (i=0; i<M; i++) 
	{
		parts.clear();
		for(j=0; j<N; j++) 
		{
			parts.push_back(elements[i*N+j]);	
		}
		matrix.push_back(parts);
	}
	return 0;
}

int read_in_double(string file, double_matrix &matrix, int M, int N)
{
	ifstream thisfile;  // "i" stands for INPUT
	vector<double> elements,parts;
	double_matrix out;
	int i,j;
	double numbers;
	string mat_string;

	thisfile.open(file);
	while (thisfile >> mat_string)
	{
		if(convert_double(mat_string, numbers)==0)
		{
			elements.push_back(numbers);
		}
		else
		{
			return 3;
		}
	}

	//cout << "size= " << elements.size() << "M=" << M << " and N=" << N << endl;
	thisfile.close();

	if(elements.size() != M*N) 
	{
		cout << "Did not find M*N elements in " << file << "." << endl;		
		return 3;
	}

	for (i=0; i<M; i++) 
	{
		parts.clear();
		for(j=0; j<N; j++) 
		{
			parts.push_back(elements[i*N+j]);	
		}
		matrix.push_back(parts);
	}
	return 0;
}

int write_out_int(string file, int_matrix &matrix)
{
	ofstream outfile; 
	outfile.open(file);
	if(outfile.is_open())
	{
		for(int i=0; i<matrix.size(); i++)
		{
			for(int j=0; j<matrix[i].size(); j++) 
			{
				outfile << matrix[i][j] << " ";		
			}
			outfile << endl;
		}
		outfile.close();

	}
	else
	{
		cout<< "Cannot open output file." << endl;
		return 4;
	}
	return 0; 
}

int write_out_double(string file, double_matrix &matrix)
{
	ofstream outfile; 
	outfile.open(file);
	if(outfile.is_open())
	{
		for(int i=0; i<matrix.size(); i++) 
		{
			for(int j=0; j<matrix[i].size(); j++) 
			{
				outfile << matrix[i][j] << " ";		
			}
			outfile << endl;
		}
		outfile.close();

	}
	else
	{
		cout<< "Cannot open output file." << endl;
		return 4;
	}
	return 0; 
}


int_matrix multiply_int(const int_matrix &A, const int_matrix &B)
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
}

double_matrix multiply_double(const double_matrix &A, const double_matrix &B)
{

 int M = A.size();
 int N = A[0].size();
 int L = B[0].size();

 double_matrix c(M,vector<double>(L));

 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int k=0;k<N;k++)
            c[i][j] += A[i][k] * B[k][j];

 return c;
}




