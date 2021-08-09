import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# MORSE CODE
# ---------------------------------------------------------------------------------------------------------------------------

class Morse(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        msg = g.question(question="What is the message? Enter as morse or letters with spaces between each:", 
        answers=g.MORSEDICT, size=0)

        word = ''.join(msg)
        wordbank = {"shell":"3.505","halls":"3.515","slick":"3.522","trick":"3.532","boxes":"3.535","leaks":"3.542",
        "strobe":"3.545","bistro":"3.552","flick":"3.555","bombs":"3.565","break":"3.572","brick":"3.575","steak":"3.582",
        "sting":"3.592","vector":"3.595","beats":"3.600"}

        if word in wordbank:
            print(f"Transmit at {wordbank[word]} MHz.")
            return wordbank[word]
        print(f"Word \"{word}\" not found.")
        return None
