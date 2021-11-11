class Elevator:

    def __init__(self, _id: int, _speed: float, _minFloor: int, _maxFloor: int,
                 _closeTime: float,
                 _openTime: float, _startTime: float, _stopTime: float):
        self.id = int(_id)
        self.speed = float(_speed)
        self.minFloor = int(_minFloor)
        self.maxFloor = int(_maxFloor)
        self.closeTime = float(_closeTime)
        self.openTime = float(_openTime)
        self.startTime = float(_startTime)
        self.stopTime = float(_stopTime)

        self.setStartTime = float(0.0)
        self.holdTime = self.stopTime + self.startTime + self.openTime + self.closeTime

        self.floors = set()
        self.pos_end = int(0)
        self.time_end = float(0.0)
        self.preSet = float(0.0)  # calcset

    def toString(self):
        st = "id = {}, speed ={}, minFloor={}, maxFloor = {}, closeTime = {}, openTime = {}, startTime = {}, " \
             "stopTime = {}, floors ={}, pos_end = {}, time_end = {}, preSet = {}".format(self.id, self.speed,
                                                                                          self.minFloor, self.maxFloor,
                                                                                          self.closeTime, self.openTime,
                                                                                          self.startTime,
                                                                                          self.stopTime,
                                                                                          self.floors,
                                                                                          self.pos_end,
                                                                                          self.time_end,
                                                                                          self.preSet)
        return st

    def calcSet(self):
        if len(self.floors) == 0:
            return 0
        diff = abs(list(self.floors)[0] - list(self.floors)[-1])
        ans = (diff / self.speed) + len(self.floors) * (self.stopTime + self.startTime
                                                        + self.openTime + self.closeTime)
        return ans
