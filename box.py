import pygame

class Box:
    # Initialization function
    def __init__(self, window_width, window_height, margin=150, color=(236, 253, 245), wall_thickness=15):
        self.margin = margin
        self.color = color
        self.wall_thickness = wall_thickness
        
        # Coordinate for Box Left Wall
        self.left_wall = pygame.Rect(
            self.margin,                                                    # x coord
            self.margin,                                                    # y coord
            wall_thickness,                                                 # width
            (window_height - self.margin - wall_thickness) - self.margin    # height
        )
        
        # Coordinate for Box Right Wall
        self.right_wall = pygame.Rect(
            window_width - self.margin - wall_thickness,                    # x
            self.margin,                                                    # y
            wall_thickness,                                                 # width
            (window_height - self.margin - wall_thickness) - self.margin    # height
        )
        
        
        # Coordinate for Box Bottom WAll
        self.bottom_wall = pygame.Rect(
            self.margin,                                  # x
            window_height - self.margin - wall_thickness, # y
            window_width - 2 * self.margin,                 # width
            wall_thickness                                # height
        )
        
    # Drawing the box function
    def draw(self, screen):
        # Drawing left -> right -> bottom walls
        pygame.draw.rect(screen, self.color, self.left_wall)
        pygame.draw.rect(screen, self.color, self.right_wall)
        pygame.draw.rect(screen, self.color, self.bottom_wall)