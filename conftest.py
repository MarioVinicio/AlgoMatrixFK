import os
import time
import pytest
import yaml
import logging
from utils.sort_algorithms import SortAlgorithms
from logging import Logger


"""
Fixture to setup logging
"""


@pytest.fixture
def test_logger(request):
    # Get the name of the currently executing test
    test_name = request.node.name

    # Create logger for the test
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)

    # Create a directory for test logs if it doesn't exist
    log_dir = "test_logs"
    os.makedirs(log_dir, exist_ok=True)

    # Create a file to capture the test output
    log_file_path = f"{log_dir}/{test_name}.log"
    # Create a file handler for the test-specific log file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    # add the file handler to the logger
    logger.addHandler(file_handler)

    yield logger  # This is the fixture value that will be injected into the test

    # Optionally, perform teardown or cleanup actions after the test
    logger.removeHandler(file_handler)


"""
Run tests from YAML file
"""

YAML_FILE_PATH = "tests/sort_algorithms.yaml"


def pytest_generate_tests(metafunc):
    if "test_params" in metafunc.fixturenames:
        with open(YAML_FILE_PATH, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
            # Provide the list of dictionaries containing parameters
            metafunc.parametrize("test_params", data["tests"], ids=lambda x: x["name"])


@pytest.fixture
def test_params(request):
    return request.param


@pytest.fixture
def sort_algorithms(measure_sort_time):
    sort = SortAlgorithms()
    # setup
    yield sort
    # teardown


@pytest.fixture
def measure_sort_time(request: pytest.FixtureRequest, test_logger: Logger):
    """Automatically print run time for each test"""

    start_time = time.time()

    def print_sort_time():
        end_time = time.time()
        elapsed_time = end_time - start_time
        test_logger.info(f"Sort time: {elapsed_time:.6f} seconds")

    request.addfinalizer(print_sort_time)
