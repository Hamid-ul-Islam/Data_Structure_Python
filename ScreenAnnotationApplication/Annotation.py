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
palette_visible = False  # Initialize palette visibility

# Function to check if a point is inside a rectangle
def is_point_inside_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx < x < rx + rw and ry < y < ry + rh

# Function to get the color under the mouse cursor in the palette
def get_palette_color(mouse_pos):
    palette_size = 20
    for i in range(6):
        for j in range(4):
            rect = (width - palette_size * (i + 1), palette_size * j, palette_size, palette_size)
            if is_point_inside_rect(mouse_pos, rect):
                return (i * 40, j * 60, 255 - i * 40)
    return None

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
                palette_visible = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            pygame.draw.line(screen, selected_color, last_pos, current_pos, line_width)
            last_pos = current_pos

    screen.fill(white)  # Clear the screen

    # Draw color palette if it's visible
    if palette_visible:
        for i in range(6):
            for j in range(4):
                color = (i * 40, j * 60, 255 - i * 40)
                rect = (width - 20 - 20 * i, 20 * j, 20, 20)
                pygame.draw.rect(screen, color, rect)

    # Get the color under the mouse cursor in the palette
    mouse_pos = pygame.mouse.get_pos()
    palette_color = get_palette_color(mouse_pos)

    # Update selected color if a color in the palette is clicked
    if palette_color is not None:
        selected_color = palette_color
        palette_visible = False  # Hide the palette

    pygame.display.flip()
