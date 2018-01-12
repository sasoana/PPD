from queue import Queue
import hashlib


class Controller:
    def __init__(self, problem):
        self.problem = problem
        self.q = Queue()
        self.items = []

    def orderStates(self, states):

        states.sort(key=lambda x: self.problem.heuristic(x), reverse=True)
        return states

    def runBFS(self):

        visited = {}
        visited[hashlib.sha224(self.problem.initialState.getValues().__str__().encode('utf-8')).hexdigest()] = True
        self.q.put(self.problem.initialState)
        while (True):
            current = self.q.get()
            if self.problem.isFinalState(current):
                print("Solution found in " + str(current.steps) + " steps.")
                break
            else:
                states = self.problem.expand(current)
                for x in states:
                    if not visited.get(hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest(), False):
                        visited[hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest()] = True
                        # print(x)
                        self.q.put(x)

    def runGBFS(self):

        self.items.append(self.problem.initialState)
        visited = {}
        visited[hashlib.sha224(self.problem.initialState.getValues().__str__().encode('utf-8')).hexdigest()] = True
        while (True):
            current = self.items.pop()
            if self.problem.isFinalState(current):
                print("Solution found in " + str(current.steps) + " steps.")
                break
            succesors = self.problem.expand(current)
            succesors1 = self.orderStates(succesors)
            for x in succesors1:
                if not visited.get(hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest(), False):
                    visited[hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest()] = True
                    # print(x)
                    self.items.append(x)
