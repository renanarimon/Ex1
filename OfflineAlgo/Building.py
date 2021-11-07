import json
from Assignments.Ex1.OfflineAlgo.Elevator import Elevator


class Building:

    def __init__(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                self.minFloor = my_d["_minFloor"]
                self.maxFloor = my_d["_maxFloor"]
                self.elevators = {}
                self.load_json(file_name)
        except IOError as e:
            print(e)

    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                elevs_list = my_d["_elevators"]
                for i in range(len(elevs_list)):
                    elev_dic = elevs_list[i]
                    # for k, v in elev_dic.items():
                    elev = Elevator(**elev_dic)
                    self.elevators[elev.id] = elev

        except IOError as e:
            print(e)
