// Copyright J Carruthers 2016
// This code was adapted from code on stack overflow
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <iostream>
int main() {
 std::string s;
 int K;
 int i, n;
 std::cin >> s >> K;
std::vector<int> v(s.size(), 0);
 fill(v.begin(), v.begin() + K, 1);
 std::string c(K, ' ');
std::unordered_set<std::string> thecombs;
do {
 n = 0;
 for (i = 0; i < v.size(); i++)
 if (v[i])
 c[n++] = s[i];
if (thecombs.find(c) != thecombs.end())
 continue;
 thecombs.insert(c);
std::cout << c << std::endl; // do something with the combination here.
 } while (prev_permutation(begin(v), end(v)));
}
