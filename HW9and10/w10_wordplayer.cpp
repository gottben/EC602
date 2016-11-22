// Author AlexBennett gottbenn@bu.edu
// Copyright 2016 Alexander Bennett
// Command to compile C++ code: g++ '-std=c++1y' <filename>

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <set>


typedef std::unordered_multimap<std::string, std::string> single_dict;
typedef std::unordered_map<int, single_dict> double_dict;
typedef std::string str;
typedef std::vector<std::string> v_string;
typedef v_string::iterator vs_it;
typedef std::unordered_set<str> strset;
typedef single_dict::iterator mapIter;


int main(int argc, char const *argv[]) {
    std::ifstream infile(argv[1]);
    str content;
    double_dict the_dict;
    v_string the_word;
    while (infile >> content) {
      int N = content.length();
      the_word = {content};
      str sortedWord = content;
      std::sort(sortedWord.begin(), sortedWord.end());
      single_dict d_words;
      if ( the_dict.find(N) == the_dict.end() ) {
          d_words.insert({sortedWord, content});
          the_dict.insert({N, d_words});
      } else if  ( the_dict.at(N).find(sortedWord) == the_dict.at(N).end() ) {
          d_words.insert({sortedWord, content});
          the_dict.at(N).insert(d_words.begin(), d_words.end());
      } else {
          d_words.insert({sortedWord, content});
          the_dict.at(N).insert(d_words.begin(), d_words.end());
      }
    }
    infile.close();

      while (1) {
        str letter_list;
        int N;
        int i, n;
        std::set<str> result;
        strset combinations;
        std::cin >> letter_list >> N;
        std::vector<int> v(letter_list.size(), 0);
        fill(v.begin(), v.begin() + N, 1);
        str c(N, ' ');
        if (N == 0)
          break;

        try {
                  result.clear();
                  single_dict a_dict = the_dict.at(N);
                if (letter_list.length() >  20) {
                          for (auto& x : the_dict.at(N)) {
                          str word = x.first;
                          str n_list = letter_list;
                          for (char& c : word) {
                            if (n_list.find(c) != str::npos) {
                              n_list.erase(n_list.begin()+n_list.find(c));
                              if ((letter_list.length() - N) ==
                                  n_list.length()) {
                                  result.insert(x.second);
                              }
                            } else {
                              break;
                            }
                          }
                      }
                  } else {
                    do {
                      n = 0;
                      for (i = 0; i < v.size(); i++)
                        if (v[i]) {
                          c[n++] = letter_list[i];
                          std::sort(c.begin(), c.end());
                        if (a_dict.find(c) !=
                            a_dict.end()) {
                            std::pair<mapIter, mapIter> keyRange =
                          a_dict.equal_range(c);
                            for (mapIter s_it = keyRange.first; s_it !=
                                keyRange.second; ++s_it) {
                                str word = (*s_it).second;
                                result.insert((*s_it).second);
                            }
                        } }
                    } while (prev_permutation(begin(v), end(v)));
                }

                  for (auto& it : result) {
                    std::cout << it << std::endl;
                  }
                  std::cout << "." << std::endl;
            }
      catch(...) {
                std::cout << "." << std::endl;
            }
      }
}
