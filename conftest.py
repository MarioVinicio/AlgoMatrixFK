import os
import pytest
import logging

"""
Using pytest hooks:
pytest provides hooks that you can use to customize test runs. 
"""


def pytest_runtest_protocol(item, nextitem):
    """
    hook to print information before and after each test.
    """
    print(f"\nRunning test: {item.nodeid}")


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
    print(f"\nLog file path: {log_file_path}")
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
