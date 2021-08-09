import engine.device as d
import engine.globe as g
import importlib, sys

# ---------------------------------------------------------------------------------------------------------------------------
# CONTROLLER CLASS
# ---------------------------------------------------------------------------------------------------------------------------

class Controller:
    def __init__(self, device=d.Device()):
        self.device = device

    def getmodule(self, name):
        try:
            return getattr(importlib.import_module("modules."+name), name)
        except:
            print(f"An error occurred trying to load module \"{name}\".")
            return None

    def run(self):
        while True:
            module = g.question(question="\nWhat is the ID of the module you would like to solve?", answers=g.MODULEDICT)
            cla = self.getmodule(module)
            if cla:
                cla(self.device).solve()

# ---------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    x = Controller()
    x.run()
    sys.exit(0)
