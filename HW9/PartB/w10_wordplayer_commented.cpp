#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <map>
#include <set>
#include <chrono>
#include <algorithm>

// Copyright 2016 Brian Appleton


//basic unorderd set structure
std::unordered_set<std::string> dict;

//Advanced set structure

std::unordered_map<int,std::map<std::string,std::unordered_set<std::string>>> ds;

void read_wordlist(std::string filename);
void print_wordlist();
void parse_input(std::string &buffer, std::string &letters, int &n);
bool possible(std::string letters, std::string word, int N);
std::unordered_set<std::string> get_combos(std::string letters, int r);

int main(int argc, char const *argv[]) {
    read_wordlist(argv[1]);
    
    std::string buffer;
    std::string letters;
    std::string number;
    int n,r;
    std::set<std::string> word_list;
    std::unordered_set<std::string> combos;

    std::chrono::high_resolution_clock::time_point st = std::chrono::high_resolution_clock::now();

    while(1) {
        word_list.clear();
        std::cin >> letters >> r;
        if (r == 0) {
            break;
        }
        n = letters.length();
        
        //Make algorithm selection
        if(n > 20) {
            if(ds.find(r) != ds.end()) {
                //If the key exists in the unordered map
                for (auto letter_key : ds[r]) {
                    //For each key of n letters, check whether it can be spelled using the given string of letters.
                    if(possible(letters, letter_key.first, r)) {
                        //std::cout << "Letter key " << letter_key.first << " is possible." << std::endl;
                        word_list.insert(letter_key.second.begin(), letter_key.second.end());
                    }
                }
            }
        }
        else {
            if(ds.find(r) != ds.end()) {
                combos = get_combos(letters, r);
                for(auto letter_key : combos) {
                    std::sort(letter_key.begin(), letter_key.end());
                    if(ds[r].find(letter_key) != ds[r].end()) {
                        //std::cout << "Letter key " << letter_key << " found in ds at r = " << r << std::endl;
                        //for(auto word : ds[r][letter_key]) {
                            //std::cout << word << " " << std::endl;
                        //}
                        word_list.insert(ds[r][letter_key].begin(), ds[r][letter_key].end());
                    }
                }
           }
        }
        //Print the word list.
        for (auto const& word : word_list) {
            std::cout << word << std::endl;
        }
        std::cout << "." << std::endl;
    }

    std::chrono::high_resolution_clock::time_point end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>( end - st ).count();
    std::cout << duration << " ms." << std::endl;


    return 0;
}


std::unordered_set<std::string> get_combos(std::string letters, int r) {

 int i, n;
 std::vector<int> v(letters.size(), 0);
 fill(v.begin(), v.begin() + r, 1);
 std::string c(r, ' ');
 std::unordered_set<std::string> thecombs;
 do {
  n = 0;
  for (i = 0; i < v.size(); i++)
    if (v[i])
      c[n++] = letters[i];
 if (thecombs.find(c) != thecombs.end())
   continue;
 thecombs.insert(c);
 //std::cout << c << std::endl; // do something
 } while (prev_permutation(begin(v), end(v)));

 return thecombs;
}

void read_wordlist(std::string filename) {
    std::ifstream fin;
    std::string word;
    fin.open(filename);
    /* Read into basic unordered set of words
    while(fin >> word) {
        dict.insert(word);
    }
    */
    int n;
    std::string letter_key;
    while(fin >> word) {
        n = word.length();
        letter_key = word;
        std::sort(letter_key.begin(), letter_key.end()); 
        ds[n][letter_key].insert(word);
    }
    fin.close();
}

void print_wordlist() {
    
    for(auto const& n : ds) {
        for(auto const& letter_key : n.second) {
            for(auto const& word : letter_key.second) {
                std::cout << word << std::endl;
            }
        }
    }
}

bool possible(std::string letters, std::string word, int N) {
    int pos;
    //std::cout << word.length() << std::endl;
    if (word.length() != N) {
        return false;
    }
    for (auto letter : word) {
        //std::cout << "Letter is : " << letter << std::endl;
        pos = letters.find_first_of(letter);
        //std::cout << "Position of this letter is: " << pos << std::endl;
        if(pos == -1) {
            return false; 
        }
        else {
            letters.erase(pos, 1);
        }
    }
    return true;
}

void parse_input(std::string &buffer, std::string &letters, int &n) {
    std::cout << "here" << std::endl;
    short i = 0;
    for (auto character : buffer) {
        if(isdigit(character)) {
            std::cout << "Found number " << character << " at position " << i << std::endl;
            std::cout << "Converting " << buffer.substr(i,std::string::npos).c_str() << " to an interger." << std::endl;
            //n = atoi(buffer.substr(i,std::string::npos).c_str());
            //buffer.erase(i, std::string::npos);
        }
        if(character == ' ') {
            buffer.erase(i, 1);
        }
        i++;
    }
    letters = buffer;
}


