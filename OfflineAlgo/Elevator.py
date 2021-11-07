

class Elevator:

    def __init__(self, _id: int = 0, _speed: float = 0.0, _minFloor: int = 0, _maxFloor: int = 0, _closeTime: float = 0.0,
                 _openTime: float = 0.0, _startTime: float = 0.0, _stopTime: float = 0.0):
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime


