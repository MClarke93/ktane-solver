# ktane-solver
This is a solver for the game **[Keep Talking and Nobody Explodes](https://keeptalkinggame.com/)**. It takes the place of the **[Defusal Manual](https://www.bombmanual.com/)**, allowing a team to enter what they see in the game and immediately recieve an answer, without having to figure it out using the manual.

The solver requires **[Python 3](https://www.python.org/)**, but has no additional dependencies.

To use the solver:
1. Clone this repository
2. Navigate to the root folder of the project using your favourite command line interface
3. Execute `py solver.py`
4. Follow the on-screen instructions.

The solver asks you to provide the ID of the module you wish to solve. This refers to the internal IDs used by the game to uniquely identify each module. The IDs for the base game are:
|Module|ID|
|:-|:-|
|Wires|`Wires`|
|The Button|`BigButton`|
|Keypad|`Keypad`|
|Simon Says|`Simon`|
|Who's on First \*|`WhosOnFirst`|
|Memory|`Memory`|
|Morse Code|`Morse`|
|Complicated Wire|`Venn`|
|Wire Sequence|`WireSequence`|
|Maze \*|`Maze`|
|Password|`Password`|

\* = Not implemented (yet)

If any modded modules from the Steam Workshop are supported by this solver in future, their IDs can be found on the **[Repository of Manual Pages](https://ktane.timwi.de/)**.

---

New modules can be added to the solver by adding a new `.py` to the `modules` folder. The name of the file should match the name of the module. Inside, start with the following boilerplate:

```py
import engine.module as m

class IDGoesHere(m.Module):
    # Replace 'IDGoesHere' with the module ID...
    def __init__(self, device):
        super().__init__(device=device)
    
    def solve(self):
        # Solve method goes here...
```

When the user enters an ID during runtime, it runs the corresponding `solve()` automatically.

---

Things left to-do:
* Implement solvers for Who's on First and Maze.
* Allow the user to start a new mission or change edgework without restarting the program. 
* Clean up the code for consistency and clarity.