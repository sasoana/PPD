from Problem import *
from Controller import *
from timeit import default_timer as timer

pr = Problem()
ctrl = Controller(pr)
start = timer()
ctrl.runGBFS()
end = timer()
print("GBFS, sequential: " + str((end - start)* 1000) + " milliseconds")

start = timer()
ctrl.runGBFSparallel()
end = timer()
print("GBFS, parallel: " + str((end - start)* 1000) + " milliseconds")
