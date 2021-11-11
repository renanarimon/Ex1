from Assignments.Ex1.Building import Building
from Assignments.Ex1.Elevator import Elevator
from Assignments.Ex1.CallForElevator import CallForElevator


class MyAlgo:
    def __init__(self, building: Building, allCalls: list):
        self.building = building
        self.allCalls = allCalls


    def MyAllocte(self):
        while len(self.allCalls) > 0:
            c1 = self.allCalls.pop(0)
            bestElev = self.elevs[0]


    def timePerSec(self, newCall: CallForElevator, elev: Elevator):
        newCallTime = newCall.time()
        elevStartTime = elev.setStartTime
        passedSecs = newCallTime - elevStartTime
        currFloor = list(elev.floors)[0]

        # while passedSecs > 0:
        for f1 in elev.floors:
            tmpT = self.timeTo(elev, currFloor, f1)
            if (tmpT < passedSecs):
                passedSecs = passedSecs - (tmpT + elev.holdTime)
                currFloor = f1
            else:
                break
        finalFloor = currFloor + (passedSecs/elev.speed)
        return finalFloor

    def timeTo(self, elev: Elevator, src, dest):
        diff = abs(dest - src)
        return diff / elev.speed