# this module generats random data

import random

from util.DataUtil import DataUtil


class RandomData(DataUtil):

    def __init__(self):
        super(RandomData, self).__init__()
        self.name = "AutoGenerate"
        self.bonus_list = [1, 1.2, 1.4, 1.6]

    def firstRound(self) -> list:
        res = []
        for _ in range(self.round_len):
            res.append(random.randint(1, 2))

        return res

    def inheritRound(self) -> list:
        res = []

        for i in range(self.round_len - 1):
            if self.prev_res[i] == self.prev_res[-1]:
                res.append(self.prev_res[i])
            else:
                res.append(random.randint(1, 2))
        res.append(res[-1])

        return res
    
    def main(self, printRes=False, saveDt=False) -> float:
        self.data[0].append(self.name)
        random.shuffle(self.bonus_list)
        self.data[0].append(self.bonus_list)

        for i in range(self.total_round):
            if i == 0:
                res = self.firstRound()
            else:
                res = self.inheritRound()

            self.prev_res = res
            self.data.append(res)

            ttprb, ttpr = self.calcPoint(res, i)

            if printRes:
                self.prtRes(res, ttprb, ttpr, i)
                if i != self.total_round - 1:
                    self.prtInherit(res)
        
        if saveDt:
            path_num = 1
            path = "_auto_generate/%d.json" % path_num
            while True:
                if not self.saveData(path):
                    path_num += 1
                    path = "_auto_generate/%d.json" % path_num
                else:
                    break

        return self.ttp
