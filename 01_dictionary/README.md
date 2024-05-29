# Day 01 - Python Bootcamp

Trolling is a art.

Help three honorable gentlemen to figure out the better way

## Table of Contents

- [Day 01 - Python Bootcamp](#day-01---python-bootcamp)
  - [Table of Contents](#table-of-contents)
    - [Rules of the day](#rules-of-the-day)
  - [Tips\*](#tips)
  - [Tasks](#tasks)
    - [Exercise 00: Functional Purse (purse.py)](#exercise-00-functional-purse-pursepy)
    - [Exercise 01: Splitwise (split\_booty.py)](#exercise-01-splitwise-split_bootypy)
    - [Exercise 02: Burglar Alarm (squeak\_decorator.py)](#exercise-02-burglar-alarm-squeak_decoratorpy)
    - [Reading and tips](#reading-and-tips)

### Rules of the day

- You should only turn in `*.py` files
- Your script (or scripts) for this day should have all functions on top level of the file, so they can possibly be imported for checking
- It is encouraged (and graded as a bonus) to write some tests for various cases inside your scripts as well. To make them run only when script is executed directly and not imported from somewhere else you can use `if __name__ == "__main__":` statement. You can read more about it [here](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

## Tips*

To make life easier I create [bash script](./src/test.sh) for testing all of 3 scripts. Just run the command from ./src directory:

```sh
./test.sh
```

## Tasks

### Exercise 00: Functional Purse ([purse.py](src/purse.py))

You need to write functions `add_ingot(purse)`, `get_ingot(purse)` and `empty(purse)` that accept
a purse (a dictionary, which is, strictly speaking, a `typing.Dict[str, int]`) and return a purse
(an empty dict in case of `empty(purse)`). They should not make assumptions about the content of
the purse (it can be empty or store something completely different, like "stones").

Also, your functions shouldn't have side effects. This means, an object passed as an argument
should not be modified inside a function. Instead, a new object should be returned. Thus, you
*shouldn't use the code written by Tom*, as it makes a *direct assignment* to a field inside
a purse. You should return a *new dict instance* with an updated number inside it instead.

So, a function composition like `add_ingot(get_ingot(add_ingot(empty(purse))))` should return
`{"gold_ingots": 1}`. Also, getting an ingot from an empty purse shouldn't lead to an error and
should just return an empty one.

Side note: It doesn't really matter what
happens with the rest of the stuff inside the purse. You can preserve it or throw away.

### Exercise 01: Splitwise ([split_booty.py](src/split_booty.py))

You need to write a function named `split_booty`, which will receive any number of purses (dictionaries) as arguments. Purses in arguments can possibly contain various items, but our men of honor are only interested in gold ingots (named `gold_ingots` as in examples above). Number of ingots can be zero or positive integer.

This function should return three purses (dictionaries) back so that in any two of three purses the difference between the number of ingots is no larger than 1. For example, if the booty includes `{"gold_ingots":3}`, `{"gold_ingots":2}` and `{"apples":10}`, then function should return `({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})`.

While implementing this function you still shouldn't use direct assignment to fields inside dictionaries. You can reuse functions you wrote in EX00 instead.

### Exercise 02: Burglar Alarm ([squeak_decorator.py](src/squeak_decorator.py))

 So far you wrote several functions (`add_ingot(purse)`, `get_ingot(purse)` and `empty(purse)`) for the purse design, but now you need to figure out a way to add some new behaviour to all of them - whenever any of them is called a word `SQUEAK` should be printed. The trick is that you can't modify the body of those functions, but still provide that alarm. The clue that William mentioned about "specific decoration" can possibly help you with that.

-----

### Reading and tips

The rule "do not assign directly" may seem confusing, so here is what's behind it: in functional programming all objects, including data structures, are generally immutable.
That means, it is considered a bad practice to modify the data inside a container, the new container with new value should be created instead.
E.g., if you have a list `a = [1, 2, 3]` and you want to increase the second element by five, instead of writing `a[1] += 5` you should create another object: `b = [a[0], a[1] + 5, a[2]]`.
This approach seems weird, but sometimes when dealing with larger codebase it helps a lot to know that your data won't be accidentally modified at any time somewhere deep in your code, as nothing is mutable.

Also, Python has some immutable object types out of the box. e.g. [frozensets](https://docs.python.org/3/library/stdtypes.html#frozenset).

As an additional cool feature, Python has a built-in way of modifying the behaviour of functions without directly modifying their code.
It is called a `decorator` and is just a special syntax for a function that accepts a function as an argument and returns a function. You can read [this article](https://realpython.com/primer-on-python-decorators/) for more details and examples.
