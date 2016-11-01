/*

Arguments, square mode (argc=6):
dtype: int or double
N:     number of rows and columns
file1: first matrix
file2: second matrix
file3: third matrix

Arguments, general mode (argc=8):
dtype: int or double
M    : rows in first matrix
N    : columns in first matrix, rows in second matrix
L    : columns in second matrix
file1: first matrix
file2: second matrix
file3: third matrix

Return codes:
1    : command line args are invalid
2    : one or more input files do not exist
3    : data in files does not conform to expectations (bad number of elements, incorrect type?)
4    : result matrix cannot be created (file write issue)


*/

//NEED TO FIX to_int and to_double in:
//PARSE ARGS
//READ double array
//READ int array

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;


typedef vector<vector<int>> int_matrix;
typedef vector<vector<double>> dub_matrix;

const int SUCCESS          = 0;
const int ERR_INVALID_ARGS = 1;
const int ERR_FILE_READ    = 2;
const int ERR_BAD_MATRIX   = 3;
const int ERR_FILE_WRITE   = 4;


//Print command line arguments
void print_args(int argc, char const *argv[]);

//Parse and validate command line arguments. Throw error if anything's bad.
void parse_args(int argc, char const *argv[], string &dtype, string &file1, string &file2, string &file3, int &M, int &N, int &L);

//Convert string to integer.
int to_integer(string num, int &convert);

//Convert string to double.
int to_double(string num, double &convert);

//Read all numbers from a text file into an MxN matrix
int read_matrix(string filename, dub_matrix &matrix, int M, int N);
int read_matrix(string filename, int_matrix &matrix, int M, int N);

//Write all numbers from a matrix to a file
int write_matrix(string filename, dub_matrix &matrix);
int write_matrix(string filename, int_matrix &matrix);

//Matrix multiplication
int_matrix multiply(const int_matrix& A,const int_matrix& B);
dub_matrix multiply(const dub_matrix& A,const dub_matrix& B);


int main(int argc, char const *argv[]) {
	
	string dtype, file1, file2, file3;
	int M, N, L;
	int return_code;
	
	dub_matrix double_matrix_1;
	dub_matrix double_matrix_2;
	dub_matrix double_matrix_3;
	int_matrix int_matrix_1;
	int_matrix int_matrix_2;
	int_matrix int_matrix_3;
	
	try{
		parse_args(argc, argv, dtype, file1, file2, file3, M, N, L);
	}
	catch (...) {
		cout << "Error. Invalid input." << endl;
		return ERR_INVALID_ARGS;
	}
	
	if (dtype == "double") {
	
		return_code = read_matrix(file1, double_matrix_1, M, N);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}
		return_code = read_matrix(file2, double_matrix_2, N, L);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}
		double_matrix_3 =  multiply(double_matrix_1, double_matrix_2);
		return_code = write_matrix(file3, double_matrix_3);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}
	
	}

	else if (dtype == "int") {

		return_code = read_matrix(file1, int_matrix_1, M, N);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}
		return_code = read_matrix(file2, int_matrix_2, N, L);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}
		//write_matrix("echo_matrix_2.txt", int_matrix_2);
		int_matrix_3 =  multiply(int_matrix_1, int_matrix_2);
		return_code = write_matrix(file3, int_matrix_3);
		if (return_code != SUCCESS) {
			//Error occurred
			return return_code;		
		}

	}


	return SUCCESS;
}


int_matrix multiply(const int_matrix& A,const int_matrix& B)
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

dub_matrix multiply(const dub_matrix& A,const dub_matrix& B)
{

 int M = A.size();
 int N = A[0].size();
 int L = B[0].size();

 dub_matrix c(M,vector<double>(L));

 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int k=0;k<N;k++)
            c[i][j] += A[i][k] * B[k][j];

 return c;
}

int write_matrix(string filename, dub_matrix &matrix) {
	ofstream fout;
	int i,j;

	fout.open(filename);

	if(fout.is_open()) {
		for(i=0; i<matrix.size(); i++) {
			for(j=0; j<matrix[i].size(); j++) {
				//cout << matrix[i][j] << " ";
				fout << matrix[i][j] << " ";		
			}
			//cout << endl;
			fout << endl;
		}
		fout.close();
	}
	else {
		cout << "Cannot open file " << filename << " for writing.";
		return ERR_FILE_WRITE;
	}
	
	return SUCCESS;
}

