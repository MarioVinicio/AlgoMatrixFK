# AlgoMatrixFK

A pytest-based benchmarking framework for measuring and comparing the execution speed of sorting algorithm implementations across multiple data distribution scenarios.

## Algorithms

| Algorithm | Variant |
|---|---|
| Radix Sort | LSD (Least Significant Digit) |
| Radix Sort | MSD (Most Significant Digit) |
| Bubble Sort | — |
| Quick Sort | Variant 1 |
| Quick Sort | Variant 2 |
| Heap Sort | — |
| Python built-in `sorted()` | New list |
| Python built-in `.sort()` | In-place |

## Test Datasets

All algorithms are tested against the following NumPy array distributions:

- `descending_order` — worst case for most comparison-based sorts
- `random_order` — average case
- `already_sorted` — best case
- `with_duplicates` — stability and deduplication stress
- `single_unique_value` — degenerate input
- `very_large_array` — scalability and performance ceiling

## Project Structure

```
AlgoMatrixFK/
├── utils/
│   └── sort_algorithms.py   # Algorithm implementations
├── tests/
│   └── test_sort_algorithms.py  # Parametrized benchmark tests
├── test_logs/               # Captured test output and timing logs
├── conftest.py              # Shared fixtures and dataset setup
├── pytest.ini               # Pytest configuration
└── run_tests.sh             # Entry point script
```

## Requirements

```bash
pip3 install pytest PyYAML numpy
```

## Usage

```bash
./run_tests.sh
```

Or run pytest directly with verbose output:

```bash
pytest tests/ -v
```