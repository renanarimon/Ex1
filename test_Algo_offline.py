import unittest
from Algo_offline import Algo_offline
from main import callList, openCsv
from Building import Building


class test_algo_offline(unittest.TestCase):

    def setUp(self) -> None:
        self.allcalls = callList
        self.building = Building(r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B3.json")
        self.algo = Algo_offline(self.building, self.allcalls)

    def testA(self):
        assert self.building.minFloor == -10
        assert len(self.allcalls) == len(self.algo.dict)

    def testB(self):
        self.algo.allocate()
        print(len(self.allcalls))


