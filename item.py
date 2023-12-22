import pygame

# Base item class
class Item:
    # Item info
    x = 0
    y = 0
    data = {}

    def __init__(self, item):
        self.x = item.x
        self.y = item.y
        self.data = item.data

    def draw_item(self, screen):
        # TODO: Figure out the proper width and height. Padding of 10 pixels.
        width = 100
        height = 50

        pygame.draw.rect(screen, (0, 0, 0), (self.x - 2, self.y - 2), (width + 4, height + 4))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y), (width, height))