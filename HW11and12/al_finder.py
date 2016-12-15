import numpy as np


the_d = {4: {"K": [59.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0],
             "W": [64.0, 121.0, 169.0, 169.0, 169.0, 144.0, 64.0, 25.0],
             "F": [167.0, 38.0, 9.0, 36.0, 121.0, 9.0, 9.0, 9.0],
             "U": [42.0, 49.0, 49.0, 49.0, 49.0, 49.0, 100.0, 112.0],
             "Z": [169.0, 42.0, 9.0, 16.0, 16.0, 16.0, 25.0, 169.0],
             "Y": [64.0, 64.0, 64.0, 36.0, 9.0, 9.0, 9.0, 9.0],
             "N": [25.0, 64.0, 105.0, 126.0, 143.0, 121.0, 81.0, 36.0],
             "R": [159.0, 100.0, 49.0, 90.0, 147.0, 49.0, 56.0, 60.0],
             "M": [9.0, 49.0, 100.0, 169.0, 196.0, 196.0, 144.0, 100.0],
             "X": [81.0, 81.0, 64.0, 36.0, 36.0, 64.0, 64.0, 64.0],
             "T": [195.0, 42.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
             "D": [143.0, 121.0, 64.0, 49.0, 49.0, 63.0, 100.0, 169.0],
             "V": [50.0, 64.0, 64.0, 64.0, 49.0, 49.0, 25.0, 4.0],
             "B": [115.0, 85.0, 49.0, 81.0, 100.0, 49.0, 76.0, 144.0],
             "S": [64.0, 64.0, 12.0, 36.0, 49.0, 16.0, 25.0, 121.0],
             "O": [81.0, 169.0, 64.0, 49.0, 49.0, 64.0, 121.0, 169.0],
             "C": [81.0, 121.0, 16.0, 16.0, 16.0, 16.0, 64.0, 169.0],
             "E": [167.0, 45.0, 9.0, 80.0, 80.0, 9.0, 25.0, 169.0],
             "A": [3.0, 16.0, 36.0, 49.0, 49.0, 116.0, 196.0, 49.0],
             "P": [117.0, 94.0, 49.0, 78.0, 136.0, 17.0, 9.0, 9.0],
             "J": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 16.0, 64.0],
             "Q": [169.0, 196.0, 100.0, 81.0, 121.0, 289.0, 64.0, 25.0],
             "H": [45.0, 49.0, 49.0, 189.0, 195.0, 49.0, 49.0, 49.0],
             "I": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
             "G": [81.0, 121.0, 16.0, 16.0, 64.0, 81.0, 99.0, 169.0],
             "L": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 22.0, 131.0]},
         3: {"Y": [64.0, 64.0, 64.0, 36.0, 9.0, 9.0, 9.0, 9.0],
             "G": [81.0, 121.0, 16.0, 16.0, 81.0, 81.0, 121.0, 169.0],
             "B": [120.0, 97.0, 49.0, 97.0, 100.0, 49.0, 92.0, 144.0],
             "N": [25.0, 64.0, 121.0, 144.0, 144.0, 121.0, 81.0, 36.0],
             "P": [115.0, 85.0, 49.0, 68.0, 144.0, 22.0, 9.0, 9.0],
             "J": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 36.0, 64.0],
             "M": [14.0, 49.0, 121.0, 196.0, 196.0, 196.0, 144.0, 100.0],
             "I": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
             "X": [64.0, 64.0, 64.0, 36.0, 25.0, 64.0, 64.0, 64.0],
             "A": [4.0, 16.0, 49.0, 49.0, 49.0, 134.0, 169.0, 49.0],
             "F": [164.0, 36.0, 9.0, 44.0, 121.0, 10.0, 9.0, 9.0],
             "D": [144.0, 121.0, 50.0, 49.0, 49.0, 50.0, 69.0, 166.0],
             "V": [64.0, 64.0, 64.0, 64.0, 64.0, 49.0, 16.0, 4.0],
             "T": [178.0, 49.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
             "K": [64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 70.0, 64.0],
             "H": [49.0, 49.0, 49.0, 160.0, 209.0, 49.0, 49.0, 49.0],
             "L": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 32.0, 141.0],
             "W": [64.0, 121.0, 169.0, 196.0, 196.0, 144.0, 64.0, 25.0],
             "S": [64.0, 64.0, 16.0, 36.0, 49.0, 16.0, 36.0, 121.0],
             "Q": [169.0, 196.0, 100.0, 81.0, 121.0, 289.0, 64.0, 25.0],
             "E": [155.0, 36.0, 9.0, 71.0, 87.0, 9.0, 21.0, 155.0],
             "O": [81.0, 169.0, 72.0, 49.0, 49.0, 64.0, 144.0, 144.0],
             "R": [161.0, 100.0, 49.0, 89.0, 144.0, 59.0, 59.0, 59.0],
             "C": [100.0, 121.0, 16.0, 16.0, 16.0, 16.0, 83.0, 144.0],
             "U": [49.0, 49.0, 49.0, 49.0, 49.0, 64.0, 121.0, 95.0]},
         5: {"A": [3.0, 16.0, 36.0, 49.0, 49.0, 86.0, 196.0, 49.0],
             "C": [87.0, 113.0, 16.0, 15.0, 15.0, 16.0, 48.0, 169.0],
             "L": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 11.0, 121.0],
             "B": [111.0, 81.0, 49.0, 81.0, 101.0, 49.0, 59.0, 144.0],
             "G": [80.0, 121.0, 16.0, 15.0, 63.0, 81.0, 78.0, 181.0],
             "S": [66.0, 53.0, 9.0, 35.0, 49.0, 16.0, 24.0, 121.0],
             "K": [59.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0],
             "P": [118.0, 82.0, 45.0, 64.0, 126.0, 21.0, 9.0, 9.0],
             "J": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 16.0, 64.0],
             "N": [24.0, 63.0, 100.0, 121.0, 121.0, 121.0, 80.0, 36.0],
             "D": [142.0, 110.0, 49.0, 49.0, 49.0, 49.0, 79.0, 169.0],
             "V": [49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 25.0, 4.0],
             "E": [145.0, 43.0, 9.0, 64.0, 97.0, 9.0, 13.0, 145.0],
             "F": [144.0, 37.0, 9.0, 25.0, 121.0, 9.0, 9.0, 9.0],
             "M": [9.0, 42.0, 100.0, 169.0, 169.0, 176.0, 144.0, 100.0],
             "H": [39.0, 39.0, 39.0, 155.0, 190.0, 39.0, 39.0, 39.0],
             "R": [144.0, 97.0, 42.0, 70.0, 144.0, 49.0, 49.0, 49.0],
             "X": [64.0, 64.0, 64.0, 36.0, 25.0, 64.0, 64.0, 64.0],
             "T": [169.0, 41.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
             "U": [49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 81.0, 121.0],
             "O": [77.0, 168.0, 64.0, 49.0, 49.0, 49.0, 90.0, 169.0],
             "Y": [64.0, 64.0, 64.0, 36.0, 9.0, 9.0, 9.0, 9.0],
             "W": [56.0, 121.0, 148.0, 169.0, 169.0, 144.0, 77.0, 25.0],
             "I": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0]}}

alphabet = {}
for key, value in the_d[4].items():
    if (key not in the_d[3]) and key in the_d[5]:
        alphabet[key] = (np.array(the_d[5][key]) + np.array(value)) // 2
    elif (key not in the_d[5]) and (key in the_d[3]):
        alphabet[key] = (np.array(the_d[3][key]) + np.array(value)) // 2
    elif (key not in the_d[5]) and (key not in the_d[3]):
        alphabet[key] = np.array(value)
    else:
        alphabet[key] = (np.array(the_d[4][key]) +
                         np.array(the_d[5][key]) + np.array(value)) // 3

for key, value in alphabet.items():
    print('"' + key + '"', ":", value.tolist(), ",")
