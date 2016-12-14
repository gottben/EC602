# README


## Important scripts

There are frour important scripts in this repository.
The first is w14_wordbraincapture.py which contains a solution,
to the wordbrain image processing problem. This problem uses a hard coded
library of letters whose features are used to find which letter is being absorbed into
the library. It fails in two unique cases out of several hundred. Making its accuracy
approximately 99.8 %.

The second is w14_wordbraincapture2.py which has an accuracy of 100% but is not
a very elegant solution. It expects a training set of matrices as an input and then
using some values that were hand-tuned it makes comparisons against the training
set data to guess which letter is being processed at that time.

The third is the training_script.py, this was used to expand on the currently available training sets and produce general forms of each letter in a 3x3, 4x4 and 5x5 matrix. The outputs of this program for each matrix dimensions were then fed into the next program al_finder.py

al_finder.py stands for alphabet finder. This was used to then take the average of each of the alphabets produced by the training_script.py for the different matrix dimensions and create one generic alphabet that would work for a 3x3, 4x4 and 5x5 wordbrain image.




