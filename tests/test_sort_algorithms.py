from logging import Logger
from utils.sort_algorithms import SortAlgorithms
import numpy as np


def numpy_data(file: str):
    # load Numpy array from file
    loaded_array = np.load(f"utils/test_arrays/{file}")
    return loaded_array.tolist()


def test_radix_sort_lsd(
    sort_algorithms: SortAlgorithms, test_logger: Logger, test_params
):
    """
    Test case for Radix Sort LSD (Least Significant Digit) Algorithm
    """
    test_logger.info("Sort Algorithm: RADIX LSD (Least Significant Digit)")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.radix_sort_lsd(array_to_sort) == sorted_array


def test_radix_sort_msd(
    sort_algorithms: SortAlgorithms, test_logger: Logger, test_params
):
    """
    Test case for Radix Sort MSD (Most Significant Digit) Algorithm
    """
    test_logger.info("Sort Algorithm: RADIX MSD (Most Significant Digit)")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.radix_sort_msd(array_to_sort) == sorted_array


def test_bubble_sort(sort_algorithms: SortAlgorithms, test_logger: Logger, test_params):
    """
    Test case for Bubble Sort Algorithm
    """
    test_logger.info("Sort Algorithm: Bubble")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.bubble_sort(array_to_sort) == sorted_array


def test_quick_sort1(sort_algorithms: SortAlgorithms, test_logger: Logger, test_params):
    """
    Test case for Quick Sort1 Algorithm
    """
    test_logger.info("Sort Algorithm: Quick1")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.quick_sort1(array_to_sort) == sorted_array


def test_quick_sort2(sort_algorithms: SortAlgorithms, test_logger: Logger, test_params):
    """
    Test case for Quick Sort2 Algorithm
    """
    test_logger.info("Sort Algorithm: Quick2")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.quick_sort2(array_to_sort) == sorted_array


def test_heap_sort(sort_algorithms: SortAlgorithms, test_logger: Logger, test_params):
    """
    Test case for Heap Sort Algorithm
    """
    test_logger.info("Sort Algorithm: Heap Sort")
    array_to_sort = numpy_data(test_params["array_to_sort"])
    sorted_array = numpy_data(test_params["sorted_array"])

    assert sort_algorithms.heap_sort(array_to_sort) == sorted_array
