import sys
from math import ceil

from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator


class MyAlgo:
    def __init__(self, building: Building, allCalls: list):
        self.building = building
        self.allCalls = allCalls
        self.dict = {}

    def allocate(self):
        for c in self.allCalls:
            if c.src < self.building.minFloor or c.src > self.building.maxFloor or c.dest > self.building.maxFloor or c.dest < self.building.minFloor:
                c.allocatedTo = -1
            else:
                bestElev = self.building.elevators[0]
                bestTime = sys.maxsize
                flag = ""
                for elev in self.building.elevators:
                    oppositePointer = ""
                    if elev.pointer == "":  # dict isEmpty
                        tmpTime = self.timeTo(elev, elev.pos, c.src)
                        if tmpTime < bestTime:
                            bestElev = elev
                            bestTime = tmpTime
                            flag = "up1" if c.dir == 1 else "down1"
                    elif ((c.dir == 1) and ((elev.pointer == "up1") or (elev.pointer == "up2"))) or (
                            (c.dir == -1) and ((elev.pointer == "down1") or (elev.pointer == "down2"))):
                        if c.dir == 1:
                            tmpPos = self.PosPerSec(c, elev)  # tmpPos = floor of elev at c time
                            if c.src >= tmpPos:  # in curr time, if elev didnt pass this floor
                                tmpTime = self.calcBestTime(elev, c, elev.pointer)
                                if tmpTime < bestTime:
                                    bestElev = elev
                                    bestTime = tmpTime
                                    flag = elev.pointer
                            else:  # elev pass the call --> add to up2
                                oppositePointer = "up2" if elev.pointer == "up1" else "up1"
                                tmpTime = self.calcBestTime(elev, c, oppositePointer)
                                if tmpTime < bestTime:
                                    bestElev = elev
                                    bestTime = tmpTime
                                    flag = oppositePointer
                        elif c.dir == -1:
                            tmpPos = self.PosPerSec(c, elev)  # tmpPos = floor of elev at c time
                            if c.src <= tmpPos:  # in curr time, if elev didnt pass this floor
                                tmpTime = self.calcBestTime(elev, c, elev.pointer)
                                if tmpTime < bestTime:
                                    bestElev = elev
                                    bestTime = tmpTime
                                    flag = elev.pointer
                            else:  # elev pass the call --> add to down2
                                oppositePointer = "down2" if elev.pointer == "down1" else "down1"
                                tmpTime = self.calcBestTime(elev, c, oppositePointer)
                                if tmpTime < bestTime:
                                    bestElev = elev
                                    bestTime = tmpTime
                                    flag = oppositePointer
                    else:  # opposite dir
                        if c.dir == 1:  # UP
                            addTo = "up1" if len(elev.orderDict.get("up1")) != 0 else "up2"  # where to add c
                            tmpTime = self.calcBestTime(elev, c, addTo)
                            if tmpTime < bestTime:
                                bestElev = elev
                                bestTime = tmpTime
                                flag = addTo
                        elif c.dir == -1:
                            addTo = "down1" if len(elev.orderDict.get("down1")) != 0 else "down2"  # where to add c
                            tmpTime = self.calcBestTime(elev, c, addTo)
                            if tmpTime < bestTime:
                                bestElev = elev
                                bestTime = tmpTime
                                flag = addTo
                c.allocatedTo = bestElev.id
                self.dict.update({c: bestElev.id})
                if bestElev.isEmpty:  # update start time of first call
                    bestElev.setStartTime = c.time
                    bestElev.pointer = flag
                    bestElev.pos = c.src
                if c.src not in bestElev.orderDict.get(flag):
                    bestElev.orderDict.get(flag).append(c.src)
                if c.dest not in bestElev.orderDict.get(flag):
                    bestElev.orderDict.get(flag).append(c.dest)

    def PosPerSec(self, c: CallForElevator, elev: Elevator):
        passedSecs = c.time - elev.setStartTime
        currFloor = elev.pos
        if elev.isEmpty():
            return elev.pos
        elev.orderDict.get(elev.pointer).sort()
        if elev.pointer == "up1" or elev.pointer == "up2":
            currFloor, passedSecs = self.myFloor(elev, elev.pointer, passedSecs)

            if len(elev.orderDict.get(elev.pointer)) <= 0:
                currPointer = "down1" if len(elev.orderDict.get("down1")) > 0 else "down2"
                if len(elev.orderDict.get("down1")) > 0 or len(elev.orderDict.get("down2")) > 0:
                    elev.orderDict.get(currPointer).sort(reverse=True)  # down --> reverse
                    currFloor, passedSecs = self.myFloor(elev, currPointer, passedSecs)
                if len(elev.orderDict.get(currPointer)) <= 0:
                    oppositePointer = "up2" if elev.pointer == "up1" else "up1"

                    if len(elev.orderDict.get(oppositePointer)) > 0:
                        elev.orderDict.get(oppositePointer).sort()
                        tmpTime = self.timeTo(elev, currFloor,
                                              elev.orderDict.get(oppositePointer)[0])  # time to get between 2 lists
                        if tmpTime > passedSecs:
                            currFloor -= ceil(passedSecs * elev.speed)
                        else:
                            passedSecs -= tmpTime
                            currFloor, passedSecs = self.myFloor(elev, oppositePointer, passedSecs)

        elif elev.pointer == "down1" or elev.pointer == "down2":
            elev.orderDict.get(elev.pointer).reverse()  # down --> reverse
            currFloor, passedSecs = self.myFloor(elev, elev.pointer, passedSecs)
            if len(elev.orderDict.get(elev.pointer)) <= 0:
                currPointer = "up1" if len(elev.orderDict.get("up1")) > 0 else "up2"
                if len(elev.orderDict.get("up1")) > 0 or len(elev.orderDict.get("up2")) > 0:
                    elev.orderDict.get(currPointer).sort()
                    currFloor, passedSecs = self.myFloor(elev, currPointer, passedSecs)
                if len(elev.orderDict.get(currPointer)) <= 0:
                    oppositePointer = "down2" if elev.pointer == "down1" else "down1"
                    if len(elev.orderDict.get(oppositePointer)) > 0:
                        elev.orderDict.get(oppositePointer).sort(reverse=True)
                        tmpTime = self.timeTo(elev, currFloor,
                                              elev.orderDict.get(oppositePointer)[0])  # time to get between 2 lists
                        if tmpTime > passedSecs:
                            currFloor += ceil(passedSecs * elev.speed)
                        else:
                            passedSecs += tmpTime
                            currFloor, passedSecs = self.myFloor(elev, oppositePointer, passedSecs)
        elev.setStartTime = c.time
        return currFloor

    def myFloor(self, elev: Elevator, p: str, passedSecs: float):
        counter = 0
        currFloor = elev.pos
        for f in elev.orderDict.get(p):
            tmpT = self.timeTo(elev, currFloor, f)
            if tmpT + elev.holdTime < passedSecs:
                passedSecs = passedSecs - (tmpT + elev.holdTime)
                currFloor = f
                elev.setStartTime += tmpT
                counter += 1
            elif len(elev.orderDict.get(p)) > 0:
                if p == "up1" or p == "up2":
                    tmpF = currFloor + ceil(passedSecs * elev.speed)
                    currFloor = tmpF if tmpF < elev.orderDict.get(p)[-1] else elev.orderDict.get(p)[-1]
                else:
                    tmpF = currFloor - ceil(passedSecs * elev.speed)
                    currFloor = tmpF if tmpF > elev.orderDict.get(p)[-1] else elev.orderDict.get(p)[-1]
                elev.pointer = p
                elev.delete(p, 0, -1)
                break
        elev.delete(p, 0, counter)

        elev.pos = currFloor
        return currFloor, passedSecs

    ## calc time between 2 floors
    def timeTo(self, elev: Elevator, src: int, dest: int):
        diff = abs(dest - src)
        return diff / elev.speed

    def calcDict(self, elev: Elevator):
        sum = 0
        for v in elev.orderDict.values():
            if len(v) != 0:
                v.sort()
                diff = abs(v[-1] - v[0])
                sum += (diff / elev.speed) + len(v) * elev.holdTime
        return sum

    ## calc the time to add call:
    ## calc time before adding call and time after,
    ## return diff
    def calcBestTime(self, elev: Elevator, c: CallForElevator, st: str):
        timeBefore = self.calcDict(elev)
        elev.orderDict.get(st).append(c.src)
        elev.orderDict.get(st).append(c.dest)
        tmpTime = abs(self.calcDict(elev) - timeBefore)
        elev.orderDict.get(st).remove(c.src)
        elev.orderDict.get(st).remove(c.dest)
        return tmpTime
