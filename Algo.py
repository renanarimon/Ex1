import math
import sys

from Assignments.Ex1.Building import Building
from Assignments.Ex1.CallForElevator import CallForElevator
from Assignments.Ex1.AllCalls import AllCalls
from Assignments.Ex1.Elevator import Elevator


class Algo:
    def __init__(self, building: Building, allCalls: AllCalls):
        self.building = building
        self.elevs = building.elevators
        self.allCalls = allCalls
        self.dict = {}

    """
    allocate all the calls to elevators
    """

    def allocate(self):
        while len(self.allCalls.calls) > 0:
            c1 = self.allCalls.calls.pop(0)
            bestElev = self.elevs[0]
            bestTime = sys.maxsize
            for elev in self.elevs:
                currTime = self.CalcSD(elev, c1.src, elev.pos_end)  # time to get to the call
                if c1.time() < elev.time_end:  # elev is not free
                    currTime += elev.preSet
                if currTime < bestTime:
                    bestElev = elev
                    bestTime = currTime
            self.dict.update({c1.time(): bestElev.id})
            bestElev.floors.add(c1.src)
            bestElev.floors.add(c1.dest())
            timeEndC = self.CalcSD(bestElev, c1.src, c1.dest()) + c1.time()
            self.RangeCalls(bestElev, c1, timeEndC)

    ## calc time from src to dest
    def CalcSD(self, elev: Elevator, src, dest):
        diff = abs(src - dest)
        ans = (diff / elev.speed) + 2 * (elev.stopTime + elev.startTime + elev.openTime + elev.closeTime)
        return ans

    ## allocate all calls in time range
    def RangeCalls(self, elev: Elevator, c1: CallForElevator, timeEndC: float):
        for call in self.allCalls:
            if call.time() > timeEndC:  # go over calls in range
                break
            if call.dir == c1.dir:  # same dir
                if (call.dir == 1 and c1.src <= call.src) or (
                        call.dir == 0 and c1.src >= call.src):  # in range
                    if call.time() > self.calcTimeToSrc(elev, call.src):
                        self.dict.update({call.time(): elev.id})
                        elev.floors.add(call.src)
                        elev.floors.add(call.dest)
                        self.allCalls.remove(call)
        elev.pos_end = list(elev.floors)[-1]  # pos = last dest
        elev.preSet = elev.calcSet()
        elev.time_end = elev.preSet + c1.time()
        elev.floors.clear()

    def calcTimeToSrc(self, elev: Elevator, src: int):
        counter = 1
        for i in range(len(elev.floors)):
            if src > list(elev.floors)[i]:
                # for i in elev.floors:
                #     print("hi im f: ", i)
                #     if src > i:
                counter += 1
        diff = abs(list(elev.floors)[0] - src)
        ans = (diff / elev.speed) + counter * (elev.stopTime + elev.startTime + elev.openTime + elev.closeTime)
        return ans

    def timePerSec1(self, newCall: CallForElevator, elev: Elevator):
        newCallTime = newCall.time()
        elevStartTime = elev.setStartTime
        passedSecs = newCallTime - elevStartTime
        currFloor = list(elev.floors)[0]

        # while passedSecs > 0:
        for f1 in elev.floors:
            tmpT = self.timeTo1(elev, currFloor, f1)
            if (tmpT < passedSecs):
                passedSecs = passedSecs - (tmpT + elev.holdTime)
                currFloor = f1
            else:
                break
        finalFloor = currFloor + (passedSecs/elev.speed)
        return finalFloor

    def timeTo1(self, elev: Elevator, src, dest):
        diff = abs(dest - src)
        return diff / elev.speed
