class UI:
    def __init__(self, controller):
        self.controller = controller

    def mainMenu(self):

        cmd = input("1 - BFS\n2 - GBFS\nGive command: ")
        if cmd == "1":
            self.controller.runBFS()
        if cmd == "2":
            self.controller.runGBFS()