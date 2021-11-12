import argparse
import csv
from Assignments.Ex1.Algo import Algo
from Assignments.Ex1.CallForElevator import CallForElevator as clfe
from Assignments.Ex1.Building import Building
import pathlib

from Assignments.Ex1.MyAlgo import MyAlgo

callList = []


def openCsv(file_name):
    with open(file_name, "r+") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            x = line[0].split(",")
            callList.append(clfe(x[0], x[1], x[2], x[3], x[4], x[5]))


def getCallList():
    return callList


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('calls')
    parser.add_argument('building')
    args = parser.parse_args()

    pathCall = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Calls\Calls_b.csv"
    pathBuild = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B2.json"
    # path = r"{}\data\Ex1_input\Ex1_Buildings\{}".format(pathlib.Path(__file__).parent.resolve(),args.building)
    b = Building(pathBuild)
    openCsv(pathCall)
    # print(b.toString())
    # for c in callList:
    #     print(type(c.time))



    # print(type(b.elevators.pop(0).time_end))
    # print(type(callList.pop(0).dir()))

    algo = MyAlgo(b, callList)
    algo.MyAllocte()
    mydict = algo.dict
    # print(len(d))

    # filename = "out.csv"
    # fields = ['name', 'time', 'src', 'dest', 'state', 'allocatedTo']
    # # writing to csv file
    # with open(filename, 'w') as csvfile:
    #     # creating a csv dict writer object
    #     writer = csv.DictWriter(csvfile, fields)
    #
    #     # writing headers (field names)
    #     writer.writeheader()
    #
    #     # writing data rows
    #     writer.writerows(mydict)


        # for k,v in d.items():
    #     print(k.toString())
    #     print(v)
        # print("call: " + k.toString() + "elev: " + v)

    # for i in d:
    #     print(type(i))

