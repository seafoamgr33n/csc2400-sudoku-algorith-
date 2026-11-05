## ***Part 1: Research Proposal***

Philip Nguyen, Masha Kochan, Katherine Harlow

### 1 \- Problem

The computational problem is generating a sudoku puzzle and creating a solution path. We’re given the rules for a sudoku game, which is that a 9x9 grid must be filled with numbers so that each of the 3x3 subsections and columns and rows contain the numbers 1-9 without repeating. (Wikipedia Contributors (2019)) A sudoku puzzle must also be “well-posed” meaning that it has exactly one solution. Therefore, a valid solution is a full 9x9 grid that follows these criteria, and, for an incomplete puzzle, one solution path that leads to the filled 9x9.   
The problem comes down to generating a sudoku puzzle that actually has one solution, which involves generating a solved 9x9 and possibly backtracking to create an unfilled grid.   
A possible goal is to minimize the number of steps it takes to generate a full, valid puzzle. 

### 2 \- Why This Problem

We picked this problem because of our shared hobby of playing sudoku and curiosity regarding which algorithm would work most efficiently at generating a valid sudoku puzzle.  
Efficiency matters in this case because there are billions of different valid solutions and billions more incorrect combinations. Efficiency in our case involves finding a valid grid in the least amount of steps possible. 

### 3 \- Brute-Force Approach

A brute-force algorithm attempts every solution until a solution is found. For a sudoku puzzle, this could involve testing every number for a specific cell until a valid number is found.  
Using the brute-force approach for sudoku would be very sub-optimal because you can't just try a number and see if it works. The algorithm will only know if the puzzle is right or wrong once the entire puzzle is completed, or it runs into a scenario where the puzzle breaks the rules of sudoku. The algorithm will have to flag only one solution as best because there is exactly one correct solution to a sudoku puzzle, no matter how big or small the puzzle board (input size) is, so. Because of this, brute force would be impractical because there is no way of verifying the puzzle as you go unless you already get it wrong. Big-O notation would take approximately 1 million years.   
Where n is the set of cells needing to be filled, worst case scenario may be testing every single cell, and potentially backtracking every single cell—approximately O(n^n)?

### 4 \- Genetic Algorithms

N/A

### 5 \- Proposed Third Algorithm

A greedy algorithm takes the first available solution—not necessarily the best—and runs with it. (GeeksforGeeks 2021\)  
Therefore, we can use a greedy algorithm to create a solved sudoku. Within the constraints of a puzzle, we will choose the first number that works for each field instead of cycling through the number of available options. For example, if it is determined that a cell can contain a 1, then the algorithm will stop there, fill the cell with a 1, and move to the next cell to be filled.   
This is appropriate for the problem as, in a sudoku grid, as long as all of the rules are followed, it does not matter if a field is filled with a 1 or a 9, and we are aiming to create an efficient algorithm.   
A brute force algorithm, on the other hand, will go through every solution option to see what works, rather than choosing the first, most immediately optimal question. This will likely be slower than a greedy algorithm.

### 6 \- Research Question

How do we reasonably make every filled puzzle random and unique with only one solution?   
How do we keep the solution from backtracking forever?  
How do we create an if/else branch for filling cells that will reduce backtracking?

### 7 \- Experimental Plan

We will compare our algorithms with the execution time, number of operations it takes in order to properly fill the cells of an entire puzzle, and number of iterations it takes in order to create a valid puzzle.

### 8 \- Expected Challenges

The two challenges that we expect to encounter are:

1. A creation of an invalid sudoku puzzle and this challenge will be important because this will help us prevent puzzles that are faulty and ensure that there is only one, unique solution to the puzzle  
2. A lack of data we can use and this challenge will be important because we don’t have a database that we can work with and look at. For us, we are using the rules of sudoku and the numbers 1-9.  
3. Possibly a long simulation time and this challenge will be important because we don’t want an algorithm to take too long to generate a puzzle. We want the algorithm to be as efficient as possible, time-wise and computational-wise.

### 9 \- Sources

Wikipedia Contributors. 2019\. “Sudoku.” Wikipedia, Wikimedia Foundation, October 22\. [https\://en.wikipedia.org/wiki/Sudoku](https://en.wikipedia.org/wiki/Sudoku).

GeeksforGeeks. 2012\. “Algorithm to Solve Sudoku \| Sudoku Solver.” GeeksforGeeks, July 14\. [https\://www\.geeksforgeeks.org/dsa/sudoku-backtracking-7/](https://www.geeksforgeeks.org/dsa/sudoku-backtracking-7/).

GeeksforGeeks. 2021\. “Brute Force Approach and Its Pros and Cons.” GeeksforGeeks, May. [https\://www\.geeksforgeeks.org/dsa/brute-force-approach-and-its-pros-and-cons/](https://www.geeksforgeeks.org/dsa/brute-force-approach-and-its-pros-and-cons/).

### 10 \- Group Expectations

We will distribute one algorithm per group member. We will do our best to check in with each other and not just work on an algorithm and try to join all the work at the very end.  
We will be trying to meet every two weeks at the least, weekly if we can manage.   
We will be communicating through text messages to make sure we are all on the same page.  
Conflicts will be resolved by communication and trying to understand each other’s point of view. We will discuss problems in a group setting and not one-on-one so that we are all on the same page.

