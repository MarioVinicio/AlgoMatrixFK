from random import randint
from typing import List


class SortAlgorithms:
    def radix_sort(self, arr: List[int]) -> List[int]:
        """
        Radix sort is a non-comparative sorting algorithm that works by distributing elements into buckets
        according to their individual digits. The algorithm processes the digits from the least significant
        to the most significant or vice versa. Radix sort can be applied to integers, strings, or other
        data types where a meaningful ordering can be defined for the individual digits.

        Sorts the input list in ascending order using the Radix Sort algorithm.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - arr (list): The sorted list.
        """

        def counting_sort(arr, exp):
            """
            counting sort as a subroutine for sorting elements at each digit place.
            """
            n = len(arr)
            output = [0] * n
            count = [0] * 10  # 0 to 9 for decimal digits

            # Count occurrences of digits at the current place value
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            # Update count to store actual positions of digits
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array using count and original array
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            # Copy the sorted elements back to the original array
            for i in range(n):
                arr[i] = output[i]

        # Find the maximum number to determine the number of digits
        max_num = max(arr)
        exp = 1  # Initialize the place value to 1 (least significant digit)

        while max_num // exp > 0:
            counting_sort(arr, exp)
            exp *= 10  # Move to the next digit place

        return arr

    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
        compares adjacent elements, and swaps them if they are in the wrong order.
        The pass through the list is repeated until the list is sorted.

        Sorts the input list in ascending order using the Bubble Sort algorithm.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - arr (list): The sorted list.
        """
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr

    def quick_sort1(self, arr: List[int]) -> List[int]:
        """
        QuickSort is a highly efficient sorting algorithm that uses a divide-and-conquer strategy to sort elements in a list.
        The basic idea is to choose a "pivot" element from the array and partition the other elements into two sub-arrays
        according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

        Sorts the input list in ascending order using the QuickSort1 algorithm.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - arr list: The sorted list.
        """
        if len(arr) <= 1:
            return arr

        smaller, equal, larger = [], [], []
        pivot = arr[randint(0, len(arr) - 1)]

        for x in arr:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                larger.append(x)

        return self.quick_sort1(smaller) + equal + self.quick_sort1(larger)

    def quick_sort2(self, arr: List[int]) -> List[int]:
        """
        Sorts the input list in ascending order using the QuickSort2 algorithm.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - arr list: The sorted list.
        """

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_sort2(left) + middle + self.quick_sort2(right)
