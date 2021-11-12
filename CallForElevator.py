class CallForElevator:
    def __init__(self, name, time, src, dest, state, allocatedTo):
        self._name = name
        self._time = float(time)
        self._src = int(src)
        self._dest = int(dest)
        self._state = int(state)
        self._allocatedTo = allocatedTo
        if (self._dest - self._src) > 0:
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
        st = "{},{},{},{},{},{}".format(self.name, self.time, self.src,
                                        self.dest, self.state,
                                        self.allocatedTo)
        return st
