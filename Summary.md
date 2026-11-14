# Project Summary: Dice Rolling Game

## What I Did
I created a console-based Dice Rolling Game using Python 3. The program asks the user to enter the number of times to roll a six-sided die. It uses Python's `random` module to generate each roll.

I used a list to keep track of the frequency of faces 1 to 6. The program then calculates and displays the total and average of the rolls. It also identifies the face or faces that occurred most often. If two or more faces have the same highest frequency, the program displays all of them.

I added input validation so that the number of rolls must be a whole number from 1 to 1000. Finally, I added an option to play the game again.

## Challenges I Faced and How I Addressed Them
The following are the main challenges considered while developing the project. Edit these points if your actual experience was different.

1. **Counting the frequency of each face:** I needed a clear way to count how many times each number appeared. I used a list with six positions and updated the correct position after every roll.
2. **Matching dice faces with list positions:** Python list indexing starts at 0, while dice faces start at 1. I handled this by using `result - 1` as the list index.
3. **Finding the most frequent face:** More than one face can have the same highest frequency. I used the maximum frequency and checked all six faces so that ties are displayed too.
4. **Handling invalid input:** Text, zero, negative numbers, and numbers above 1000 should not be accepted. I used `try`/`except` for non-integer input and a condition to check the allowed range.

## Concepts Learned
- Using the `random` module
- Writing and calling functions
- Using `for` and `while` loops
- Working with lists
- Applying conditions
- Handling invalid input with exception handling
- Calculating total, average, and frequency

## Conclusion
This project helped me practise basic Python programming concepts by applying them to a simple dice game. It also helped me understand how to organize a program into functions and validate user input.
