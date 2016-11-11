// Author AlexBennett gottbenn@bu.edu

// Convert command line values to double

// Command to compile C++ code: g++ '-std=c++1y' <filename> 


#include <iostream>
#include <string> // provides stoX where X can be i (int), d (double), etc.
#include <fstream> 
#include <vector> 

using namespace std;

// Function Declarations using generic templates 
template <typename vector_class> vector_class read_file(vector_class squares, string filename, string dtype);
template <typename matrix_shape, typename vector_class, typename row_class, typename column_class> matrix_shape shape_matrix(int M, int L, vector_class squares, row_class row, column_class column);
template <typename matrix_multiply, typename row_class, typename column_class> matrix_multiply multiply_matrix(matrix_multiply M1, matrix_multiply M2, int M, int L, int T, row_class row, column_class column);
template <typename matrix_class> int print_matrix(int M, int L, matrix_class matrix, string filename);

// Define Global Error constants 
const int  ERROR_ONE = 1; 			//	invalid command line arguments
const int ERROR_TWO = 2; 			//	one or more input files don't exist
const int ERROR_THREE = 3;			//	data in files doesn't conform to expectations 
const int ERROR_FOUR = 4; 			//	the result matrix cannot be created 

/********************************************************************************************************************************************/
/*************************************** The beginning of Main ******************************************************************************/
/********************************************************************************************************************************************/

int main(int argc, char const *argv[])
{
// Check to see if there the # of expected input arguments than there should be. 
if ((argc-1) != 5 && (argc-1) != 7)
{
	cout << argc-1 << endl;
	cout << "ERROR_ONE: command line inputs invalid" << endl;
	return ERROR_ONE; 
}


// check to see if we are provided a valid datatype. 
try
{
	if((argc-1) == 7)
	{
		std:: string dtype = argv[argc-7];
		if(dtype != "int" && dtype !="double")
		{
			//cout << "ERROR_ONE: command line inputs invalid" << endl;
			return ERROR_ONE; 
		}
	}
	else if((argc-1) == 5)
	{
		std:: string dtype = argv[argc- 5];
		if(dtype != "int" && dtype !="double")
		{
			//cout << "ERROR_ONE: command line inputs invalid" << endl;
			return ERROR_ONE; 
		}
	}
}
catch (...)
{
	//cout << "ERROR_ONE: command line inputs invalid" << endl;
	return ERROR_ONE; 
}

// create the dtype variable
std:: string dtype = argv[1]; 

// test to see if the input files were provided
// we have to redifine them outside of this test if we want to use them in the main. 
try
{
	std:: string filename1 = argv[argc-3];
	std:: string filename2 = argv[argc-2];
	std:: string output_file = argv[argc-1];
}
catch (...) 
{
	//cout << "ERROR_ONE: command line inputs invalid" << endl;
	return ERROR_ONE; 
}

// test to see if the matrix dimensions were provided
try 
{
	if((argc-1) == 5)
	{
		int dimension = stoi(argv[argc-4]);
		if(dimension < 1)
		{
			//cout << "ERROR_ONE: command line inputs invalid" << endl;
			return ERROR_ONE; 
		}
	}
	else if((argc-1) == 7)
	{
		int dim1 = stoi(argv[argc-6]);
		int dim2 = stoi(argv[argc-5]);
		int dim3 = stoi(argv[argc-4]);
		if((dim1 < 1) || (dim2 < 1) || (dim3 <1))
		{
			cout << "ERROR_ONE: command line inputs invalid" << endl;
			return ERROR_ONE;
		}
	}
}
catch (...)
{
	cout << "ERROR_ONE: command line inputs invalid" << endl;
	return ERROR_ONE;
}


// redefinition of input and output filenames. 
	std:: string filename1 = argv[argc-3];
	std:: string filename2 = argv[argc-2];
	std:: string output_file = argv[argc-1];

// test to see if the files open & if we are are getting the variables we expect
	try
	{
		ifstream filetest; 
		filetest.open(filename1);
		if(!filetest.is_open())
		{
			cout << "ERROR_TWO: one or more input files does not exist" << endl;
			return ERROR_TWO;
		}
		if(dtype == "int")
		{

		}
		filetest.close();
		filetest.open(filename2);
		if(!filetest.is_open())
		{
			cout << "ERROR_TWO: one or more input files does not exist" <<endl;
			return ERROR_TWO;
		}
		filetest.close();
	}
	catch(...)
	{
		return ERROR_TWO;
	}

// test to see if we have the correct input values from the text files && test to see if we can create a proper matrix from the input files.
	
	try
	{
		if(dtype=="int")
		{
			vector<int> squares1,squares2;
			squares1 = read_file <vector<int>>(squares1,filename1,dtype);
			squares2 = read_file <vector<int>>(squares2,filename2,dtype);
			if((argc-1) == 5)
			{
				int theoretical_size = stoi(argv[2])*stoi(argv[2]);
				if((theoretical_size == 1) || (theoretical_size == 0))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE; 
				}
				if((squares1.size() != squares2.size()) || (squares2.size() != theoretical_size))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE;
				}
			}
			else if((argc-1) == 7)
			{
				int theoretical_size1 = stoi(argv[2]) * stoi(argv[3]);
				int theoretical_size2 = stoi(argv[3]) * stoi(argv[4]);
				if((theoretical_size1 == 1) || (theoretical_size2 == 1))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE; 
				}
				if((squares1.size() != theoretical_size1) || (squares2.size() != theoretical_size2))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE;
				}
			}
		}
		else if(dtype == "double")
		{
			vector<double> squares1,squares2;
			squares1 = read_file <vector<double>>(squares1,filename1,dtype);
			squares2 = read_file <vector<double>>(squares2,filename2,dtype);
			if((argc-1) == 5)
			{
				int theoretical_size = stoi(argv[2])*stoi(argv[2]);
				if((theoretical_size == 1) || (theoretical_size == 0))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE; 
				}
				if((squares1.size() != squares2.size()) && (squares2.size() != theoretical_size))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE;
				}
			}
			else if((argc-1) == 7)
			{
				int theoretical_size1 = stoi(argv[2]) * stoi(argv[3]);
				int theoretical_size2 = stoi(argv[3]) * stoi(argv[4]);
				if((theoretical_size1 == 1) || (theoretical_size2 == 1))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE; 
				}
				if((squares1.size() != theoretical_size1) || (squares2.size() != theoretical_size2))
				{
					cout << "ERROR_THREE: Cannot create matrix" << endl;
					return ERROR_THREE;
				}
			}
		}
	}
	catch (...)
	{
		cout << "ERROR_THREE: inputs not what were expected" << endl;
		return ERROR_THREE; 
	}


