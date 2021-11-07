import csv

from Assignments.Ex1.OfflineAlgo.CallForElevator import CallForElevator


class Calls:

    def __init__(self, file_name):
        self.rows = []
        self.calls = []
        self.openCsv(file_name)

    def openCsv(self, file_name):
        with open(file_name) as file:
            csvReader = csv.reader(file)
            header = next(csvReader)

            for row in csvReader:
                call = CallForElevator(name=row[0], time=row[1], src=row[2], dest=row[3], state=row[4],
                                       allocatedTo=row[5])
                self.calls.append(call)
                self.rows.append(row)
