from shapes.button import Button


class ButtonsHandler:
    """
    The ButtonHandler takes care of all the buttons in the display.

    Parameters
    ----------

    button : list / Button.
    the list of buttons.

    Attributes
    ----------

    self.buttons : list.
    this is where we store the list of buttons.
    """
    def __init__(self, button=None):
        self.buttons = []
        # type checking.
        if isinstance(button, Button):
            self.buttons = [button]
        elif isinstance(button, list):
            for item in button:
                if not isinstance(item, Button):
                    raise Exception("Invalid button provided")
            self.buttons = button
        elif button is None:
            self.buttons = []
        else:
            raise Exception("Invalid button provided")

    def add_button(self, button):
        """
        adding a button.
        :param button: Button.
        :return: None.
        """
        # type checking.
        if isinstance(button, Button) and button not in self.buttons:
            self.buttons.append(button)
        else:
            raise Exception("Invalid button provided")

    def remove_button(self, button):
        """
        remove a button from the list.
        :param button: Button.
        :return: None.
        """
        if button in self.buttons:
            self.buttons.remove(button)
        else:
            print("button not in list")

    def draw_on_board_and_hover(self, position, win):
        """
        draw the buttons on the display and check if the mouse is hovering over one.
        :param position: tuple.
        :param win: pygame.display.
        :return: None.
        """
        for button in self.buttons:
            button.is_hover(position, win)

    def draw_on_board(self, win):
        """
        draw the buttons on the screen without checking if the mouse is hovering over one.
        :param win: pygame.display.
        :return: None.
        """
        for button in self.buttons:
            button.draw_on_window(win)

    def get_buttons(self):
        """
        return the list of buttons.
        :return: None.
        """
        return self.buttons
