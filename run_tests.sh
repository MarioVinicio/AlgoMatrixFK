#!/bin/bash

python3 -m pytest -r tests/test_sort_algorithms.py

# To save pytest test session details to file
# pytest -r a shaman/tests/test_sort_algorithms.py | tee logs/test_session.log 