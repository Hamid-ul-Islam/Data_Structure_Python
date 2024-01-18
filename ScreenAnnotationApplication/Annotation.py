import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Screen Annotation App")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
selected_color = (255, 0, 0)  # Default selected color

# Set up drawing variables
drawing = False
last_pos = None
line_width = 2

def draw_color_palette():
    # Draw a basic color palette
    palette_size = 20
    for i in range(6):
        for j in range(4):
            color = (i * 40, j * 60, 255 - i * 40)
            pygame.draw.rect(screen, color, (width - palette_size * (i + 1), palette_size * j, palette_size, palette_size))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos
            elif event.button == 3:  # Right mouse button
                # Show color palette
                draw_color_palette()
                pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            pygame.draw.line(screen, selected_color, last_pos, current_pos, line_width)
            last_pos = current_pos

    screen.fill(white)  # Clear the screen
    if not drawing:
        draw_color_palette()  # Draw color palette

    pygame.display.flip()
