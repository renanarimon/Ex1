class CallForElevator:
    def __init__(self, name, time: float, src: int, dest: int, state: int, allocatedTo: int):
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)
        self.allocatedTo =int(allocatedTo)
        if (self.dest - self.src) > 0:
            self.dir = 1  # UP
        else:
            self.dir = -1  # down

    # @property
    # def getSrc(self):
    #     return self._src
    #
    # def getDest(self):
    #     return self._dest
    #
    # def time(self):
    #     return self._time

    def toString(self):

        st = "{},{},{},{},{},{}".format("Elevator call", self.time, self.src,
                                        self.dest, self.state,
                                        self.allocatedTo)

        return st
