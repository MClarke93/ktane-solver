import engine.globe as g
import engine.module as m

# ---------------------------------------------------------------------------------------------------------------------------
# PASSWORD
# ---------------------------------------------------------------------------------------------------------------------------

class Password(m.Module):
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        reels = [g.question(question=f"What are the letters in position #{num}?", 
        answers=g.SIMPLEDICT(g.LETTERLIST), size=6, delim="") for num in range(1,6)]
        wordlist = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", 
        "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", 
        "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]

        for word in wordlist:
            if word[0] in reels[0] and word[1] in reels[1] and word[2] in reels[2] and word[3] in reels[3] and word[4] in reels[4]:
                print(f"The password is {word.upper()}.")
                return word
        print(f"Valid word could not be found.")
        return None
