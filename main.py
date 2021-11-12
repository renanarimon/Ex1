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

    pathCall = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Calls\Calls_c.csv"
    pathBuild = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B4.json"
    # path = r"{}\data\Ex1_input\Ex1_Buildings\{}".format(pathlib.Path(__file__).parent.resolve(),args.building)
    b = Building(pathBuild)
    openCsv(pathCall)
    algo = MyAlgo(b, callList)
    algo.MyAllocte()
    mydict = algo.dict
    # print(len(d))

    filename = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\out4.csv"
    # open the file in the write mode
    with open(filename, 'w', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        for k in mydict.keys():
            writer.writerow([k.toString()])

        f.close()

