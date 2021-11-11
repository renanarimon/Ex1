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
            self.dir = 0  # down

    @property
    def src(self):
        return self._src

    def dest(self):
        return self._dest

    def time(self):
        return self._time


    def toString(self):
        str = "_name = {} _time = {} _time = {} _src = {} _state = {}".format(self._name,self._time,self._src,self._dest,self._state)
        return str



