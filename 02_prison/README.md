# Day 02 - Python Bootcamp

Discover the mysteries of a closed Vault

## Table of Contents

- [Day 02 - Python Bootcamp](#day-02---python-bootcamp)
  - [Table of Contents](#table-of-contents)
    - [Rules of the day](#rules-of-the-day)
  - [Tasks](#tasks)
    - [Exercise 00: Gaining Access (key.py)](#exercise-00-gaining-access-keypy)
    - [Exercise 01: Morality (prisoners\_dilemma.py)](#exercise-01-morality-prisoners_dilemmapy)
    - [Reading and tips](#reading-and-tips)

### Rules of the day

- You should only turn in `*.py` files
- It is encouraged to write some tests for various cases inside your scripts as well. To make them run only when script is executed directly and not imported from somewhere else you can use `if __name__ == "__main__":` statement. You can read more about it [here](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)
- You can guess (or model) the solution for EX01, or you can go through [this small tutorial on Game Theory](https://ncase.me/trust/) to help you with that

## Tasks

### Exercise 00: Gaining Access ([key.py](./prison/key.py))

set of lines appeared in the screen:

```log
AssertionError: len(key) == 1337
AssertionError: key[404] == 3
AssertionError: key > 9000
AssertionError: key.passphrase == "zax2rulez"
AssertionError: str(key) == "GeneralTsoKeycard"

```

You need to describe a Python class `Key` so that an instance of this class
would pass the checks listed above. Keep in mind, that your code in this
exercise shouldn't create any containers, neither of size 404 nor less.

### Exercise 01: Morality ([prisoners_dilemma.py](./prison/prisoners_dilemma.py))

There is a machine that
controls the supply of candy for two groups of people based on whether
one or both of two operators put one in it:

|  | Both cooperate | 1 cheats, 2 cooperates | 1 cooperates, 2 cheats | Both cheat |
|------------|----------|----------|----------|---------|
| Operator 1 | +2 candy | +3 candy | -1 candy | 0 candy |
| Operator 2 | +2 candy | -1 candy | +3 candy | 0 candy |

So, if everyone is cooperating and puts candy in a machine as agreed,
everyone gets a reward. But both participants also have a temptation to
cheat and only pretend to put a candy into machine, because in this case
their group will get 3 candy back, just taking one candy from a second
group. The problem is, if both operators decide to play dirty, then nobody
will get anything.

Here are the five models of behavior that it used to run experiments:

| Behavior type | Player Actions                                                                                                                                                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cheater       | Always cheats                                                                                                                                                                                          |
| Cooperator    | Always cooperates                                                                                                                                                                                      |
| Copycat       | Starts with cooperating, but then just repeats whatever the other guy is doing                                                                                                                         |
| Grudger       | Starts by always cooperating, but switches to Cheater forever if another guy cheats even once                                                                                                          |
| Detective     | First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],  and if during these four turns another guy cheats even once -  switches into a Copycat. Otherwise, switches into Cheater himself |

-----

You need to model a system with seven
classes - `Game`, `Player` and five behavior types (subclassed from `Player`).

The skeleton for a `Game` class looks like this:

```python
from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        # simulate number of matches
        # equal to self.matches

    def top3(self):
        # print top three
```

Here, `registry` is used to keep track of the current number of candy
during the game, while `player1` and `player2` are instances of
subclasses of `Player` (each being one of 5 behavior types). Calling
`play()` method of a `Game` instance should perform a simulation
of a specified number of matches between players of a given behavior.

Method `top3()` should print current top three player's behaviors
along with their current score, like:

```log
cheater 10
detective 9
grudger 8
```

By default, your code when run should simulate 10 matches (one call of
`play()`) between every pair of two players with *different* behavior
types (total 10 rounds by 10 matches each, no matches between two
copies of the same behavior) and print top three winners after the
whole game.

You are strongly encouraged to experiment around with different
behaviors and writing your own behavior class (this is graded as a
bonus). You can get even more bonus points if an instance of your
class performs better in the same "contest between each pair of
players" check that at least three of five provided behaviors.

Don't forget that the only thing a player can do on each turn is
either cooperate or cheat, based on a history of a current game.

### Reading and tips

Classes in Python fully support inheritance, but do not provide encapsulation very well. Probably
one of the most interesting things to look at in Python OOP is `super()`, you can read about it
[here, for example](https://realpython.com/python-super/).

Another thing to read about is a "constructor", which in Python is complex and includes at least
two methods - `__new__` and `__init__`. Here is [some more information](https://medium.com/thedevproject/new-vs-init-in-python-a-most-known-resource-7beb538dc3b) on topic.
