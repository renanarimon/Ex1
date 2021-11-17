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

    def toString(self):
        st = "id = {}, speed ={}, minFloor={}, maxFloor = {}, closeTime = {}, openTime = {}, startTime = {}, " \
             "stopTime = {}".format(self.id, self.speed,
                                    self.minFloor, self.maxFloor,
                                    self.closeTime, self.openTime,
                                    self.startTime,
                                    self.stopTime,
                                    )
        return st
