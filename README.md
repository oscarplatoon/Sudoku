# Rudoku

Many people will spend hours in their spare time solving Soduku problems, but by the end of this challenge you'll have a solver that can handle any valid Sodoku problem.

Some of you have maybe never heard of Sodoku, if not You should check it out [here](https://en.wikipedia.org/wiki/Sudoku)

## Premise

The idea is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid (also called "boxes") contains all of the digits from 1 to 9.

Something that starts like this will be solved and turned into this:

![](http://image.slidesharecdn.com/americanpoplanguage-150127095610-conversion-gate01/95/americanpoplanguage-23-638.jpg?cb=1422352672)

## The Rules

We'll use the traditional board layout/style. A puzzle is made up of:

* a *spot* holds a single number 1-9
* a *square* is a 3x3 group of spots
* a *board* is made up of a 3x3 group of squares
* a *row* spans nine squares in a straight line left-to-right across the board
* a *column* spans nine squares in a straight line top-to-bottom across the board
* at puzzle-start, one or more spots are blank

A valid solution is made up of:

* each square has each number 1-9
* each *row* has each number 1-9
* each *column* has each number 1-9

## Pseudocode

It is highly suggested that you try to model this problem space out before jumping into the code. You can do this by asking yourself how you would solve this as a human. Take note of how you solve this problem:

Where are you choosing to start?
How can you be sure that the number you put in a cell is the right number?
Is there any strategy you're avoiding because it requires you to remember too much?

How would those approaches translate to code? Are there some core methods that will need to be implemented?

## Starting Off

Your program will need to take in a string like this, "619030040270061008000047621486302079000014580031009060005720806320106057160400030
"
```ruby
game = Rudoku.new("619030040270061008000047621486302079000014580031009060005720806320106057160400030")
game.solve!
puts game.board

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

## Some Thoughts
Optimizing for speed shouldn't be the goal of this right now. Instead optimize for readability. Performance optimizations will come later.
