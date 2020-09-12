import pygame

class Button:
    """
    The Button class represents a button on the animation, each button has color, hover color, name, and dimensions -
    top left point coordinates and width, height.

    Parameters
    ----------

    x : int.
    top left point x-coordinate.

    y : int.
    top left point y-coordinate.

    width : int.
    button width.

    height: int.
    button height.

    color: tuple.
    color of the button.

    hover_color : tuple.
    color of the button whenever the mouse is hovering over the button.

    name : str.
    the name of the button, meaning which sorting algorithm it represents.

    Attributes
    ----------

    self.x : top left point x-coordinate.
    self.y : top left point y-coordinate.
    self.width : button width.
    self.height : button height.
    self.color : base button color (when the mouse does not hover on the button).
    self.hover_color : button color if the mouse hovers over it.
    self.display_color : the color of the button when it is being displayed.
    self.name : button name.
    """
    def __init__(self, x, y, width, height, color, hover_color, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.display_color = self.color
        self.name = name

    def draw_on_window(self, window):
        """
        Draw the button on the display provided, first we draw a rect representing the button.
        then we type the button name inside it.
        :param window: pygame.display
        :return: None.
        """
        BLACK = (0, 0, 0)
        pygame.draw.rect(window, self.display_color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 20)
        text = font.render(self.name, 1, BLACK)
        window.blit(text, ((self.x + self.width) / 3 + 5, (self.y * 2 + self.height) // 2 - 5))

    def is_hover(self, position, window):
        """
        check if the mouse is hovering over the button by checking the x,y coordinates of the mouse and draw the button
        to the display.
        :param position: tuple.
        :param window: pygame.display
        :return: None.
        """
        x, y = position
        # check if the mouse the hovering over the button.
        if self.clicked_on(position):
            # if it does update the button color.
            self.display_color = self.hover_color
        else:
            # if not update the button color.
            self.display_color = self.color
        # draw the button on the display.
        self.draw_on_window(window)

    def clicked_on(self, position):
        """
        Check if the mouse clicked on the button.
        :param position: tuple.
        :return: bool.
        """
        x, y = position
        return self.x <= x <= (self.x + self.width) and self.y <= y <= (self.y + self.height)

    def get_name(self):
        """
        return the name of the button.
        :return: str.
        """
        return self.name
