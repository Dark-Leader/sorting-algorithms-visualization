import random
from geometry.point import Point
from geometry.line import Line
from helper_functions.constants import *
from shapes.buttons_handler import ButtonsHandler
from shapes.button import Button


def create_buttons():
    """
    This function creates the buttons for the animation and holds them together inside a ButtonHandler.
    :return: ButtonHandler
    """
    buttons = []
    names = ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Heap Sort", "Insertion Sort",
             "Bucket Sort", "Radix Sort", "Shuffle Array"]
    j = 0
    colors = [RED, LIGHT_RED, GREEN, LIGHT_GREEN, BLUE, LIGHT_BLUE, YELLOW,
              LIGHT_YELLOW, PURPLE, LIGHT_PURPLE, PINK, LIGHT_PINK, ORANGE, LIGHT_ORANGE, CYAN, DARK_CYAN,
              DARK_PURPLE, MAGENTA]
    for i in range(0, len(colors) - 1, 2):
        button = Button(x_start_button, y_start_button + button_height * j + button_gap * j, button_width,
                        button_height, colors[i], colors[i+1], names[j])
        buttons.append(button)
        j += 1

    buttons_handler = ButtonsHandler(buttons)
    return buttons_handler


def create_arr_and_lines():
    """
    This function creates the lines for the animation.
    :return: list.
    """
    numbers = list(range(line_gap - 2, lines_end + line_gap * 5, 5))
    shuffle_arr(numbers)
    arr = []
    for i in range(len(numbers)):
        start_point = Point(x_start + line_gap * i, y_start)
        end_point = Point(x_start + line_gap * i, y_start - numbers[i])
        line = Line(start_point, end_point, VALUE_COLOR, line_width)
        arr.append(line)
    return arr


def shuffle_arr(arr):
    """
    Shuffle the array provided in place.
    :param arr: list.
    :return: None.
    """
    random.shuffle(arr)
