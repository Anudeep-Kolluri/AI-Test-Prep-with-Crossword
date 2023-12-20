import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CROSS WORD")

# Light theme colors
bg_color = (255, 255, 255)  # White background
text_color = (0, 0, 0)  # Black text

# Display title
title_font = pygame.font.Font(None, 72)
title_text = title_font.render("CROSS WORD", True, text_color)
title_rect = title_text.get_rect(center=(width // 2, height // 4))

# Display instructions
font = pygame.font.Font(None, 36)
instruction_text = font.render("Click anywhere to continue", True, text_color)
instruction_rect = instruction_text.get_rect(center=(width // 2, height // 2))

# Input screen
input_font = pygame.font.Font(None, 48)
input_text = input_font.render("Enter a topic:", True, text_color)
input_rect = input_text.get_rect(center=(width // 2, height // 4))
input_box = pygame.Rect(width // 4, height // 2, width // 2, 40)
input_active = False
input_text_value = ""

# Game loop
waiting_for_click = True
waiting_for_topic = False
while waiting_for_click or waiting_for_topic:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if waiting_for_click:
                waiting_for_click = False
                waiting_for_topic = True
            elif waiting_for_topic:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("User entered topic:", input_text_value)
                        waiting_for_topic = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text_value = input_text_value[:-1]
                    else:
                        input_text_value += event.unicode

    # Draw on the screen
    screen.fill(bg_color)  # Fill the screen with white
    
    if waiting_for_click:
        screen.blit(title_text, title_rect)
        screen.blit(instruction_text, instruction_rect)
    elif waiting_for_topic:
        pygame.draw.rect(screen, text_color, input_box, 2)
        input_surface = input_font.render(input_text_value, True, text_color)
        width_diff = (input_box.width - input_surface.get_width()) // 2
        screen.blit(input_text, input_rect)
        screen.blit(input_surface, (input_box.x + width_diff, input_box.y + 10))

    # Update display
    pygame.display.flip()

# Continue with the rest of your game logic after entering the topic
# ...
