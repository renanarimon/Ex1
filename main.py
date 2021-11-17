import argparse
import csv
from Algo_offline import Algo_offline
from CallForElevator import CallForElevator as clfe
from Building import Building

callList = []


# callList - list of all calls from csv

def getCallList():
    return callList


# openCsv: read each row in csv --> CallForElevator --> add to 'callList'

def openCsv(file_name):
    with open(file_name, "r+") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            x = line[0].split(",")
            callList.append(clfe(x[0], x[1], x[2], x[3], x[4], x[5]))


# writeToCsv: write CallForElevators after allocation to csv
def writeToCsv():
    filename = r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\out.csv"
    writer1 = csv.writer(open(filename, "w", newline=''), quoting=csv.QUOTE_NONE, escapechar=' ', delimiter=' ')
    for k in mydict.keys():
        writer1.writerow([k.toString()])


if __name__ == '__main__':
    # get arguments from configuration
    parser = argparse.ArgumentParser()
    parser.add_argument('building')
    parser.add_argument('calls')
    args = parser.parse_args()

    # make building form xml
    b = Building(args.building)

    # make calls from csv
    openCsv(args.calls)

    # call the algorithm
    algo = Algo_offline(b, callList)
    algo.allocate()
    mydict = algo.dict

    writeToCsv()
