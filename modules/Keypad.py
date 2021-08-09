import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# KEYPAD
# ---------------------------------------------------------------------------------------------------------------------------

class Keypad(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        keypad = g.question(question='''What are the keypad symbols? Possible symbols: 
б 6, Ӭ euro, Ѯ 3, Ѽ gamepad, Ѧ at, Ѭ alien, Ѣ tb, Ҋ n, Җ k, 
Ҩ wisp, Ԇ r, ҂ rail, Ͼ (, Ͽ ), Ψ phi, Ϟ bolt, Ϙ o, Ω omega, 
ϗ h, ƛ lambda, æ ae, ټ smiley,  © copy, ¿ ?, ¶ p, ☆ k*, ★ w*.
Seperate with spaces:''', 
        answers=g.SIMPLEDICT(["6","euro","3","gamepad","at","alien","tb","n","k","wisp","r","rail","(",")","phi","bolt","o",
        "omega","h","lambda","ae","smiley","copy","?","p","k*","w*"]), size=4)
        
        table = [
            ["o","at","lambda","bolt","alien","h",")"],
            ["euro","o",")","wisp","w*","h","?"],
            ["copy","gamepad","wisp","k","r","lambda","w*"],
            ["6","p","tb","alien","k","?","smiley"],
            ["phi","smiley","tb","(","p","3","k*"],
            ["6","euro","rail","ae","phi","n","omega"]
            ]

        for column in table:
            if set(keypad) <= set(column):
                answer = sorted(keypad, key=column.index)
                print(f"Press {answer[0]}, {answer[1]}, {answer[2]}, then {answer[3]}.")
                return answer
        print("Invalid. The four symbols do not appear in the same column.")
        return None