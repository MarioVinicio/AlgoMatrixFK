from logging import Logger
import time
import pytest
from utils.sort_algorithms import SortAlgorithms


@pytest.fixture
def sort_algorithms():
    sort = SortAlgorithms()
    # setup
    yield sort
    # teardown


@pytest.fixture
def measure_sort_time(request, test_logger: Logger):
    start_time = time.time()

    def finalizer():
        end_time = time.time()
        elapsed_time = end_time - start_time
        test_logger.info(f"Sort time: {elapsed_time:.6f} seconds")

    request.addfinalizer(finalizer)


@pytest.mark.usefixtures("measure_sort_time")
def test_radix_sort(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Radix Sort Algorithm
    """
    test_logger.info("Sort Algorithm: RADIX")
    assert sort_algorithms.radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]


@pytest.mark.usefixtures("measure_sort_time")
def test_bubble_sort(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Bubble Sort Algorithm
    """
    test_logger.info("Sort Algorithm: Bubble")
    assert sort_algorithms.bubble_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]


@pytest.mark.usefixtures("measure_sort_time")
def test_quick_sort1(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Quick Sort1 Algorithm
    """
    test_logger.info("Sort Algorithm: Quick1")
    assert sort_algorithms.quick_sort1([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]


@pytest.mark.usefixtures("measure_sort_time")
def test_quick_sort2(sort_algorithms: SortAlgorithms, test_logger: Logger):
    """
    Test case for Quick Sort2 Algorithm
    """
    test_logger.info("Sort Algorithm: Quick2")
    assert sort_algorithms.quick_sort2([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]
