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
                currTime = self.CalcSD(elev, c1.src, elev.pos_end)
                if c1.time < elev.time_end:  # elev is not free
                    currTime += elev.preSet
                if currTime < bestTime:
                    bestElev = elev
                    bestTime = currTime
            self.dict.update({c1: bestElev})
            bestElev.Elevator.floors.add(c1.src)
            bestElev.Elevator.floors.add(c1.dest)
            timeEndC = self.CalcSD(bestElev, c1.src, c1.dest) + c1.time
            self.RangeCalls(bestElev, c1, timeEndC)

    ## calc time from src to dest
    def CalcSD(self, elev: Elevator, src, dest):
        diff = abs(src - dest)
        ans = (diff / elev.speed) + 2 * (elev.stopTime + elev.startTime + elev.openTime + elev.closeTime)
        return ans

    ## allocate all calls in time range
    def RangeCalls(self, elev: Elevator, c1: CallForElevator, timeEndC):
        for call in self.allCalls.calls:
            while call.time < timeEndC:  # go over calls in range
                if call.dir == c1.dir():  # same dir
                    if (call.dir == 1 and c1.src <= call.src) or (call.dir == 0 and c1.src >= call.src):  # in range
                        self.dict.update({call: elev})
                        elev.floors.add(call.src)
                        elev.floors.add(call.dest)
                        self.allCalls.calls.remove(call)
            elev.pos_end = list(elev.floors)[-1]  # pos = last dest
            self.allCalls.calls.remove(c1)
            elev.preSet = elev.calcSet()
            elev.time_end = elev.preSet + c1.time()
            elev.floors.clear()
            break



