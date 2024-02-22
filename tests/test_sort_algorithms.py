from logging import Logger
import pytest
from utils.sort_algorithms import SortAlgorithms


@pytest.fixture
def sort_algorithms():
    sort = SortAlgorithms()
    # setup
    yield sort
    # teardown


def test_radix_sort(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Radix Sort Algorithm
    """
    test_logger.info("Sort Algorithm: RADIX")
    assert sort_algorithms.radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]


def test_bubble_sort(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Bubble Sort Algorithm
    """
    test_logger.info("Sort Algorithm: Bubble")
    assert sort_algorithms.bubble_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]