int write_matrix(string filename, int_matrix &matrix) {
	ofstream fout;
	int i,j;

	fout.open(filename);

	if(fout.is_open()) {
		for(i=0; i<matrix.size(); i++) {
			for(j=0; j<matrix[i].size(); j++) {
				//cout << matrix[i][j] << " ";
				fout << matrix[i][j] << " ";		
			}
			//cout << endl;
			fout << endl;
		}
		fout.close();
	}
	else {
		cout << "Cannot open file " << filename << " for writing.";
		return ERR_FILE_WRITE;
	}
	
	return SUCCESS;
}

int read_matrix(string filename, dub_matrix &matrix, int M, int N) {
	ifstream fin;
	string number;
	vector<double> numbers, buffer;
	int i,j;
	double value;


	//Read file into "numbers" vector
	fin.open(filename);

	if (fin.is_open()) {
		while(fin >> number) {
			//numbers.push_back(to_double(number));
			if(to_double(number, value) == SUCCESS) {
				numbers.push_back(value);
			}
			else {
				return ERR_BAD_MATRIX;			
			}
		}
		fin.close();
	}
	else {				
		cout << "Cannot open file " << filename << "." << endl;
		return ERR_FILE_READ;	
	}

	//Transform numbers into MxN matrix "matrix"
	
	if(numbers.size() != M*N) {
		cout << "Did not find M*N elements in " << filename << "." << endl;		
		return ERR_BAD_MATRIX;
	}

	for (i=0; i<M; i++) {
		buffer.clear();		
		for(j=0; j<N; j++) {
			buffer.push_back(numbers[i*N+j]);	
		}
		matrix.push_back(buffer);
	}

	return SUCCESS;
}

int read_matrix(string filename, int_matrix &matrix, int M, int N) {
	ifstream fin;
	string number;
	vector<int> numbers, buffer;
	int i, j;
	int value;

	fin.open(filename);

	if (fin.is_open()) {
		while(fin >> number) {
			//numbers.push_back(to_integer(number));
			if(to_integer(number, value) == SUCCESS) {
				numbers.push_back(value);			
			}
			else {
				return ERR_BAD_MATRIX;
			}
		}

		fin.close();
	}
	else {				
		cout << "no bueno" << endl;
		return ERR_FILE_READ;	
	}

	//Transform numbers into MxN matrix "matrix"
	
	if(numbers.size() != M*N) {
		cout << "Did not find M*N elements in " << filename << "." << endl;		
		return ERR_BAD_MATRIX;
	}

	for (i=0; i<M; i++) {
		buffer.clear();		
		for(j=0; j<N; j++) {
			buffer.push_back(numbers[i*N+j]);	
		}
		matrix.push_back(buffer);
	}
	return SUCCESS;
}

int to_double(string num, double &convert) {
	//make sure all elements are digits and there are no decimal points
	for (int i=0; i<num.length(); i++) {
		if (!isdigit(num[i]) && num[i]!='.' && num[i]!= '-') {
			cout << "Cannot convert element " << num << " to double." << endl;;
			return ERR_BAD_MATRIX;		
		}
	}
	convert =  atof(num.c_str());
	return SUCCESS;
}

int to_integer(string num, int &convert) {
	//make sure all elements are digits and there are no decimal points
	for (int i=0; i<num.length(); i++) {
		if (!isdigit(num[i]) && num[i]!= '-') {
			cout << "Cannot convert element " << num << " to int." << endl;
			return ERR_BAD_MATRIX;		
		}
	}
	convert = atoi(num.c_str());
	return SUCCESS;
}

void parse_args(int argc, char const *argv[], string &dtype, string &file1, string &file2, string &file3, int &M, int &N, int &L) {
	
	//Assign M, N, L
	if (argc==6) {
		//Square mode
		if (to_integer(argv[2], M)==SUCCESS) {
		N = L = M;
		}
		else {throw 1;}		
		//M = N = L = to_integer(argv[2]);
	}
	else if (argc==8) {
		//General mode
		//M     = to_integer(argv[2]);
		//N     = to_integer(argv[3]);
		//L     = to_integer(argv[4]);
		if (to_integer(argv[2],M)!=SUCCESS || to_integer(argv[3],N)!=SUCCESS || to_integer(argv[4],L)!=SUCCESS) {
			throw 1;
		}
	}
	else {
		//Unrecognized input			
		throw 1;		
	}

	//Assign data type
	dtype = argv[1];		
	if (dtype != "int" && dtype != "double") {
		throw 1;		
	}
	
	//Assign file names
	file1 = argv[argc-3];
	file2 = argv[argc-2];
	file3 = argv[argc-1];

}


void print_args(int argc, char const *argv[]) {
	cout << "number of arguments: " << argc << endl;
	for (int i=0; i<argc; i++) {
		cout << argv[i] << endl;
	}
}

