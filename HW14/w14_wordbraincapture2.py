#   Pseudo Code Template
#   use any libraries in the anaconda library
#   1st step read in the image

from os import listdir
from skimage.io import imread
import numpy as np
import json


the_alphabet = {"R": [33.0, 9.0, 25.0, 10.0, 9.0],
                "U": [9.0, 9.0, 9.0, 11.0, 25.0],
                "T": [27.0, 1.0, 1.0, 1.0, 1.0],
                "J": [1.0, 1.0, 1.0, 1.0, 9.0],
                "C": [25.0, 4.0, 3.0, 4.0, 28.0],
                "F": [25.0, 1.0, 16.0, 3.0, 1.0],
                "D": [35.0, 12.0, 9.0, 10.0, 36.0],
                "N": [8.0, 24.0, 31.0, 25.0, 9.0],
                "M": [4.0, 24.0, 41.0, 40.0, 25.0],
                "H": [9.0, 9.0, 49.0, 9.0, 9.0],
                "V": [9.0, 11.0, 11.0, 9.0, 1.0],
                "A": [1.0, 9.0, 9.0, 28.0, 16.0],
                "L": [1.0, 1.0, 1.0, 1.0, 16.0],
                "K": [14.0, 16.0, 16.0, 16.0, 16.0],
                "Q": [49.0, 25.0, 25.0, 49.0, 4.0],
                "Y": [16.0, 16.0, 4.0, 1.0, 1.0],
                "E": [25.0, 1.0, 23.0, 1.0, 22.0],
                "B": [25.0, 9.0, 25.0, 9.0, 25.0],
                "O": [25.0, 16.0, 9.0, 16.0, 35.0],
                "S": [16.0, 4.0, 9.0, 4.0, 19.0],
                "W": [16.0, 36.0, 40.0, 25.0, 5.0],
                "I": [1.0, 1.0, 1.0, 1.0, 1.0],
                "P": [25.0, 9.0, 25.0, 4.0, 1.0],
                "G": [25.0, 4.0, 9.0, 16.0, 36.0],
                "X": [16.0, 16.0, 4.0, 16.0, 16.0]}
