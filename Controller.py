from queue import Queue
import hashlib
import threading


class Controller:
    def __init__(self, problem):
        self.problem = problem
        self.q = Queue()
        self.items = []
        self.visited = {}

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

        # start by adding the initial state to the queue of items and an empty list of visited items
        self.items.append(self.problem.initialState)
        visited = {}
        # mark the initial state as visited
        # we use a hash function to be able to check faster if a certain item has been already visited or not
        # otherwise, we would have to check by iterating over every cell in the matrix of a particular item
        visited[hashlib.sha224(self.problem.initialState.getValues().__str__().encode('utf-8')).hexdigest()] = True
        while (True):
            # get the next item in the queue
            current = self.items.pop()
            # if we have reached the final configuration of the puzzle, stop the algorithm
            if self.problem.isFinalState(current):
                print("Solution found after " + str(current.steps) + " nodes have been created.")
                break
            # otherwise, we expand the current item to its succesors
            # by applying all the possible moves allowed on this configuration of the puzzle
            succesors = self.problem.expand(current)
            # we arrange the successors based on the smallest Manhattan distance with respect to the final state
            # in order to expand first the most promising of the succesors
            succesors1 = self.orderStates(succesors)
            for x in succesors1:
                if not visited.get(hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest(), False):
                    # mark this succesor as visited and add it in the queue
                    visited[hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest()] = True
                    # print(x)
                    self.items.append(x)

    def expandState(self, visited, currentState):
        succesors = self.problem.expand(currentState)
        succesors1 = self.orderStates(succesors)
        for x in succesors1:
            if not visited.get(hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest(), False):
                visited[hashlib.sha224(x.getValues().__str__().encode('utf-8')).hexdigest()] = True
                # print(x)
                self.items.append(x)

    def runGBFSparallel(self):

        threads = []
        self.items.append(self.problem.initialState)
        self.visited[hashlib.sha224(self.problem.initialState.getValues().__str__().encode('utf-8')).hexdigest()] = True
        while (True):
            current = self.items.pop()
            if self.problem.isFinalState(current):
                print("Solution found after " + str(current.steps) + " nodes have been created.")
                break
            t = threading.Thread(target=self.expandState, args=(self.visited, current,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()