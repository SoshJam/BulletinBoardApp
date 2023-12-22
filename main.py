# Import PyGame
import pygame

# Import classes

# Other imports
import sys

# Main program function
def main():
    # Initialize and setup pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Bulletin Board - New Board")

    # Program Variables

    # Main program loop
    while True:

        # Handle Events
        for event in pygame.event.get():

            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Resize the window
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Draw the screen
        screen.fill((255, 255, 255))

        # Update the display
        pygame.display.flip()
        
# Start main function if needed
if __name__ == "__main__":
    main()