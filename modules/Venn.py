import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# COMPLICATED WIRES
# ---------------------------------------------------------------------------------------------------------------------------

class Venn(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        count = g.question(question="How many wires does the module have?", answers=g.RANGEDICT(1,6), 
        error="Invalid. Expected an integer between 1 and 6.")

        answers = {"0000":"C","0001":"D","0010":"C","0011":"B","0100":"S","0101":"P","0110":"D","0111":"P",
        "1000":"S","1001":"B","1010":"C","1011":"B","1100":"S","1101":"S","1110":"P","1111":"D"}

        for num in range(0, count):
            wire = ''.join(g.question(question=f"What is wire #{num+1}? R=Red, B=Blue, *=Star, L=LED, e.g. \"RB*\":", 
            answers=g.SIMPLEDICT(["r","b","*","l",""]), size=0, delim=''))
            answer = ""
            for option in "rb*l":
                answer += "1" if option in wire else "0"

            answer = answers[answer]
            if (answer == "C" or (answer == "S" and int(self.device.getserial()[-1])%2 == 0) 
            or (answer == "P" and self.device.getport(port="parallel") > 0) 
            or (answer == "B" and self.device.getbatteries() > 1)):
                print("Cut the wire.")
            else:
                print("Leave the wire.")
