# basic module

import json
import os


class DataUtil(object):

    def __init__(self):
        self.name = ""
        self.total_round = 4
        self.bonus_len = self.total_round
        self.round_len = 6
        self.ttp = 0
        self.prev_res = []
        self.bonus_list = []
        self.data = [[]]

    def _toAlphabet(self, res_raw : list) -> list:
        res_alp = []
        for i in res_raw:
            if i == 1:
                res_alp.append('T')
            elif i == 2:
                res_alp.append('F')
            else:
                raise ValueError("Round result (int) should be either 1 or 2")
        return res_alp

    def setName(self, name) -> None:
        # self.name = input("Name: ")
        self.name = name
        if self.name.isspace() or not bool(self.name):
            self.name = "Anonymous"
        self.data[0].append(self.name)

    def setBonus(self, bonus_raw) -> None:
        temp = []
        if len(bonus_raw) != self.bonus_len:
            raise IndexError("Bonus list should have exactly %d values" % self.bonus_len)

        # for i in bonus_raw:
        #     if i not in [1.0, 1.2, 1.4, 1.6]:
        #         raise ValueError("Only support: x1.0, x1.2, x1.4, x1.6")
        
        # self.bonus_list = bonus_raw[:]
        
        for i in bonus_raw:
            if i == 0:
                temp.append(1.0)
            elif i == 2:
                temp.append(1.2)
            elif i == 4:
                temp.append(1.4)
            elif i == 6:
                temp.append(1.6)
            else:
                raise ValueError("Only support: 0(x1.0), 2(x1.2), 4(x1.4), 6(x1.6)")

        self.bonus_list = temp
        self.data[0].append(self.bonus_list)

    def prtRes(self, res, ttprb, ttpr, bonus_index) -> None:
        res = self._toAlphabet(res)
        for i in range(self.round_len - 1):
            print(res[i] + "\t", end="")
        print("(i=%s)\t\t(r=%.2f (%.2fx%.2f))\t(t=%.2f)"
              % (res[-1], ttpr, ttprb, self.bonus_list[bonus_index], self.ttp))
    
    def prtInherit(self, res, rep=2) -> None:
        res = self._toAlphabet(res)
        inherit_t = True if res[-1] == "T" else False
        for _ in range(rep):
            for i in range(self.round_len - 1):
                if ((not inherit_t) and (res[i] == "F")) or (inherit_t and (res[i] == "T")):
                    print("^\t", end="")
                else:
                    print(" \t", end="")
            print()

    def firstRound(self, res):
        if len(res) != self.round_len:
            raise IndexError("First round list should have exactly %d values" % self.round_len)
    
    def inheritRound(self, res) -> list:
        res_after = []
        k = 0
        min_len = self.round_len - 1
        for i in range(self.round_len - 1):
            if self.prev_res[i] == self.prev_res[-1]:
                min_len -= 1

        if len(res) < min_len:
            raise IndexError("(Receive) Inherit round list should have at least %d values" % min_len)

        for i in range(self.round_len - 1):
            if self.prev_res[i] == self.prev_res[-1]:
                res_after.append(self.prev_res[i])
            else:
                res_after.append(res[k])
                k += 1
        res_after.append(res[k])

        if len(res_after) != self.round_len:
            raise IndexError("(Return) Inherit round list should have exactly %d values" % self.round_len)

        return res_after
    
    def calcPoint(self, res, bonus_index):
        ttprb = 0
        for i in range(self.round_len - 1):
            if res[i] == 1:
                ttprb += 2 ** (self.round_len - 1 - i)  # 32, 16, 8, 4, 2
        ttpr = ttprb * self.bonus_list[bonus_index]
        self.ttp += ttpr

        return ttprb, ttpr

    def saveData(self, file_path) -> bool:
        if os.path.exists(file_path):
            return False

        with open(file_path, "w") as f:
            f.write(json.dumps(self.data))
        return True