train_dict = {3: {"train3_1.png": ["EDI", "NBL", "RAS"],
                  "train3_2.png": ["HIF", "SSK", "SOC"],
                  "train3_3.png": ["FSI", "YLC", "ELK"],
                  "train3_4.png": ["JAA", "NEP", "FTL"],
                  "train3_5.png": ["BAR", "XRB", "EOL"],
                  "train3_6.png": ["HOS", "EQU", "ERA"],
                  "train3_7.png": ["TAI", "JSR", "USG"],
                  "train3_8.png": ["NWL", "LOE", "MEL"],
                  "train3_9.png": ["SHO", "DGV", "OLE"],
                  "zuzzle28.png": ['PAK', 'NOS', 'EFI'],
                  "zuzzle29.png": ['ETL', 'OKC', 'RDO'],
                  "zuzzle31.png": ['KLI', 'BAM', 'DRE'],
                  "zuzzle32.png": ['LSR', 'TLA', 'WBE'],
                  "zuzzle33.png": ['HTL', 'AUO', 'PMS'],
                  "zuzzle34.png": ['DIE', 'TAC', 'REH'],
                  "zuzzle35.png": ['HSA', 'EIR', 'DBF']},
              4: {"train4_1.png": ["EGEL", "AAEG", "TVMN", "IEAR"],
                  "train4_2.png": ["BEOT", "TXIA", "LFRH", "EFES"],
                  "train4_3.png": ["YEHO", "SLNL", "ONCA", "NNAB"],
                  "train4_4.png": ["EOCA", "WPLT", "CIMK", "USEL"],
                  "train4_5.png": ["UNOD", "LEOS", "LBRL", "SMAL"],
                  "train4_6.png": ["TOFR", "NPOI", "YPMJ", "TUME"],
                  "train4_7.png": ["BIKA", "TTNR", "EEZU", "NLZP"],
                  "z10.png": ['TNOB', 'ANCO', 'BXET', 'MAIL'],
                  "z11.png": ['FOKI', 'RKET', 'NATA', 'PETS'],
                  "z12.png": ['CRHE', 'KAED', 'RLEO', 'SSLC'],
                  "z13.png": ['KURT', 'ONCE', 'SRTK', 'GHOT'],
                  "z14.png": ['EGAI', 'LCEL', 'KPEN', 'THIN'],
                  "z15.png": ['NIBA', 'CAPT', 'HAOS', 'NWMN'],
                  "z16.png": ['CIUM', 'EISP', 'TOLU', 'HCTN'],
                  "z5.png": ['BIRT', 'HDYI', 'YATN', 'INFI'],
                  "z6.png": ['RMLP', 'KEAO', 'PNRB', 'DEID'],
                  "z7.png": ['TRAU', 'ELER', 'RODH', 'RECR'],
                  "z8.png": ['LECL', 'UKLU', 'KBOF', 'SROL'],
                  "z9.png": ['OPEA', 'NOOC', 'LNCC', 'TUOO'],
                  "zuzzle1.png": ['BALT', 'ELAT', 'OPAH', 'MBOR'],
                  "zuzzle17.png": ['NEIK', 'TNAP', 'PGMM', 'UGGE'],
                  "zuzzle18.png": ['YARS', 'DPPE', 'OIRE', 'LADM'],
                  "zuzzle19.png": ['ELBA', 'RRSE', 'DEOP', 'TAFV'],
                  "zuzzle2.png": ['PITE', 'NEAA', 'TCHP', 'NAIL'],
                  "zuzzle20.png": ['STRI', 'PEMI', 'XNOH', 'EYBC'],
                  "zuzzle21.png": ['PIET', 'KAES', 'WYTE', 'ARKS'],
                  "zuzzle22.png": ['GEBS', 'AACB', 'DAIR', 'ETAP'],
                  "zuzzle23.png": ['SREI', 'TLPL', 'ETIP', 'SNMI'],
                  "zuzzle24.png": ['OLAM', 'ILEW', 'RICC', 'AHDI'],
                  "zuzzle25.png": ['FROS', 'TSIH', 'ILEV', 'ODLE'],
                  "zuzzle26.png": ['FRAR', 'PYOC', 'PTCS', 'HAEK'],
                  "zuzzle3.png": ['ELEV', 'ROTA', 'BKDU', 'CRCA']},
              5: {"train5_1.png": ["STRTB", "IMOHA", "ORANP",
                                   "SKAEP", "HCTAF"],
                  "train5_2.png": ["OKSRA", "EMFCI", "ATAON",
                                   "NOLOG", "PPILL"],
                  "train5_3.png": ["ALEBU", "LFRNM", "ALMLA",
                                   "BLSAE", "HOUSE"],
                  "train5_4.png": ["DLEIF", "BWOOW", "HODRC",
                                   "REBEO", "LLSRO"],
                  "train5_5.png": ["HTROO", "YHPNY", "SEGIE",
                                   "GNLOA", "GNOLB"],
                  "train5_6.png": ["KHPDO", "OIOWO", "ELLKU",
                                   "PEACB", "RETNI"],
                  "train5_7.png": ["SLBOP", "SIOKP", "ERLEG",
                                   "GEIAS", "FRUCT"],
                  "train5_8.png": ["GHNEF", "SCVLA", "EEONB",
                                   "LLARD", "TIMBE"],
                  "train5_9.png": ["TEGDE", "KJRTU", "NOUGI",
                                   "KETIN", "YRINF"],
                  "train5_10.png": ["RSPLS", "EEPIT", "LOREL",
                                    "DIUPE", "BOLIV"],
                  "train5_11.png": ["WIGBB", "EGANA", "TNRCP",
                                    "EECEC", "NAKLE"],
                  "train5_12.png": ["VITTM", "APOSI", "NVAMI",
                                    "MEREP", "OORDB"],
                  "train5_13.png": ["EROST", "ATCHO", "KSHTM",
                                    "EPEED", "HATCH"],
                  "train5_14.png": ["NANAO", "NAOBS", "EBROA",
                                    "DBEOR", "TLDSW"],
                  "zuzzle27.png": ['STRTB', 'IMOHA', 'ORANP', 'SKAEP', 'HCTAF'],
                  "zuzzle30.png": ['EANOP', 'NINKP', 'SOCAO', 'TIRIN', 'YSGOP'],
                  "zuzzle36.png": ['BIEDU', 'NITTS', 'ULUOM', 'RRSAE', 'RSEUG'],
                  "zuzzle37.png": ['PLLBU', 'ETURS', 'SPTLE', 'OCNPT', 'CYEIA'],
                  "zuzzle40.png": ['XOVOG', 'FABOL', 'LDLOB', 'GTBOO', 'AKOBL']}
              }

