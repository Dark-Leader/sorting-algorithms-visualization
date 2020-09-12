from helper_functions.helpers import *
import os
from animation.animation import Animation
from animation.background import BackGround
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def main():
    """
    main function to create the display and run the animation.
    """
    # initializing the pygame display.
    pygame.init()
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Sorting Algorithms Visualization")
    icon = pygame.image.load(os.path.join("resources/icon.png"))
    pygame.display.set_icon(icon)
    # crating the lines, background, buttons handler and the animation.
    lines = create_arr_and_lines()
    buttons = create_buttons()
    background = BackGround(WHITE)
    animation = Animation(buttons, background, lines)
    running = True
    # running the animation
    while running:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            animation.update_display(window, mouse)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                animation.choose_algorithm(window, mouse)
    pygame.quit()


if __name__ == "__main__":
    main()