/********************************************************************************************************************************************/
//				This marks the end of the checker and the beginning of the steps to multiplication
/*********************************************************************************************************************************************/ 

	if(dtype == "int")
	{

	// Open up the first file and perform the operation of accessing 
	// the matrix data. This component of the program opens up files 
	// and imports them into a vector. 
		vector<int> squares1,squares2;

		squares1 = read_file <vector<int>>(squares1,filename1,dtype);
		squares2 = read_file <vector<int>>(squares2,filename2,dtype);




	// The next thing we need to do is prepare the vectors we made 
	// to be multiplied together by converting them into matrices. 
		if((argc-1) == 5)
		{
			int M = stoi(argv[2]);
			int* row = 0;
			int column = 0;
			int** M1     = shape_matrix <int**>(M, 1, squares1, row, column);
			int** M2     = shape_matrix <int**>(M, 1, squares2, row, column);
			int** squares3 = multiply_matrix(M1, M2, M, 1, 1, row, column);
			int print = print_matrix(M,1,squares3,output_file);
			if(print == 4)
				return ERROR_FOUR;
		}
		else
		{
			int M = stoi(argv[2]);
			int L = stoi(argv[4]);
			int T = stoi(argv[3]);
			int* row = 0; 
			int column = 0; 
			int** M1     = shape_matrix <int**> (M,T,squares1, row, column);
			int** M2     = shape_matrix <int**> (T,L,squares2, row, column);
			int** squares3 = multiply_matrix(M1, M2, M, L, T, row, column);
			int print = print_matrix(M,L,squares3,output_file);
			if(print == 4)
				return ERROR_FOUR;
		}
	}
	else if(dtype == "double")
	{
	// Open up the first file and perform the operation of accessing 
	// the matrix data. This component of the program opens up files 
	// and imports them into a vector. 
		vector<double> squares1,squares2;

		squares1 = read_file <vector<double>>(squares1,filename1,dtype);
		squares2 = read_file <vector<double>>(squares2,filename2,dtype);

	// The next thing we need to do is prepare the vectors we made 
	// to be multiplied together by converting them into matrices. 
		if((argc-1) == 5)
		{
			int M = stoi(argv[2]);
			double* row = 0;
			double column = 0;
			double** M1     = shape_matrix <double**>(M, 1, squares1, row, column);
			double** M2     = shape_matrix <double**>(M, 1, squares2, row, column);
			double** squares3 = multiply_matrix(M1, M2, M, 1, 1, row, column);
			int print = print_matrix(M,1,squares3,output_file);
			if(print ==4)
				return ERROR_FOUR;
		}
		else
		{
			int M = stoi(argv[2]);
			int L = stoi(argv[4]);
			int T = stoi(argv[3]);
			double* row = 0; 
			double column = 0; 
			double** M1     = shape_matrix <double**> (M,T,squares1, row, column);
			double** M2     = shape_matrix <double**> (T,L,squares2, row, column);
			double** squares3 = multiply_matrix(M1, M2, M, L, T, row, column);
			int print = print_matrix(M,L,squares3,output_file);
			if(print == 4)
				return ERROR_FOUR;

		}
	}
}
/*********************************************************************************************************************************************/
// This is the end of Main
/*********************************************************************************************************************************************/