total_dict = {}

directory = "./train_files"
dog = listdir(directory)
dog.sort()
for file in dog:
    if file.endswith(".png"):
        img = 255 - imread(directory + "/" + file)
        index = np.where(img[568:1907] == 0)
        if index[1][0] == 387:
            row = 416         # row changing width
            colu = 350        # column changing width
            r_w = 46          # white space row width
            c_w = 112       # white space column width
            rc = 415          # Row constant dimension
            cc = 345          # Column constant dimension
            N = 3               # array size
            M1 = 387
            M2 = 1660
            D = 120
            F = 2
        elif index[1][0] == 358:
            N = 4
            M1 = 353
            M2 = 1710
            cc = 302
            rc = 293
            r_w = 44
            c_w = 39
            row = 304
            colu = 308
            F = 2
            D = 120
        elif index[1][0] == 348:
            N = 5
            M1 = 348
            M2 = 1800
            cc = 230
            rc = 230
            r_w = 50
            c_w = 50
            row = 228
            colu = 228
            F = 2
            D = 130

        data = img[569:1910, M1:M2]
        data[data < 170] = 0
        data[data > 0] = 255
        the_matrix = []
        for j in range(0, N):
            for i in range(0, N):
                letter = data[i * (row + r_w):rc + i * (row + r_w),
                              j * (colu + c_w): cc + j * (colu + c_w)]
                indices = np.where(letter == [255, 255, 255])
                letter = letter[np.min(indices[0]): np.max(indices[0]),
                                np.min(indices[1]): np.max(indices[1])]
                pix_c = np.array([])
                for t in range(0, F*N):
                    R = letter[t * (len(letter) // (F*N)):
                               (t + 1) * (len(letter) // (F*N))]
                    L = np.count_nonzero(R) // (N * D)
                    pix_c = np.append(pix_c, L)
                pix_c = pix_c ** 2
                if "train" in file:
                    if N not in total_dict:
                        total_dict[N] = {train_dict[N][file][j][i]: pix_c}
                    elif (train_dict[N][file][j][i] not
                          in total_dict[N]):
                        total_dict[N].update(
                            {train_dict[N][file][j][i]: pix_c})
                    else:
                        total_dict[N][train_dict[N][file][j][i]] = ((
                            (total_dict[N][train_dict[N][file][j][i]] + pix_c)
                            // 2))
                    the_matrix = the_matrix + [train_dict[N][file][j][i]]
                else:
                    keys = []
                    values = []
                    for key, value in total_dict[N].items():
                        keys += [key]
                        values += [np.sqrt((value - pix_c)**2).mean()]
                    the_matrix += keys[values.index(min(values))]
        rm = []
        for i in range(0, N):
            rm += [''.join(the_matrix[i * N: (i + 1) * N])]
        result = {}
        result["lengths"] = []
        result["grid"] = rm
        result["size"] = N
        print('"', file, '"', ":", rm)
# for key, value in total_dict[N].items():
#     print('"' + key + '"', ":", value.tolist(), ",")
