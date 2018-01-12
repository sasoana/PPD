from copy import deepcopy


class State:
    def __init__(self, values, n, steps):
        self.values = values
        self.n = n
        self.steps = steps

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.n):
                string += str(self.values[i][j]) + " "
            string += "\n"

        return string

    def __eq__(self, other):

        for i in range(self.n):
            for j in range(self.n):
                if self.values[i][j] != other.values[i][j]:
                    return False
        return True

    def getValue(self, i, j):
        return self.values[i][j]

    def getValues(self):
        return deepcopy(self.values)

    def findCoordinates(self, value):
        for i in range(self.n):
            for j in range(self.n):
                if self.values[i][j] == value:
                    return i, j