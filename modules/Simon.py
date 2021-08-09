import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# SIMON SAYS
# ---------------------------------------------------------------------------------------------------------------------------

class Simon(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        press = ""
        startcolors = "rbgy"
        endcolors = "rbgy"

        strikes = self.device.getstrikes()
        if strikes == 0:
            if self.device.getserialchar("aeiou") > 0:
                endcolors = "bryg"
            else:
                endcolors = "bygr"
        elif strikes == 1:
            if self.device.getserialchar("aeiou") > 0:
                endcolors = "ygbr"
            else:
                endcolors = "rbyg"
        else:
            if self.device.getserialchar("aeiou") > 0:
                endcolors = "gryb"
            else:
                endcolors = "ygbr"

        for stage in range(1,6):
            flash = g.question(question=f"What is the color of flash #{stage}?", answers=g.SIMPLEDICT(['r','b','g','y','']))
            if flash:
                press += endcolors[startcolors.index(flash)]
                print(f"Press {press.upper()}.")
                continue
            break
        return press
            