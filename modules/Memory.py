import engine.globe as g
import engine.module as m
import itertools

# ---------------------------------------------------------------------------------------------------------------------------
# MEMORY
# ---------------------------------------------------------------------------------------------------------------------------

class Memory(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        options = [num+''.join(perm) for num in "1234" for perm in itertools.permutations("1234", 4)]
        memory = []
        for stage in range(0,5):
            read = g.question(question="What is the display and the button labels in reading order? E.g. \"23142\":", 
            answers=g.SIMPLEDICT(options))

            answer = None
            if stage == 0:
                if read[0] == "3":
                    answer = 3
                elif read[0] == "4":
                    answer = 4
                else:
                    answer = 2
            elif stage == 1:
                if read[0] == "1":
                    answer = 1+read[1:].index("4")
                elif read[0] == "3":
                    answer = 1
                else:
                    answer = memory[0][-1]
            elif stage == 2:
                if read[0] == "1":
                    label = memory[1][int(memory[1][-1])]
                    answer = 1+read[1:].index(str(label))
                elif read[0] == "2":
                    label = memory[0][int(memory[0][-1])]
                    answer = 1+read[1:].index(str(label))
                elif read[0] == "3":
                    answer = 3
                else:
                    answer = 1+read[1:].index("4")
            elif stage == 3:
                if read[0] == "1":
                    answer = memory[0][-1]
                elif read[0] == "2":
                    answer = 1
                else:
                    answer = memory[1][-1]
            else:
                if read[0] == "1":
                    label = memory[0][int(memory[0][-1])]
                    answer = 1+read[1:].index(str(label))
                elif read[0] == "2":
                    label = memory[1][int(memory[1][-1])]
                    answer = 1+read[1:].index(str(label))
                elif read[0] == "3":
                    label = memory[3][int(memory[3][-1])]
                    answer = 1+read[1:].index(str(label))
                else:
                    label = memory[2][int(memory[2][-1])]
                    answer = 1+read[1:].index(str(label))

            memory.append(read+f"{answer}")
            print(f"Press the button in position #{answer}.")
        return memory