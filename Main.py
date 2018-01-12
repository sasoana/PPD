from Problem import *
from Controller import *
from UI import *

pr = Problem()
ctrl = Controller(pr)
ui = UI(ctrl)
ui.mainMenu()