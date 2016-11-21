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
#include <set>


typedef std::unordered_multimap<std::string, std::string> single_dict;
typedef std::unordered_map<int, single_dict> double_dict;
typedef std::string str;
typedef std::vector<std::string> v_string;
typedef v_string::iterator vs_it;
typedef std::set<str> strset;
typedef single_dict::iterator mapIter;

template <typename Iterator>
bool next_combination(const Iterator first, Iterator k, const Iterator last);

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

      while (1) {
        str mystr;
        strset result;
        str temp;
        strset combinations;
        std::vector<str> input;
        getline(std::cin, mystr);
        std::stringstream s(mystr);
        while (s >> temp)
          input.push_back(temp);

        int N = stoi(input[1]);
        if (input[1] == "0")
            break;
        str letter_list = input[0];

        try {
                  single_dict a_dict = the_dict.at(N);
                if ((letter_list.length() - N) > 5) {
                          for (auto& x : a_dict) {
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
                      for (std::size_t i = 1; i <= letter_list.size(); ++i) {
                         do {
                            str comb = str(letter_list.begin(),
                                           letter_list.begin() + i);
                            if (comb.length() == N)
                                combinations.insert(comb);
                         } while (next_combination(letter_list.begin(),
                                                   letter_list.begin() + i,
                                                   letter_list.end()));
                      }

                      for (auto& cit : combinations) {
                        if (a_dict.find(cit) !=
                            a_dict.end()) {
                            std::pair<mapIter, mapIter> keyRange =
                          a_dict.equal_range(cit);
                            for (mapIter s_it = keyRange.first; s_it !=
                                keyRange.second; ++s_it) {
                                str word = (*s_it).second;
                                result.insert((*s_it).second);
                            }
                        }
                      }
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

template <typename Iterator>
bool next_combination(const Iterator first, Iterator k, const Iterator last) {
// Credits: Mark Nelson http://marknelson.us
  if ((first == last) || (first == k) || (last == k))
    return false;
  Iterator i1 = first;
  Iterator i2 = last;
  ++i1;
  if (last == i1)
    return false;
  i1 = last;
  --i1;
  i1 = k;
  --i2;
  while (first != i1) {
    if (*--i1 < *i2) {
       Iterator j = k;
       while (!(*i1 < *j)) ++j;
       std::iter_swap(i1, j);
       ++i1;
       ++j;
       i2 = k;
       std::rotate(i1, j, last);
       while (last != j) {
          ++j;
          ++i2;
       }
       std::rotate(k, i2, last);
       return true;
    }
  }
  std::rotate(first, k, last);
  return false;
}
