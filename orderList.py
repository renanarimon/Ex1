from Assignments.Ex1 import Elevator, Building


class orderList:
    def __init__(self, elev: Elevator, building: Building):
        self._elev = elev
        self._building = building
        self._UP1 = set()
        self._UP2 = set()
        self._DOUN1 = set()
        self._DOUN2 = set()
        self._pointer = set()

    def isEmpty(self):
        return len(self._UP1) == 0 and len(self.UP2) == 0 and len(self._DOUN1) == 0 and len(self._DOUN2) == 0

    def remove(self):
        if self._pointer == self._UP1 and len(self._UP1) > 0:
            ans = list(self._UP1).pop()
            if len(self._UP1) == 0:
                if len(self._DOUN1) > 0:
                    self._pointer = self._DOUN1
                elif len(self._DOUN2) > 0:
                    self._pointer = self._DOUN2
                elif (len(self._UP2) > 0):
                    self._pointer = self._UP2
        elif self._pointer == self._UP2 and len(self._UP2) > 0:
            ans = list(self._UP2).pop()
            if len(self._UP2) == 0:
                if len(self._DOUN1) > 0:
                    self._pointer = self._DOUN1
                elif len(self._DOUN2) > 0:
                    self._pointer = self._DOUN2
                elif len(self._UP1) > 0:
                    self._pointer = self._UP1

        elif self._pointer == self._DOUN1 and len(self._DOUN1) > 0:
            ans = list(self._DOUN1)[-1]
            self._DOUN1.remove(ans)
            if len(self._DOUN1) == 0:
                if len(self._UP1) > 0:
                    self._pointer = self._UP1
                elif len(self._UP2) > 0:
                    self._pointer = self._UP2
                elif len(self._DOUN2) > 0:
                    self._pointer = self._DOUN2
        elif self._pointer == self._DOUN2 and len(self._DOUN2) > 0:
            ans = list(self._DOUN2)[-1]
            self._DOUN2.remove(ans)
            if len(self._DOUN2) == 0:
                if len(self._UP1) > 0:
                    self._pointer = self._UP1
                elif len(self._UP2) > 0:
                    self._pointer = self._UP2
                elif len(self._DOUN1) > 0:
                    self._pointer = self._DOUN1
        return ans

    def calcSet(self, curSet: set):
        if len(curSet) == 0: return 0;
        diff = abs(list(curSet)[0] - list(curSet)[-1])
        ans = (diff / self._elev.speed) + len(curSet) * (self._elev.stopTime + self._elev.startTime
                                                         + self._elev.openTime + self._elev.closeTime)
        return ans

    # def add(self, c:Calls):
    #     if(c.calls[])
