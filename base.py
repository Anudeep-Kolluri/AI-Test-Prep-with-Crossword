import pygame
import sys

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

# Create the crossword current_grid
current_grid = [[' ' for _ in range(current_grid_SIZE)] for _ in range(current_grid_SIZE)]

# acutal grid


# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossword Game')

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
current_cell = [0, 0]
current_word = ""

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
            elif event.key == pygame.K_DOWN or event.key == pygame.K_RETURN:
                current_cell[1] = min(current_cell[1] + 1, current_grid_SIZE - 1)
            elif event.key == pygame.K_UP:
                current_cell[1] = max(current_cell[1] - 1, 0)

                
            # elif event.key == pygame.K_BACKSPACE:
            #     current_cell[0] = max(current_cell[0] - 1, 0)
            #     print(current_cell)
            #     current_grid[current_cell[0]][current_cell[1]] = " "

            
                
            # Handle letter input
            elif event.unicode.isalpha():
                current_word += event.unicode.upper()
                
            
            if current_word:
                    current_grid[current_cell[1]][current_cell[0]] = current_word[0]
                    current_cell[0] = min(current_cell[0] + 1, current_grid_SIZE - 1)
            current_word = ""

    # Draw the current_grid
    screen.fill(WHITE)
    for y in range(current_grid_SIZE):
        for x in range(current_grid_SIZE):
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            letter = current_grid[y][x]
            if letter != ' ':
                text = font.render(letter, True, BLACK)
                screen.blit(text, (x * CELL_SIZE + CELL_SIZE // 3, y * CELL_SIZE + CELL_SIZE // 3))

    # Draw the current cell
    pygame.draw.rect(screen, BLACK, (current_cell[0] * CELL_SIZE, current_cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
    

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
