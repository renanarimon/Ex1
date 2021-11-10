import argparse
import csv
import json
from Assignments.Ex1.CallForElevator import CallForElevator as clfe
list = []


def openCsv():
    with open(r"C:\Users\PC\PycharmProjects\OOP_2021-main\Assignments\Ex1\Ex1_Calls\Calls_a.csv") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            x = line[0].split(",")
            list.append(clfe(x[0], x[1], x[2], x[3], x[4], x[5]))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('calls')
    parser.add_argument('building')
    args = parser.parse_args()
    openCsv()
    print(list.pop(0).toString())


    # def openJson():
    #     with open(args.building) as f:
    #         data = json.load(f)
