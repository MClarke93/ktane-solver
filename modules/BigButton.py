import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# THE BUTTON
# ---------------------------------------------------------------------------------------------------------------------------

class BigButton(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        options = [f"{color}{label}" for color in "rbyw" for label in "adhp"]
        button = g.question(question="What is the button's color and the first letter of its label? E.g. \"RH\":", answers=g.SIMPLEDICT(options))
        color, label = button
        action = None

        if color == "b" and label == "a":
            action = "h"
        elif label == "d" and self.device.getbatteries() > 1:
            action = "p"
        elif color == "w" and self.device.getlit("car"):
            action = "h"
        elif self.device.getbatteries() > 2 and self.device.getlit("frk"):
            action = "p"
        elif color == "y":
            action = "h"
        elif color == "r" and label == "h":
            action = "p"
        else:
            action = "h"
        
        if action == "p":
            print("Press and immediately release the button.")
        elif action == "h":
            strip = g.question(question="Press and hold the button. What color is the strip?", answers=g.SIMPLEDICT("rbyw"))
            time = 1
            if strip == "b":
                time = 4
            elif strip == "y":
                time = 5
            print(f"Release when the device timer contains a {time}.")
        else:
            print("Invalid. Couldn't find an answer.")
        return action
