import pygame



class Line:
    """
    The Line object represents a line in 2d space.

    Parameters
    ----------
    start_point: Point.
    start_point is the start Point of the line.

    end_point: Point.
    end_point is the end point of the line.

    color: tuple.
    this is the color of the line.

    width: int.
    this is the width of the line.

    Attributes
    ----------
    self.start : start point of the line.
    self.end : end point of the line.
    self.color : color of the line.
    self.width : width of the line.
    """
    def __init__(self, start_point, end_point, color, width):
        self.start = start_point
        self.end = end_point
        self.color = color
        self.width = width

    def get_start(self):
        """
        returns the start point of the line.
        :return: Point.
        """
        return self.start

    def get_end(self):
        """
        returns the end point of the line.
        :return: Point.
        """
        return self.end

    def get_color(self):
        """
        returns the color of the line.
        :return: tuple.
        """
        return self.color

    def draw_on_board(self, window):
        """
        this function draws the line on the window surface provided.
        :param window: pygame.display
        :return: None.
        """
        pygame.draw.line(window, self.color, (self.start.get_x(), self.start.get_y()),
                         (self.end.get_x(), self.end.get_y()), self.width)

    def set_start(self, new_start):
        """
        update the start point of the line.
        :param new_start: Point.
        :return: None.
        """
        self.start = new_start

    def set_end(self, new_end):
        """
        update the end point of the line.
        :param new_end: Point.
        :return: None.
        """
        self.end = new_end

    def __str__(self):
        """
        used for debugging.. this function prints out the start and end point of the line in 2 tuples.
        :return: None.
        """
        return f'({self.start.get_x()},{self.start.get_y()}), ({self.end.get_x()}, {self.end.get_y()})'

    def __lt__(self, other):
        """
        This function determines if a line is shorter than another line.
        We determine this according to the end point of the line since all lines will have the same
        start point y-coordinate.
        Since the pygame display represents the location of a point starting from the top left as (0,0)
        if a line is shorter than another, then its end point y-coordinate will be larger.
        :param other: Line.
        :return: bool.
        """
        return self.end.get_y() > other.get_end().get_y()

    def __gt__(self, other):
        """
        This function determines if a line is longer than another line.
        We determine this according to the end point of the line since all lines will have the same
        start point y-coordinate.
        Since the pygame display represents the location of a point starting from the top left as (0,0)
        if a line is longer than another, then its end point y-coordinate will be smaller.
        :param other: Line.
        :return: bool.
        """
        return self.end.get_y() < other.get_end().get_y()
