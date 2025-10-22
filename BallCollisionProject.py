import pygame
import sys

# Importing other local files
from box import Box

# Initializing Pygame
pygame.init()

# Creating our playground window -> 1600 x 900 Resolution -> HD+
Width = 1600
Height = 900

screen = pygame.display.set_mode((Width, Height))

# Labeling the window
pygame.display.set_caption("2D Ball Physics Box Playground")

# Managing frame rates
clock = pygame.time.Clock()

# Making box object
box = Box(Width, Height, margin=150)

# Window set up
window_running = True

# Color themeing
bg_color = (37, 45, 64)

while window_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_running = False
            
    # Adding background color -> Dark-ish gray
    screen.fill(bg_color)
    
    # Drawing our box
    box.draw(screen)
    
    # Updating the screen
    pygame.display.flip()
    
    # Adding FPS limiter -> 165 FPS for my 165 Hz monitor
    clock.tick(165)

# Exitting playground window
pygame.quit()
sys.exit()
