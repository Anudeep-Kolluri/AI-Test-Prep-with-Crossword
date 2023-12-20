import pygame
import sys

def check_word(current, horizontal):
    if horizontal:
        given_word = ""
        actual_word = ""
        for i in range(current[1], -1, -1):
            if actual_grid[current[0]][i] != ' ':
                given_word += current_grid[current[0]][i]
                actual_word += actual_grid[current[0]][i]
            else:
                break
        given_word = given_word[::-1].lower()
        actual_word = actual_word[::-1].lower()
        print(given_word + actual_word)
        return given_word == actual_word, len(actual_word)
    else:  # Vertical word check
        given_word = ""
        actual_word = ""
        for i in range(current[0], -1, -1):
            if actual_grid[i][current[1]] != ' ':
                given_word += current_grid[i][current[1]]
                actual_word += actual_grid[i][current[1]]
            else:
                break
        given_word = given_word[::-1].lower()
        actual_word = actual_word[::-1].lower()
        print(given_word + actual_word)
        return given_word == actual_word, len(actual_word)
    

def score(current, size, correct, horizontal):
    if horizontal:
            if correct:
                score_grid[current[0]][1+current[1]-size:current[1]] = ['g'] * size
            else:
                score_grid[current[0]][1+current[1]-size:current[1]] = ['r'] * size
    else:  # Vertical word scoring
        if correct:
            for i in range(current[0]-size+1, current[0]+1):
                score_grid[i][current[1]] = 'g'
        else:
            for i in range(current[0]-size+1, current[0]+1):
                score_grid[i][current[1]] = 'r'




# Initialize Pygame
pygame.init()


# Direction
horizontal = True


# Constants
WIDTH, HEIGHT = 600, 600
current_grid_SIZE = 15
CELL_SIZE = WIDTH // current_grid_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
HIGHLIGHT = (255, 255, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the crossword current_grid
current_grid = [[' ' for _ in range(current_grid_SIZE)] for _ in range(current_grid_SIZE)]
score_grid = [[' ' for _ in range(current_grid_SIZE)] for _ in range(current_grid_SIZE)]

# acutal grid
actual_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'o', 'v', 'e', 'r', 'f', 'i', 't', 't', 'i', 'n', 'g'], ['j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'h', 't', 'm', 'l', ' ', ' ', ' '], ['a', ' ', 'h', 'y', 'p', 'e', 'r', 't', 'u', 'n', 'i', 'n', 'g', ' ', ' '], ['v', ' ', ' ', ' ', 'b', 'i', 'n', 'a', 'r', 'y', ' ', ' ', ' ', ' ', ' '], ['a', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '], ['s', ' ', ' ', 'd', 'e', 'b', 'u', 'g', ' ', 'y', ' ', ' ', ' ', ' ', ' '], ['c', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '], ['r', ' ', ' ', ' ', ' ', 'c', 'o', 'd', 'e', 'h', ' ', ' ', ' ', ' ', ' '], ['i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' '], ['p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'n', ' ', ' ', ' ', ' ', ' '], ['t', 'j', 'a', 'v', 'a', ' ', ' ', 'r', 'u', 'b', 'y', ' ', ' ', ' ', ' '], [' ', ' ', 'c', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 's', ' ', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', ' ', ' '], [' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]



# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossword Game')

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
current_word = ""


exit_flag = False
for y in range(current_grid_SIZE):
    for x in range(current_grid_SIZE):
        if actual_grid[y][x] != ' ':
            exit_flag = True
            break
    if exit_flag:
        break

current_cell = [x, y]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the current_grid bounds
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_cell = [mouse_x // CELL_SIZE, mouse_y // CELL_SIZE]
            if 0 <= clicked_cell[0] < current_grid_SIZE and 0 <= clicked_cell[1] < current_grid_SIZE:
                current_cell = clicked_cell


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_cell[0] = min(current_cell[0] + 1, current_grid_SIZE - 1)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                current_cell[0] = max(current_cell[0] - 1, 0)
            elif event.key == pygame.K_DOWN:
                current_cell[1] = min(current_cell[1] + 1, current_grid_SIZE - 1)
            elif event.key == pygame.K_UP:
                current_cell[1] = max(current_cell[1] - 1, 0)
            elif event.key == pygame.K_TAB:
                horizontal = not horizontal
            elif event.key == pygame.K_RETURN:
                correct, size = check_word([current_cell[1], current_cell[0]], horizontal)
                score([current_cell[1], current_cell[0]], size, correct, horizontal)
                # current_cell[1] = min(current_cell[1] + 1, current_grid_SIZE - 1)
                

                
            # elif event.key == pygame.K_BACKSPACE:
            #     current_cell[0] = max(current_cell[0] - 1, 0)
            #     print(current_cell)
            #     current_grid[current_cell[0]][current_cell[1]] = " "

            
                
            # Handle letter input
            elif event.unicode.isalpha():
                current_word += event.unicode.upper()
                
            
            if current_word:
                    
                    if horizontal:
                        # Check if current box is gray or not
                        if actual_grid[current_cell[1]][current_cell[0]] != ' ':

                            current_grid[current_cell[1]][current_cell[0]] = current_word[0]

                            # Check if next box is gray or not
                            prev = current_cell.copy()
                            current_cell[0] = min(current_cell[0] + 1, current_grid_SIZE - 1)
                            if actual_grid[current_cell[1]][current_cell[0]] == ' ':
                                current_cell = prev

                    else:
                        if actual_grid[current_cell[1]][current_cell[0]] != ' ':
                            current_grid[current_cell[1]][current_cell[0]] = current_word[0]

                            # Check if next box is gray or not
                            prev = current_cell.copy()
                            current_cell[1] = min(current_cell[1] + 1, current_grid_SIZE - 1)
                            if actual_grid[current_cell[1]][current_cell[0]] == ' ':
                                current_cell = prev


            current_word = ""

    # Draw the current_grid
    screen.fill(WHITE)
    for y in range(current_grid_SIZE):
        for x in range(current_grid_SIZE):
            # Gray box render
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1) if actual_grid[y][x] != " " else pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Highlight render
            if horizontal:
                if current_cell[1] == y:
                    if actual_grid[current_cell[1]][x] != ' ':
                        pygame.draw.rect(screen, HIGHLIGHT, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

            else:
                if current_cell[0] == x:
                    if actual_grid[y][current_cell[0]] != ' ':
                        pygame.draw.rect(screen, HIGHLIGHT, (current_cell[0] * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, BLACK, (current_cell[0] * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)




            letter = current_grid[y][x]
            if letter != ' ':
                if score_grid[y][x] == 'g':
                    text = font.render(letter, True, GREEN)
                elif score_grid[y][x] == 'r':
                    text = font.render(letter, True, RED)
                else:
                    text = font.render(letter, True, BLACK)
                screen.blit(text, (x * CELL_SIZE + CELL_SIZE // 3, y * CELL_SIZE + CELL_SIZE // 3))

    # Draw the current cell
    pygame.draw.rect(screen, BLACK, (current_cell[0] * CELL_SIZE, current_cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
    

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
