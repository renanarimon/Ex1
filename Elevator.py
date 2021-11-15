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
        self.orderDict = {}
        self.orderDict.update({"up1": list()})
        self.orderDict.update({"down1": list()})
        self.orderDict.update({"up2": list()})
        self.orderDict.update({"down2": list()})

        self.setStartTime = float(0.0)
        self.holdTime = self.stopTime + self.startTime + self.openTime + self.closeTime
        self.pos = 0
        self.pointer = ""

    def toString(self):
        st = "id = {}, speed ={}, minFloor={}, maxFloor = {}, closeTime = {}, openTime = {}, startTime = {}, " \
             "stopTime = {}, pos_end = {}, time_end = {}, preSet = {}".format(self.id, self.speed,
                                                                              self.minFloor, self.maxFloor,
                                                                              self.closeTime, self.openTime,
                                                                              self.startTime,
                                                                              self.stopTime,
                                                                              self.pos_end,
                                                                              self.time_end,
                                                                              self.preSet)
        return st

    def isEmpty(self):
        for v in self.orderDict.values():
            if len(v) > 0:
                return False
        return True

    def delete(self, p: str, a: int, b: int):
        if b == -1:
            self.orderDict.get(p).clear()
        del self.orderDict.get(p)[a:b]