// These are the functions that are used within main to multiply matrices. 

template <typename vector_class> vector_class read_file(vector_class squares, string filename, string dtype)
{
	ifstream file1; 
	std:: string test;

	file1.open(filename);

	while(file1 >> test)
	{
		if(dtype == "int")
		{
			int one = stoi(test);
			squares.push_back(one);

		}
		else if(dtype == "double")
		{
			double one = stod(test);
			squares.push_back(one);

		}
	}
	file1.close();
	return squares;
}

template <typename matrix_shape, typename vector_class, typename row_class, typename column_class> matrix_shape shape_matrix(int M, int L, vector_class squares, row_class row, column_class column)
{
	if(L == 1)
	{
		matrix_shape M1 = 0;
		M1 = new row_class[M];
		int counter = 0; 

		for(int i = 0; i<M; i++)
		{
			M1[i] = new column_class[M];

			for(int j =0; j<M; j++){
				M1[i][j] = squares[counter++];
			}
		}
		return M1;
	}
	else 
	{
		matrix_shape M1 = 0; 
		M1 = new row_class[M];
		int counter = 0; 

		for(int i =0; i<M;i++)
		{
			M1[i] = new column_class[L];

			for(int j=0;j<L;j++){
				M1[i][j] = squares[counter++];
			}
		}
		return M1;
	}
}


template <typename matrix_multiply, typename row_class, typename column_class> matrix_multiply multiply_matrix(matrix_multiply M1, matrix_multiply M2, int M, int L, int T, row_class row, column_class column)
{ 
	if((L == 1) && (T == 1))
	{
		matrix_multiply squares = 0;
		squares = new row_class[M];

		for(int i =0; i<M;i++)
		{
			squares[i] = new column_class[M];
			for(int j=0;j<M;j++)
				squares[i][j]= 0;
		}

		for(int i = 0; i<M;i++)
			for(int j = 0; j<M; j++)
				for(int n = 0; n<M; n++){
					squares[i][j] += M1[i][n]*M2[n][j];
					// cout << "squares3[i][j]=" << " " << squares3[i][j] << endl;
				}
		return squares; 
	}
	else
	{
		matrix_multiply squares = 0; 
		squares = new row_class[M];

		for(int i = 0; i<M; i++)
		{
			squares[i] = new column_class[L];
			for(int j=0;j<L;j++){
				squares[i][j]= 0;
			}
		}
		
		for(int i = 0; i<M;i++)
			for(int j = 0; j<L; j++)
				for(int n = 0; n<T; n++){
					squares[i][j] += M1[i][n]*M2[n][j];
					// cout << "squares3[i][j]=" << " " << squares3[i][j] << endl;
				}

		return squares; 
	}
}

template <typename matrix_class> int print_matrix(int M, int L, matrix_class matrix, string filename){

	ofstream file3; 

	file3.open(filename);

	if(!file3.is_open())
	{
		cout << "ERROR_FOUR: cannot write to file" << endl;
		return ERROR_FOUR; 
	}

	if(L == 1){
		for(int i = 0; i < M; i++)
		{
			for(int j=0;j<M;j++)
				file3 << matrix[i][j] << " ";
			file3 << endl;
		}

	}
	else 
	{
		for(int i = 0; i < M; i++){
			for(int j=0;j<L;j++)
				file3 << matrix[i][j] << " ";
			file3 << endl;
	}

	file3.close();
	}
}