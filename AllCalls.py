import csv

from CallForElevator import CallForElevator


class AllCalls:

    def __init__(self, file_name):
        self.calls = []
        self.openCsv(file_name)

    def openCsv(self, file_name):
        with open(file_name) as file:
            csvReader = csv.reader(file)

            for row in csvReader:
                call = CallForElevator(row[0], row[1], row[2], row[3], row[4],
                                       row[5])
                self.calls.append(call)
