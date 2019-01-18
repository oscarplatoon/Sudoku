# Sudoku
Many people will spend hours in their spare time solving Sudoku problems, but by the end of this challenge you'll have a solver that can handle any valid Sudoku problem. Some of you have maybe never heard of Sudoku. If not, you should check it out [here](https://en.wikipedia.org/wiki/Sudoku).

As developers, we very often have to jump into unknown territory with no training. You get to jump into that this weekend with learning about Python's [CSV library](https://docs.python.org/3/library/csv.html). Don't worry if you get stuck, we'll be going over it next week as well. Maybe you want to look ahead in our curriculum to help guide you?

## Premise
The idea is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid (also called "boxes") contains all of the digits from 1 to 9.

The person who created the puzzle provides a partial solution so that some squares already have numbers. Typically, there are enough initial numbers to guarantee a unique solution.

Something that starts like this will be solved and turned into this:

![](http://image.slidesharecdn.com/americanpoplanguage-150127095610-conversion-gate01/95/americanpoplanguage-23-638.jpg?cb=1422352672)

## The Rules
We'll use the traditional board layout/style. A puzzle is made up of:

* a *spot* holds a single number 1-9
* a *square* is a 3x3 group of spots
* a *board* is made up of a 3x3 group of squares
* a *row* spans nine squares in a straight line left-to-right across the board
* a *column* spans nine squares in a straight line top-to-bottom across the board
* at the start of a Sudoku game, one or more spots are blank

A valid solution is made up of:

* each square has each number 1-9
* each *row* has each number 1-9
* each *column* has each number 1-9
* each square, column, and row must have the numbers 1-9 in them and cannot have duplicates

## Pseudocode
It is highly suggested that you try to solve this problem and model it out before jumping into the code. You can do this by asking yourself how you would solve this as a human. Take note of how you solve this problem:

* What strategies are you adopting and why?
* Where/how are you choosing to start?
* How can you be sure that the number you put in a cell is the right number?
* Is there any strategy you're avoiding because it requires you to remember too much?
* How would those approaches translate to code? 
* Are there some core methods that will need to be implemented?

It's important to see that sometimes the strategies that work for us (humans) would be really hard to implement on a computer, and vice versa: strategies we avoid because we'd have to write too much, use too many sheets of paper, or remember too much are a cakewalk for a computer.

## Starting Off
Your program will need to take in a string like this like below. Note that blank spaces are written as `0`'s.
```python
game = SudokuSolver("619030040270061008000047621486302079000014580031009060005720806320106057160400030")
game.solve()
print(game.board)

```

And should output something like this,
```text
---------------------
4 8 3 | 9 2 1 | 6 5 7
9 6 7 | 3 4 5 | 8 2 1
2 5 1 | 8 7 6 | 4 9 3
---------------------
5 4 8 | 1 3 2 | 9 7 6
7 2 9 | 5 6 4 | 1 3 8
1 3 6 | 7 9 8 | 2 4 5
---------------------
3 7 2 | 6 8 9 | 5 1 4
8 1 4 | 2 5 3 | 7 6 9
6 9 5 | 4 1 7 | 3 8 2
---------------------
```

### Release 0 : Modeling

**Modeling: Write down the nouns and verbs of the game**

For the first iteration, we're just going build a solver that fills in "logically necessary" squares and requires no guessing.

Think carefully about all the nouns and verbs in a Sudoku game. There's the person who created the puzzle (the setter). There's the person who is solving the puzzle (the player). What are the important parts of the board called? How do the player and setting interact with them?

A computer program that solves Sudoku is simulating the *player*, which means the better you can empathize with the player the more likely you'll understand how to write a Sudoku solver. You'll be tempted to focus on the board first—is it some kind of array, a hash, something else?—but don't! Understanding the person playing the game is key, the code to "power" the board is a detail.

**HINT:** given a cell/square, you'll probably need at least three methods:

1. Give me the other cells in that cell's row.
2. Give me the other cells in that cell's column.
3. Give me the other cells in that cell's box.

### Release 1: Code!
This first iteration might not solve every possible Sudoku board. This means it would finish when it can no longer make a choice and "give up." We'll create the fully-featured version in the next release.

**When you're done with release 1, make sure you commit your changes to have a reference point before jumping to release 2**

### Release 2: Iterate on the finished product on release 1
This second iteration will include the "guessing" portion of Sudoku. What happens if a square can contain multiple possible numbers and you don't have enough information to conclude right then and there which number it is?

Most people who play Sudoku "guess," usually by writing possibilities in the corners of the square. Your program has to do this kind of guessing as well. Would recursion be useful here?
