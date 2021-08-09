import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# WIRE SEQUENCE
# ---------------------------------------------------------------------------------------------------------------------------

class WireSequence(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        options = [f""]+[f"{color}{letter}" for color in "rbk" for letter in "abc"]
        reds, blues, blacks = (0, 0, 0)
        redcuts, bluecuts, blackcuts = (["c","b","a","ac","b","ac","abc","ab","b"], ["b","ac","b","a","b","bc","c","ac","a"], ["abc","ac","b","ac","b","bc","ab","c","c"])

        while True:
            wire = g.question(question="What's the next wire color and which letter does it go to? E.g. \"kc\":", 
            answers=g.SIMPLEDICT(options))
            cut = False
            if wire == "":
                return True
            else:
                if wire[0] == "r":
                    if wire[1] in redcuts[reds]:
                        cut = True
                    reds = reds + 1
                elif wire[0] == "b":
                    if wire[1] in bluecuts[blues]:
                        cut = True
                    blues = blues + 1
                else:
                    if wire[1] in blackcuts[blacks]:
                        cut = True
                    blacks = blacks + 1
                if cut == True:
                    print("Yes, cut the wire.")
                else:
                    print("No, leave the wire.")
