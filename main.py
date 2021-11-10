import argparse
import csv
import json
from Assignments.Ex1.CallForElevator import CallForElevator as clfe
from Assignments.Ex1.Building import Building
import pathlib
list = []


def openCsv(file_name):
    with open(file_name, "r+") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            x = line[0].split(",")
            list.append(clfe(x[0], x[1], x[2], x[3], x[4], x[5]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('calls')
    parser.add_argument('building')
    args = parser.parse_args()
    print(args.building)
    path = "{}\data\Ex1_input\Ex1_Buildings\{}".format(pathlib.Path(__file__).parent.resolve(),args.building)
    print(path)
    b = Building(path)
    print(b.toString())
    print(b.maxFloor)



    # def openJson():
    #     with open(args.building) as f:
    #         data = json.load(f)
