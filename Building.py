import json
from Elevator import Elevator


class Building:

    def __init__(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                self.minFloor = my_d["_minFloor"]
                self.maxFloor = my_d["_maxFloor"]
                self.elevators = []
                self.load_json(file_name)
        except IOError as e:
            print(e)

    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                elevs_list = my_d["_elevators"]
                for elev_dict in elevs_list:
                    elev = Elevator(**elev_dict)
                    self.elevators.append(elev)

        except IOError as e:
            print(e)

    def toString(self):
        st = "minFloor = {} maxFloor = {} ".format(self.minFloor, self.maxFloor)
        st += "elevators = {"
        for elev in self.elevators:
            st += elev.toString()
        return st + "}"
