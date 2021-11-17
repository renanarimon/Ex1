class CallForElevator:
    def __init__(self, name, time: float, src: int, dest: int, state: int, allocatedTo: int):
        self.name = name
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)
        self.allocatedTo = int(allocatedTo)

    def toString(self):
        st = "{},{},{},{},{},{}".format("Elevator call", self.time, self.src,
                                        self.dest, self.state,
                                        self.allocatedTo)

        return st
