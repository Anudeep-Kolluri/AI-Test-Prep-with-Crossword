import random

def create_crossword(words, grid_size=15, padding=1):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    placed_words = {}

    def try_place_word(word):
        directions = [(0, 1), (1, 0)]  # across, down

        for _ in range(10):
            direction = random.choice(directions)
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)

            if direction == (0, 1) and col + len(word) + padding <= grid_size:
                intersecting_cells = [(row, col + i) for i in range(padding, len(word) + padding)]
            elif direction == (1, 0) and row + len(word) + padding <= grid_size:
                intersecting_cells = [(row + i, col) for i in range(padding, len(word) + padding)]
            else:
                continue

            conflict = any(grid[r][c] != ' ' for r, c in intersecting_cells)

            if not conflict:
                for i, (r, c) in enumerate(intersecting_cells):
                    grid[r][c] = word[i]
                    if (r, c) not in placed_words:
                        placed_words[(r, c)] = []
                    placed_words[(r, c)].append((word[i], i == 0))  # Mark the starting position
                return True

        return False

    def is_connected():
        visited = set()
        stack = [(0, 0)]

        while stack:
            current_cell = stack.pop()
            visited.add(current_cell)

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current_cell[0] + dr, current_cell[1] + dc)
                if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size and neighbor not in visited:
                    stack.append(neighbor)

        return len(visited) == grid_size * grid_size

    def fill_grid():
        for word in words:
            success = False
            for _ in range(50):
                if try_place_word(word):
                    success = True
                    break
            if not success:
                return False

        return is_connected()

    while not fill_grid():
        grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        placed_words = {}

    return grid

def print_crossword(grid):
    for row in grid:
        for cell in row:
            if isinstance(cell, tuple):
                print(cell[0], end=' ')
            else:
                print(cell, end=' ')
        print()

# Example usage:
word_list = ["python", "java", "ruby", "javascript", "html", "css", "algorithm", "code", "program", "debug", "binary", "hypertuning", "overfitting"]
crossword_grid = create_crossword(word_list, padding=1)

if crossword_grid:
    print(crossword_grid)
    print_crossword(crossword_grid)
else:
    print("Failed to create a fully connected crossword.")
