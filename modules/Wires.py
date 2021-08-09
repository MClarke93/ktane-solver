import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# WIRES
# ---------------------------------------------------------------------------------------------------------------------------

class Wires(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        wires = g.question("What are the wire colors from top to bottom? E.g. \"RKYBB\":", answers=g.SIMPLEDICT("rbywk"), size=0, delim="")
        count, answer = (len(wires), None)

        if count == 3:
            if 'r' not in wires:
                answer = 2
            elif wires[-1] == 'w':
                answer = 3
            elif wires.count('b') > 1:
                answer = 3-wires[::-1].index('b')
            else:
                answer = 3
        elif count == 4:
            if wires.count('r') > 1 and int(self.device.getserial()[-1])%2 == 1:
                answer = 4-wires[::-1].index('r')
            elif wires.count('b') == 1 or (wires[-1] == 'y' and wires.count('r') == 0):
                answer = 1
            elif wires.count('y') > 1:
                answer = 4
            else:
                answer = 2
        elif count == 5:
            if wires[-1] == 'k' and int(self.device.getserial()[-1])%2 == 1:
                answer = 4
            elif wires.count('r') == 1 and wires.count('y') > 1:
                answer = 1
            elif wires.count('k') == 0:
                answer = 2
            else:
                answer = 1
        elif count == 6:
            if wires.count('y') == 0 and int(self.device.getserial()[-1])%2 == 1:
                answer = 3
            elif wires.count('y') == 1 and wires.count('w') > 1:
                answer = 4
            elif wires.count('r') == 0:
                answer = 6
            else:
                answer = 4
        else:
            print("Invalid. There should be 3-6 wires.")
        
        if answer != None and answer in range(1, count+1):
            print(f"Cut wire #{answer}.")
        return answer
