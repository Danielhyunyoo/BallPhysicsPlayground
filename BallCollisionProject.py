import pygame
import sys


# Initializing Pygame
pygame.init()

# Creating our playground window
Width = 1000
Height = 800

screen = pygame.display.set_mode((Width, Height))

# Labeling the window
pygame.display.set_caption("2D Ball Physics Box Playground")

# Managing frame rates
clock = pygame.time.Clock()


# Window set up
window_running = True

while window_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_running = False
            
    # Adding background color -> Dark-ish gray
    screen.fill((67, 67, 67))
    
    pygame.display.flip()
    
    # Adding FPS limiter -> 165 FPS for my 165 Hz monitor
    clock.tick(165)

# Exitting playground window
pygame.quit()
sys.exit()
