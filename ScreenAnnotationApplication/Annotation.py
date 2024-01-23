import pygame
import sys
hello

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Screen Annotation App")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up drawing variables
drawing = False
last_pos = None
line_color = white
line_width = 2

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            pygame.draw.line(screen, line_color, last_pos, current_pos, line_width)
            last_pos = current_pos

    pygame.display.flip()
