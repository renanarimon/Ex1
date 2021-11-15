import argparse
import csv
from Algo import Algo
from CallForElevator import CallForElevator as clfe
from Building import Building
import pathlib

from MyAlgo import MyAlgo

callList = []


def getCallList():
    return callList


def openCsv(file_name):
    with open(file_name, "r+") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            x = line[0].split(",")
            callList.append(clfe(x[0], x[1], x[2], x[3], x[4], x[5]))

def writeToCsv(num):
    filename = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\out"+num+".csv"
    writer1 = csv.writer(open(filename, "w", newline=''), quoting=csv.QUOTE_NONE, escapechar=' ', delimiter=' ')
    for k in mydict.keys():
        writer1.writerow([k.toString()])


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('building')
    parser.add_argument('calls')
    args = parser.parse_args()

    b = Building(args.building)
    openCsv(args.calls)

    algo = MyAlgo(b, callList)
    algo.allocate()
    mydict = algo.dict

    writeToCsv("1")





