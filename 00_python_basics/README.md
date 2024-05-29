# Day 00 - Python Bootcamp

Introduction to Python.

Blockchain Analysis, Message Decryption, and Pattern Detection.

## Table of Contents

- [Day 00 - Python Bootcamp](#day-00---python-bootcamp)
  - [Table of Contents](#table-of-contents)
  - [Rules of the day](#rules-of-the-day)
  - [Tips\*](#tips)
  - [Tasks](#tasks)
    - [Exercise 00: Blockchain (blocks.py)](#exercise-00-blockchain-blockspy)
    - [Exercise 01: Decypher (decypher.py)](#exercise-01-decypher-decypherpy)
    - [Exercise 02: Track and Capture (mfinder.py)](#exercise-02-track-and-capture-mfinderpy)
    - [Reading and Tips](#reading-and-tips)
  - [Project status](#project-status)

## Rules of the day

- You should only turn in `*.py` files
- This day's programs in EX00 and EX02 should receive text from standard input and NOT read it from files. EX01 should just receive an input as a command line argument.

## Tips*

To make life easier I create [bash script](./src/test.sh) for testing all of 3 scripts. Just run the command from ./src directory:

```sh
./test.sh
```

## Tasks

### Exercise 00: Blockchain ([blocks.py](./src/ex00/blocks.py))

Given the file `data_hashes.txt`, notice
a pattern - some lines are starting with several zeroes.

Write a Python script which will be able to receive a text from its standard input, and then print out only those lines that start with exactly 5 zeroes.
Only lines that fit into certain criteria are considered valid:

- Correct lines are 32 characters long
- They start with exactly 5 zeroes, so e.g. line starting with 6 zeroes is NOT considered correct

So, for the example above your script should print:

```txt
00000254b208c0f43409d8dc00439896
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v
```

Your code should accept the number of lines as an argument, like this:

`~$ cat data_hashes_10lines.txt | python blocks.py 10`

This way the program will stop when it processed 10 lines. Keep in mind that in this approach
the program may hang if the number of lines in a file is smaller than the one in the argument.
This is not considered an error.

### Exercise 01: Decypher ([decypher.py](./src/ex01/decypher.py))

Decrypt cryptic messages to reveal hidden meanings and identify locations. Create a Python script that accepts a string input and outputs the decrypted message as a single word.

Examples:

- `The only way everyone reaches Brenda rapidly is delivering groceries explicitly`
- `Britain is Great because everyone necessitates`.

Python script should be launchable like this:

`~$ python decypher.py "Have you delivered eggplant pizza at restored keep?"`

and print out the answer as a single word without spaces.

### Exercise 02: Track and Capture ([mfinder.py](./src/ex02/mfinder.py))

Develop a Python script named `mfinder.py` that analyzes a 2D "image" represented as text in a file `m.txt`.

So, as an input your code is given a 2d "image" as text in a file `m.txt`. File contains five characters over three lines, like this:

```txt
*d&t*
**h**
*l*!*
```

You may notice that there is a pattern of stars here, with a letter M. All your code has to do is to print 'True' if this M-pattern exists in a given input image or 'False' otherwise. Other characters (outside the M pattern) should be different, so these examples should print out 'False':

```txt
*****
*****
*****
```

```txt
*s*f*
**f**
*a***
```

If a given pattern is not 3x5, then 'Error' word should be printed instead.
The file with code should be named `mfinder.py`.

### Reading and Tips

`sys` Python module may help you when reading from standard input. Avoid reading the input data
into a data structure like list (if possible), because it is a lot more effective to for-loop
through the lines processing them one by one on the fly.

Python is a high level language, so a lot of operations are already present as methods inside a
standard library, e.g. for strings you can refer to [this link](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
Also, don't forget to `strip()` newline symbols from the lines!

Keep in mind that Python strings are immutable, also unlike in C here you don't need to
pre-allocate memory most of the time, instead just let garbage collector do its job.

It is highly recommended to study [Argparse](<https://docs.python.org/3/howto/argparse.html>) Python module for parsing command
line arguments. It helps to avoid ugly errors on non-valid inputs and generate helpful tips
for the future users of your CLI.

## Project status

Project is: **completed**
