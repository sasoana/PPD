from State import *


class Problem:
    filenameInitial = "puzzle.txt"
    filenameFinal = "puzzleout.txt"

    def __init__(self):
        self.n = 0
        self.initialState = [[0 for x in range(3)] for y in range(3)]
        self.finalState = [[0 for x in range(3)] for y in range(3)]
        self.readFomFileIN()
        self.readFromFileOUT()

    def expand(self, state):
        desc = []
        for i in range(self.n):
            for j in range(self.n):
                # based on the row and column of the current tile, we determine the next possible moves
                if state.getValue(i, j) == 0:
                    if i - 1 >= 0:
                        mat = state.getValues()
                        mat[i][j] = mat[i - 1][j]
                        mat[i - 1][j] = 0
                        desc.append(State(mat, state.n, state.steps + 1))
                    if i + 1 < state.n:
                        mat = state.getValues()
                        mat[i][j] = mat[i + 1][j]
                        mat[i + 1][j] = 0
                        desc.append(State(mat, state.n, state.steps + 1))
                    if j - 1 >= 0:
                        mat = state.getValues()
                        mat[i][j] = mat[i][j - 1]
                        mat[i][j - 1] = 0
                        desc.append(State(mat, state.n, state.steps + 1))
                    if j + 1 < state.n:
                        mat = state.getValues()
                        mat[i][j] = mat[i][j + 1]
                        mat[i][j + 1] = 0
                        desc.append(State(mat, state.n, state.steps + 1))

        return desc

    def heuristic(self, state1):
        # Manhattan distance
        #a measure of how far from the final configuration the current one is
        distance = 0
        for x in range(self.n):
            for y in range(self.n):
                value = state1.getValue(x, y)
                x_value = x
                y_value = y
                x_goal, y_goal = self.finalState.findCoordinates(value)
                # computes the sum of the differences between the position of the tile
                # in the current configuration and in the final one
                distance += abs(x_value - x_goal) + abs(y_value - y_goal)

        # print(state1.__str__() + " -> "+ str(distance) + "  " + str(state1.steps))
        return distance

    def isFinalState(self, state):
        return self.heuristic(state) == 0

    def readFomFileIN(self):
        try:
            f = open(self.filenameInitial, "r")
        except IOError:
            return
        mat = [[0 for x in range(10)] for y in range(10)]
        line = f.readline().strip()
        t = line.split(" ")
        self.n = int(t[0])
        for i in range(self.n):
            line = f.readline().strip()
            t = line.split(" ")
            for j in range(self.n):
                mat[i][j] = int(t[j])
        self.initialState = State(mat, self.n, 0)
        print(self.initialState)

    def readFromFileOUT(self):
        try:
            f = open(self.filenameFinal, "r")
        except IOError:
            return
        mat = [[0 for x in range(10)] for y in range(10)]
        line = f.readline().strip()
        t = line.split(" ")
        self.n = int(t[0])
        for i in range(self.n):
            line = f.readline().strip()
            t = line.split(" ")
            for j in range(self.n):
                mat[i][j] = int(t[j])
        self.finalState = State(mat, self.n, 0)
        print(self.finalState)