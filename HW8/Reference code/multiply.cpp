
typedef vector< vector<int> > int_matrix;

int_matrix multply(const & int_matrix A,const & int_matrix B){

 int M = A.size()
 int K = A[0].size()
 int L = B[0].size()

 int_matrix c(M,L);
 
 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int n=0;n<N;n++)
            c[i][j] = A[i][n]*B[n][j]


}

