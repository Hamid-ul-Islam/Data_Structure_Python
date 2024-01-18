# Set up drawing variables
drawing = False
last_pos = None
line_color = black
line_width = 2

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # Activate drawing
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False  # Deactivate drawing
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            pygame.draw.line(screen, line_color, last_pos, current_pos, line_width)
            last_pos = current_pos

    pygame.display.flip()
