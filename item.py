import pygame

# Base item class
class Item:
    # Setup for text
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 12)

    # Item info
    x = 0
    y = 0
    data = {}

    def __init__(self, item):
        self.x = item['x']
        self.y = item['y']
        self.data = item['data']

    def draw_item(self, screen):
        # TODO: Figure out the proper width and height. Padding of 10 pixels.
        width = 200
        height = 50

        pygame.draw.rect(screen, (0, 0, 0), (self.x - 2, self.y - 2, width + 4, height + 4))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, width, height))

# More specific classes
        
# Basic text
class Text(Item):

    def draw_item(self, screen):
        # Draw the card
        super().draw_item(screen)

        # Draw the text
        text = self.font.render(self.data['text'], True, (0, 0, 0))
        screen.blit(text, (self.x + 10, self.y + 10))

# Todo List
class Todo(Item):

    def draw_item(self, screen):
        # Draw the card
        super().draw_item(screen)

        pass

# Link to a website
class Link(Item):

    def draw_item(self, screen):
        # Draw the card
        super().draw_item(screen)

        pass

# Link to another board
class BoardLink(Item):

    def draw_item(self, screen):
        # Draw the card
        super().draw_item(screen)

        pass