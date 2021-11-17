from Algo_offline import Algo_offline
from Building import Building
from main import openCsv
import unittest

class test_algo_offline(unittest.TestCase):
    def test_allocate(self):
        calls = []
        # make building form xml
        b = Building(r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B3.json")

        # make calls from csv
        openCsv(r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Calls\Calls_c.csv")

        algo = Algo_offline(b, calls)
        algo.allocate()
        mydict = algo.dict

        self.assertEqual(len(calls), len(mydict), "all calls are allocated!")

        self.assertEqual(mydict.get(calls[0]), 0)
