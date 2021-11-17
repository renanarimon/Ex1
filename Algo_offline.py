from math import ceil
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator


class Algo_offline:
    def __init__(self, building: Building, allCalls: list):
        self.building = building
        self.allCalls = allCalls
        self.dict = {}

    """
    allocate an elevator for each call.
    Each elevator receives a number of calls according to its speed.
    For example: Elevator 0 with speed 5 receives 5 calls and so on.
    """

    def allocate(self):
        while len(self.allCalls) > 0:
            for elev in self.building.elevators:
                for i in range(ceil(elev.speed)):
                    if i < len(self.allCalls):
                        if self.allCalls[i].src < self.building.minFloor or self.allCalls[
                            i].src > self.building.maxFloor or self.allCalls[i].dest > self.building.maxFloor or \
                                self.allCalls[i].dest < self.building.minFloor:
                            self.allCalls.remove(self.allCalls[i])
                        else:
                            self.allCalls[i].allocatedTo = elev.id
                            self.dict.update({self.allCalls[i]: elev.id})
                            self.allCalls.remove(self.allCalls[i])
