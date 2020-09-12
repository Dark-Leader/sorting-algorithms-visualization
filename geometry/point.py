

class Point:
    """
    The Point class represents a point in 2d space.

    Parameters
    ---------
    x : int
    x is the x-coordinate of the point
    y : int
    y is the y-coordinate of the point

    Attributes
    ----------

    self.x : this is where we store the x - coordinate.
    self.y : this is where we store the y - coordinate.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        """
        return x - coordinate
        """
        return self.x

    def get_y(self):
        """
        return y - coordinate
        """
        return self.y

    def set_x(self, new_x):
        """
        updates the x - coordinate.
        :param new_x: int.
        :return: None.
        """
        self.x = new_x

    def set_y(self, new_y):
        """
        update the y - coordinate.
        :param new_y: int.
        :return: None.
        """
        self.y = new_y
