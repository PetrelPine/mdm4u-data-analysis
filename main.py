# MDM 4U Probability Game
# 2021-11-04
# Eric Gao 978840 AHSS

"""
Calculated E(x) = 161.2

Use RandomData module to calculate the approximate expected value:
Data size: 1000000

Result_01: 161.1783128001206
Result_02: 161.33128040012448
Result_03: 161.3134896001158
Result_04: 161.29312400011932
Result_05: 161.0602104001173
Result_06: 161.06291480011572
Result_07: 161.1694432001145
Result_08: 161.23023760011637
Result_09: 161.24542520012074
Result_10: 161.11072160011943
Result_11: 161.22849440011842
Result_12: 161.40855400011435
Result_13: 161.22930640011015
Result_14: 161.27300480011738
Result_15: 161.1220168001212
Result_16: 161.1758652001168
Result_17: 161.0400352001081
Result_18: 161.1274452001261
Result_19: 161.3181812001209
Result_20: 161.05868120012028

Sum of 20 results: 3223.97674400235794
Average of 20 results: 161.198837200117897 ~= 161.2
"""

import os


# create necessary folders
if not os.path.exists("_auto_generate"):
    os.mkdir("_auto_generate")
if not os.path.exists("_collected_data"):
    os.mkdir("_collected_data")


def fcollectdata():  # collect players' data
    from util.CollectData import CollectData

    collectdata = CollectData()
    collectdata.main()


def floaddata():  # load and show existing data
    from util.LoadData import LoadData
    
    dir_ = "_collected_data"
    for file_name in os.listdir(dir_):
        file_path = dir_ + "/" + file_name
        loaddata = LoadData()
        loaddata.main(file_path)


def frandomdata():  # create random data
    from util.RandomData import RandomData
    
    # data_size = 1000000
    data_size = 20
    ttp = 0  # total point

    for t in range(data_size):
        randomdata = RandomData()
        ttp_each = randomdata.main(saveDt=True)
        ttp += ttp_each

    # print(ttp / data_size)


def fexceldata():  # load and write existing data into excel
    from util.ExcelData import ExcelData

    exceldata = ExcelData()
    exceldata.main("_collected_data")


# fcollectdata()
# floaddata()
# frandomdata()
# fexceldata()
