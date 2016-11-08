#Compile
g++ -std=c++14 w8c_multiply.cpp -o w8c_multiply

#Run
#./w8c_multiply int 3 3 5 matrix1.txt matrix2.txt matrix3.txt
./w8c_multiply double 0 3 5 matrix1.txt matrix2.txt matrix3.txt

#Print return code
echo "return code: " $?
