# this module collects data from players

from util.DataUtil import DataUtil


class CollectData(DataUtil):
    def __init__(self):
        super(CollectData, self).__init__()

    def main(self):
        self.setName(input("Name: "))

        print("Bonus: ", end="")
        self.setBonus([int(x) for x in input().split(" ") if x.isnumeric()])

        for i in range(self.total_round):
            # print("Round %d/%d: " % (i + 1, self.total_round))
            if i == 0:
                print(f"Round {i+1} ({self.round_len}): ", end="")
                res = [int(x) for x in input().split(" ") if x.isnumeric()]
                self.firstRound(res)
            else:
                input_num = self.round_len
                for j in range(self.round_len - 1):
                    if self.prev_res[j] == self.prev_res[-1]:
                        input_num -= 1
                print(f"Round {i+1} ({input_num}): ", end="")
                res_raw = [int(x) for x in input().split(" ") if x.isnumeric()]
                res = self.inheritRound(res_raw)

            self.prev_res = res
            self.data.append(res)

            ttprb, ttpr = self.calcPoint(res, i)

            self.prtRes(res, ttprb, ttpr, i)
            if i != self.total_round - 1:
                self.prtInherit(res)
        
        file_num = 1
        while True:
            if not self.saveData(f"_collected_data/{self.name}-{file_num}.json"):
                file_num += 1
            else:
                break
