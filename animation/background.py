class BackGround:
    """
    Simple background for the animation.

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
