import sys

from Assignments.Ex1.Building import Building
from Assignments.Ex1.Elevator import Elevator
from Assignments.Ex1.CallForElevator import CallForElevator


class MyAlgo:
    def __init__(self, building: Building, allCalls: list):
        self.building = building
        self.allCalls = allCalls
        self.dict = {}

    def MyAllocte(self):
        for c in self.allCalls:
            bestElev = self.building.elevators[0]
            bestTime = sys.maxsize
            for elev in self.building.elevators:
                if len(elev.floors) == 0:
                    tmpTime = self.timeTo(elev, elev.pos, c.src)
                    if tmpTime < bestTime:
                        bestElev = elev
                        break

                pos = self.PosPerSec(c, elev)
                if c.dir == elev.dir:
                    if c.dir == 1:
                        if c.src >= pos:
                            bestElev = elev
                            break
                    elif c.dir == -1:
                        if c.dir <= pos:
                            bestElev = elev
                            break
                else:
                    lastFloor = list(elev.floors)[-1]
                    tmpTime = elev.calcSet() + self.timeTo(elev, lastFloor, c.src)
                    if tmpTime < bestTime:
                        bestTime = tmpTime
                        bestElev = elev
            c.allocatedTo = bestElev.id
            # st = "{},{},{},{},{},{}".format(c.name, c.time, c.src,
            #                                 c.dest, c.state,
            #                                 c.allocatedTo)
            # self.dict.update({st: bestElev.id})
            self.dict.update({c: bestElev.id})

            bestElev.floors.add(c.src)
            bestElev.floors.add(c.dest)
            bestElev.dir = c.dir
            bestElev.pos = self.PosPerSec(c, bestElev)
        return "done"

    ## calc the elevator curr floor by curr time
    def PosPerSec(self, newCall: CallForElevator, elev: Elevator):
        if len(elev.floors) == 0:
            return elev.pos
        newCallTime = newCall.time
        elevStartTime = elev.setStartTime
        passedSecs = newCallTime - elevStartTime
        if elev.dir == 1:
            currFloor = list(elev.floors)[0]
        elif elev.dir == -1:
            currFloor = list(elev.floors)[-1]

        # while passedSecs > 0:
        for f1 in elev.floors:
            tmpT = self.timeTo(elev, currFloor, f1)
            if tmpT < passedSecs:
                passedSecs = passedSecs - (tmpT + elev.holdTime)
                currFloor = f1
            else:
                break
        finalFloor = currFloor + (passedSecs / elev.speed)
        return finalFloor

    ## calc time between 2 floors
    def timeTo(self, elev: Elevator, src: int, dest: int):
        diff = abs(dest - src)
        return diff / elev.speed
