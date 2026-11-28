import random
import copy
import time
import json

# -------------------------------
# ALGORITHM SETUP
# -------------------------------

POPULATION_SIZE = 300
MAX_GENERATIONS = 5000
MUTATION_RATE = 0.30
MAX_RESTARTS = 10
BEST_BOARD_COUNT = 10

# -------------------------------
# GET SUDOKU PUZZLE FROM USER
# -------------------------------

def get_puzzle():
    print("How would you like to enter your Sudoku puzzle?")
    print("1. Load puzzle from JSON file")
    print("2. Enter puzzle manually")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        with open("sudoku.json", "r") as file:
            data = json.load(file)

        puzzle = data["puzzle"]

    elif choice == "2":
        print("\nEnter your Sudoku puzzle.")
        print("Use 0 for empty cells.")
        print("Enter each row as 9 digits (example: 530070000)\n")

        puzzle = []

        for row in range(9):
            while True:
                numbers = input(f"Enter row {row + 1}: ")

                if len(numbers) == 9 and numbers.isdigit():
                    new_row = [int(num) for num in numbers]
                    puzzle.append(new_row)
                    break

                print("Invalid input. Please enter exactly 9 digits.")

    else:
        print("Invalid choice. Please choose 1 or 2.")
        return get_puzzle()

    return puzzle


# -------------------------------
# PUZZLE VALIDATION
# -------------------------------

def validate_puzzle(puzzle):

    if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
        raise ValueError("Puzzle must be a 9x9 grid.")

    for row in range(9):

        for col in range(9):

            num = puzzle[row][col]

            if num not in range(10):
                raise ValueError("Puzzle values must be between 0 and 9.")

            if num == 0:
                continue

            # Check row
            if num in puzzle[row][:col]:
                raise ValueError("Duplicate number in a row.")

            # Check column
            if num in [puzzle[r][col] for r in range(row)]:
                raise ValueError("Duplicate number in a column.")

            # Check 3x3 box
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3

            for r in range(box_row, row + 1):

                for c in range(box_col, box_col + 3):

                    if (r, c) != (row, col):

                        if puzzle[r][c] == num:
                            raise ValueError("Duplicate number in a 3x3 box.")

    return True


# -------------------------------
# CREATE SUDOKU BOARD
# -------------------------------

def create_board(puzzle):

    board = []

    for row in range(9):

        new_row = puzzle[row].copy()

        missing_numbers = [
            num for num in range(1, 10)
            if num not in new_row
        ]

        random.shuffle(missing_numbers)

        for col in range(9):

            if new_row[col] == 0:

                new_row[col] = missing_numbers.pop()

        board.append(new_row)

    return board


# -------------------------------
# CREATE POPULATION
# -------------------------------

def create_population(puzzle):

    return [
        create_board(puzzle)
        for _ in range(POPULATION_SIZE)
    ]


# -------------------------------
# DISPLAY SUDOKU BOARD
# -------------------------------

def display_board(board):

    for row in range(9):

        if row % 3 == 0 and row != 0:
            print("-" * 21)

        for col in range(9):

            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            print(board[row][col], end=" ")

        print()


# -------------------------------
# CALCULATE FITNESS
# -------------------------------

def calculate_fitness(board):

    violations = 0

    # Check columns
    for col in range(9):

        numbers = [board[row][col] for row in range(9)]

        violations += 9 - len(set(numbers))

    # Check 3x3 boxes
    for box_row in range(0, 9, 3):

        for box_col in range(0, 9, 3):

            numbers = []

            for row in range(box_row, box_row + 3):

                for col in range(box_col, box_col + 3):

                    numbers.append(board[row][col])

            violations += 9 - len(set(numbers))

    return violations


# -------------------------------
# SELECTION
# -------------------------------

def selection(population, fitness_scores):

    tournament = random.sample(
        list(zip(population, fitness_scores)), 5
    )

    winner = min(tournament, key=lambda x: x[1])

    return winner[0]


# -------------------------------
# CROSSOVER
# -------------------------------

def crossover(parent1, parent2):

    split = random.randint(1, 8)

    child = (
        [row.copy() for row in parent1[:split]]
        + [row.copy() for row in parent2[split:]]
    )

    return child


# -------------------------------
# MUTATION
# -------------------------------

def mutation(board, puzzle):

    if random.random() < MUTATION_RATE:

        row = random.randint(0, 8)

        empty_positions = [
            col for col in range(9)
            if puzzle[row][col] == 0
        ]

        if len(empty_positions) >= 2:

            col1, col2 = random.sample(empty_positions, 2)

            board[row][col1], board[row][col2] = (
                board[row][col2],
                board[row][col1]
            )

    return board


# -------------------------------
# GENETIC ALGORITHM
# -------------------------------

def genetic_algorithm(puzzle):

    population = create_population(puzzle)

    for generation in range(MAX_GENERATIONS):

        fitness_scores = [
            calculate_fitness(board)
            for board in population
        ]

        ranked = sorted(
            zip(population, fitness_scores),
            key=lambda x: x[1]
        )

        best_board = ranked[0][0]
        best_fitness = ranked[0][1]

        # Check if solution is found
        if best_fitness == 0:

            print("Sudoku solution found!")
            print("Generation:", generation)

            return best_board

        # Keep the best boards
        new_population = [
            copy.deepcopy(board)
            for board, score in ranked[:BEST_BOARD_COUNT]
        ]

        # Create the rest of the population
        while len(new_population) < POPULATION_SIZE:

            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)

            child = crossover(parent1, parent2)

            child = mutation(child, puzzle)

            new_population.append(child)

        population = new_population

        if generation % 100 == 0:

            print(
                "Generation:", generation,
                "| Best fitness:", best_fitness
            )

    print("Maximum generations reached.")

    return None


# -------------------------------
# RANDOM RESTART
# -------------------------------

def solve_sudoku(puzzle):

    for attempt in range(1, MAX_RESTARTS + 1):

        print("\nStarting attempt", attempt)

        solution = genetic_algorithm(puzzle)

        if solution is not None:

            print("\nSuccessful attempt:", attempt)

            return solution

        print("Attempt failed. Creating a new population...")

    print("\nMaximum restart attempts reached.")

    return None


# -------------------------------
# MAIN FUNCTION
# -------------------------------


def main():
    start_time = time.time()

    puzzle = get_puzzle()

    try:
        validate_puzzle(puzzle)
    except ValueError as error:
        print("\nInvalid Sudoku puzzle:", error)

        end_time = time.time()
        print(f"Total Runtime: {end_time - start_time:.2f} seconds")
        return

    print("\nStarting Sudoku Genetic Algorithm...\n")

    solution = solve_sudoku(puzzle)

    if solution is not None:
        print("\nCompleted Sudoku Board:")
        display_board(solution)
    else:
        print("\nUnable to find a solution.")

    end_time = time.time()
    runtime = end_time - start_time

    print(f"\nTotal Runtime: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()
