class BackGround:
    """
    Simple background for the animation.
    You can create a more complex background and implement it here if you so choose, make sure to draw it on 
    to the window in the "draw" function.

    Parameters
    ----------

    color : tuple
    represents the background color.

    Attributes
    ----------

    self.color : color of the background.
    """
    def __init__(self, color):
        self.color = color

    def draw(self, win):
        """
        Draw the background to the screen by filling the screen with the background color.
        :param win: pygame.display
        :return: None.
        """
        win.fill(self.color)
