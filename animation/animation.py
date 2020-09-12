import random
from helper_functions.constants import *
import pygame
import time


class Animation:
    """
    The Animation class takes care of drawing the animation, deciding on which sorting algorithm to run and update
    the display.

    Parameters
    ----------

    handler : ButtonHandler.
    the handler handles how and where to draw the buttons and their functionality.

    background : Background
    background for the animation.

    array : list.
    list of lines.

    Attributes
    ----------

    self.button_handler : ButtonHandler.
    self.background : Background.
    self.arr : list.
    """
    def __init__(self, handler, background, array):
        self.button_handler = handler
        self.background = background
        self.arr = array

    def update_display(self, win, position):
        """
        This function updates the display by drawing the background, buttons, and the array.
        :param win: pygame.display.
        :param position: tuple.
        :return: None.
        """
        self.background.draw(win)
        self.button_handler.draw_on_board_and_hover(position, win)
        for line in self.arr:
            line.draw_on_board(win)
        pygame.display.flip()


    def shuffle_array(self):
        """
        Shuffle the array in place.
        :return: None.
        """
        random.shuffle(self.arr)

    def update_x_start_and_end(self, index):
        """
        update the start and end point x-coordinate.
        :param index: index of the array at which we need to update the start and end point of the line.
        :return: None.
        """
        self.arr[index].get_start().set_x(x_start + index * line_gap)
        self.arr[index].get_end().set_x(x_start + index * line_gap)

    def swap(self, i, j):
        """
        Swap two lines in the array.
        :param i: first index.
        :param j: second index.
        :return: None.
        """
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.update_x_start_and_end(i)
        self.update_x_start_and_end(j)

    def update_entire_array_and_shuffle(self):
        """
        shuffle the array and update the start, end points of the lines.
        :return: None.
        """
        self.shuffle_array()
        for i in range(len(self.arr)):
            self.update_x_start_and_end(i)

    def print_arr(self, win):
        """
        This function draws the background, buttons without updating colors, array to the display.
        :param win: pygame.display.
        :return: None.
        """
        self.background.draw(win)
        self.button_handler.draw_on_board(win)
        for line in self.arr:
            line.draw_on_board(win)
        pygame.display.flip()

    def bubble_sort(self, win):
        """
        This function sorts the array by using the 'bubble sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        n = len(self.arr)
        for i in range(n):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.swap(j, j + 1)
                    self.print_arr(win)
                    time.sleep(0.001)

    def quick_sort(self, left, right, win):
        """
        This function sorts the array by using the 'quick sort' algorithm.
        :param left: int.
        :param right: int.
        :param win: pygame.display.
        :return: None.
        """
        if left >= right:
            return
        pivot = self.partition(left, right, win)
        self.quick_sort(left, pivot - 1, win)
        self.quick_sort(pivot + 1, right, win)

    def partition(self, left, right, win):
        """
        This is a helper function of quick sort that chooses a partition that all lines to left are shorter
        than it and all lines to the right are longer than it.
        :param left: int.
        :param right: int.
        :param win: pygame.display.
        :return: None.
        """
        pivot = self.arr[right]
        i = left - 1
        for j in range(left, right):
            if self.arr[j] < pivot:
                i += 1
                self.swap(i, j)
                self.print_arr(win)
                time.sleep(0.01)
        i += 1
        self.swap(i, right)
        self.print_arr(win)
        return i

    def selection_sort(self, win):
        """
        This function sorts the array by using the 'selection sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        size = len(self.arr)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            self.swap(i, min_index)
            self.print_arr(win)
            time.sleep(0.02)

    def merge_sort(self, main_arr, start_index, end_index, auxiliary_arr, win):
        """
        This function sorts the array by using the 'merge sort' algorithm with an auxiliary array for the swaps,
        array updates.
        :param main_arr: list.
        :param start_index: int.
        :param end_index: int.
        :param auxiliary_arr: list.
        :param win: pygame.display.
        :return: None.
        """
        if start_index == end_index:
            return
        middle_index = (start_index + end_index) // 2
        self.merge_sort(auxiliary_arr, start_index, middle_index, main_arr, win)
        self.merge_sort(auxiliary_arr, middle_index + 1, end_index, main_arr, win)
        self.merge(main_arr, start_index, middle_index, end_index, auxiliary_arr, win)

    def merge(self, main_arr, start_index, middle_index, end_index, auxiliary_arr, win):
        """
        This is a helper function to the merge_sort function.
        It sorts the array by splitting it into 2 parts, and then updates the array according to the auxiliary array.
        :param main_arr: list.
        :param start_index: int.
        :param middle_index: int.
        :param end_index: int.
        :param auxiliary_arr: list.
        :param win: pygame.display.
        :return: None.
        """
        k = start_index
        i = start_index
        j = middle_index + 1
        while i <= middle_index and j <= end_index:
            if auxiliary_arr[i] < auxiliary_arr[j]:
                main_arr[k] = auxiliary_arr[i]
                i += 1
            else:
                main_arr[k] = auxiliary_arr[j]
                j += 1
            self.update_x_start_and_end(k)
            self.print_arr(win)
            time.sleep(0.005)
            k += 1
        while i <= middle_index:
            main_arr[k] = auxiliary_arr[i]
            self.update_x_start_and_end(k)
            self.print_arr(win)
            time.sleep(0.005)
            i += 1
            k += 1
        while j <= end_index:
            main_arr[k] = auxiliary_arr[j]
            self.update_x_start_and_end(k)
            self.print_arr(win)
            time.sleep(0.005)
            j += 1
            k += 1

    def iterative_merge_sort(self, win):
        """
        This function sorts the array by using 'merge sort' algorithm but instead of recursion, using iteration.
        :param win: pygame.display.
        :return: None.
        """
        current_size = 1
        while current_size < len(self.arr) - 1:
            left = 0
            while left < len(self.arr) - 1:
                mid = min((left + current_size - 1), len(self.arr) - 1)
                right = ((2 * current_size + left - 1, len(self.arr) - 1)[2 * current_size + left - 1 >
                                                                          len(self.arr) - 1])
                self.iterative_merge_helper(left, mid, right, win)
                left = left + current_size * 2

            current_size = 2 * current_size

    def iterative_merge_helper(self, left_index, mid_index, right_index, win):
        """
        This is a helper function to the iterative merge sort function.
        it splits the segments into to two parts each time and sorts each part before merging them together.
        :param left_index: int.
        :param mid_index: int.
        :param right_index: int.
        :param win: pygame.display.
        :return: None.
        """
        left_bound = mid_index - left_index + 1
        right_bound = right_index - mid_index
        left_side = [0] * left_bound
        right_side = [0] * right_bound
        for i in range(0, left_bound):
            left_side[i] = self.arr[left_index + i]
        for i in range(0, right_bound):
            right_side[i] = self.arr[mid_index + i + 1]

        i, j, k = 0, 0, left_index
        while i < left_bound and j < right_bound:
            if left_side[i] > right_side[j]:
                self.arr[k] = right_side[j]
                self.update_x_start_and_end(k)
                self.print_arr(win)
                j += 1
            else:
                self.arr[k] = left_side[i]
                self.update_x_start_and_end(k)
                self.print_arr(win)
                i += 1
            k += 1
            time.sleep(0.01)

        while i < left_bound:
            self.arr[k] = left_side[i]
            self.update_x_start_and_end(k)
            self.print_arr(win)
            i += 1
            k += 1
            time.sleep(0.01)

        while j < right_bound:
            self.arr[k] = right_side[j]
            self.update_x_start_and_end(k)
            self.print_arr(win)
            j += 1
            k += 1
            time.sleep(0.01)

    def heapify(self, size, root_index, win):
        """
        This is a helper function for the 'heap sort' function, it performs the 'heapify' algorithm on the array.
        :param size: int.
        :param root_index: int.
        :param win: pygame.display.
        :return: None.
        """
        largest_value = root_index
        left = largest_value * 2 + 1
        right = largest_value * 2 + 2
        if left < size and self.arr[root_index] < self.arr[left]:
            largest_value = left
        if right < size and self.arr[largest_value] < self.arr[right]:
            largest_value = right
        if largest_value != root_index:
            self.swap(root_index, largest_value)
            self.print_arr(win)
            time.sleep(0.01)
            self.heapify(size, largest_value, win)

    def heap_sort(self, win):
        """
        This function sorts the array by using the 'heap sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(size, i, win)

        for i in range(size - 1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0, win)

    def insertion_sort(self, win):
        """
        This function sorts the array by using the 'inserting sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                self.update_x_start_and_end(j + 1)
                self.print_arr(win)
                j -= 1
            self.arr[j + 1] = key
            self.update_x_start_and_end(j + 1)
            self.print_arr(win)

    def bucket_sort(self, win):
        """
        This function sorts the array by using the 'bucket sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        bucket_size = 100
        minimum = maximum = self.arr[0]
        for i in range(1, len(self.arr)):
            if self.arr[i] < minimum:
                minimum = self.arr[i]
            elif self.arr[i] > maximum:
                maximum = self.arr[i]
        num_of_buckets = ((minimum.get_end().get_y() - maximum.get_end().get_y()) // bucket_size) + 1
        buckets = []
        for i in range(num_of_buckets):
            buckets.append([])
        for i in range(0, len(self.arr)):
            # create the buckets.
            buckets[(self.arr[i].get_end().get_y() - maximum.get_end().get_y()) // bucket_size].append(self.arr[i])
            time.sleep(0.02)
        k = 0
        for i in range(len(buckets) - 1, - 1, -1):
            # sort each bucket.
            self.bucket_sort_helper(buckets[i])
            time.sleep(0.02)
            for j in range(len(buckets[i]) - 1, - 1, -1):
                # update the array.
                self.arr[k] = buckets[i][j]
                self.update_x_start_and_end(k)
                self.print_arr(win)
                k += 1
                time.sleep(0.02)

    def bucket_sort_helper(self, array):
        """
        This is a helper function of the 'bucket sort' function, it sorts an array by using
        the inserting sort algorithm.
        :param array: list.
        :return: None.
        """
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key.get_end().get_y() < array[j].get_end().get_y():
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    def radix_sort(self, win):
        """
        This function sorts the array by using the 'radix sort' algorithm.
        :param win: pygame.display.
        :return: None.
        """
        max1 = min(self.arr).get_end().get_y()
        exp = 1
        while max1 / exp > 1:
            self.counting_sort(exp, win)
            exp *= 10

    def counting_sort(self, exp, win):
        """
        This is a helper function of the radix sort function, it sorts the array by using 'counting sort'
        on the array according to the exponent provided.
        :param exp: int.
        :param win: pygame.display.
        :return: None.
        """
        size = len(self.arr)
        output = [0] * size
        count = [0] * 10
        for i in range(size):
            # counting the amount of times each digit is in the lines.
            index = self.arr[i].get_end().get_y() / exp
            count[9 - int(index % 10)] += 1
        for i in range(1, 10):
            # update the counts.
            count[i] += count[i - 1]
        for i in range(size - 1, -1, -1):
            # updating the count, output array.
            index = self.arr[i].get_end().get_y() / exp
            output[count[9 - int(index % 10)] - 1] = self.arr[i]
            count[9 - int(index % 10)] -= 1
        for i in range(size):
            # update the array.
            self.arr[i] = output[i]
            self.update_x_start_and_end(i)
            self.print_arr(win)
            time.sleep(0.01)

    def choose_algorithm(self, win, position):
        """
        This function is responsible for choosing which sorting algorithm to perform on the array by
        checking which button got clicked and thus deciding which sorting algorithm to perform.
        :param win: pygame.display.
        :param position: tuple.
        :return: None.
        """
        for button in self.button_handler.get_buttons():
            if button.clicked_on(position):
                name = button.get_name()
                if name == "Quick Sort":
                    self.quick_sort(0, len(self.arr) - 1, win)
                elif name == "Merge Sort":
                    # self.iterative_merge_sort(win) # you can choose to use the iterative merge sort or
                    # recursive merge sort.
                    self.merge_sort(self.arr, 0, len(self.arr) - 1, self.arr.copy(), win)
                elif name == "Selection Sort":
                    self.selection_sort(win)
                elif name == "Heap Sort":
                    self.heap_sort(win)
                elif name == "Bubble Sort":
                    self.bubble_sort(win)
                elif name == "Shuffle Array":
                    self.update_entire_array_and_shuffle()
                elif name == "Bucket Sort":
                    self.bucket_sort(win)
                elif name == "Insertion Sort":
                    self.insertion_sort(win)
                elif name == "Radix Sort":
                    self.radix_sort(win)
