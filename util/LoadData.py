# this module loads and shows the data from existing json files

import json
import os

from util.DataUtil import DataUtil


class LoadData(DataUtil):

    def __init__(self):
        super(LoadData, self).__init__()
        self.res = []

    def loadJson(self, path):
        with open(path, 'rb') as f:
            data = json.load(f)
            # data = json.loads(f.read())
        self.name = data[0][0]
        self.bonus_list = data[0][1]
        for i in range(1, len(data)):
            self.res.append(data[i])
        
    def main(self, file_path):
        self.loadJson(file_path)

        print("Name:", self.name)
        print("Bonus:", self.bonus_list, end="\n\n")

        for i in range(len(self.res)):
            ttprb, ttpr = self.calcPoint(self.res[i], i)

            self.prtRes(self.res[i], ttprb, ttpr, i)
            if i != self.total_round - 1:
                self.prtInherit(self.res[i])
        print("\n\n")
