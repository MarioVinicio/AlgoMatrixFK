from random import randint


class SortAlgorithms:
    def radix_sort_lsd(self, arr: list[int]) -> list[int]:
        """
        Least Significant Digit (LSD) Radix Sort algorithm.
        Radix Sort is a non-comparative sorting algorithm that sorts integers by processing digits
        starting from the least significant digit (rightmost digit) to the most significant digit (leftmost digit).

        Sorts the input list in ascending order using the Radix Sort LSD algorithm.

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

    def radix_sort_msd(self, arr: list[int]) -> list[int]:
        """
        Most Significant Digit (MSD) Radix Sort algorithm.
        Similar to the Least Significant Digit (LSD) Radix Sort, MSD Radix Sort is a non-comparative
        sorting algorithm that sorts integers by processing digits, but it starts from the most
        significant digit (leftmost digit) and moves towards the least significant digit (rightmost digit).

        Sorts the input list in ascending order using the Radix Sort MSD algorithm.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - arr (list): The sorted list.
        """

        def _radix_sort_msd(arr, digit_count):
            if digit_count == 0:
                return

            buckets = [[] for _ in range(10)]  # Create 10 buckets for digits 0-9

            # Distribute elements into buckets based on current digit
            for num in arr:
                digit = get_digit(num, digit_count)
                buckets[digit].append(num)

            # Recursively sort each bucket
            for i in range(10):
                _radix_sort_msd(buckets[i], digit_count - 1)

            # Concatenate buckets to form the sorted array
            arr.clear()
            for bucket in buckets:
                arr.extend(bucket)

        def get_digit(num, digit_count):
            # Get the digit at the specified position from the right
            return (num // 10 ** (digit_count - 1)) % 10

        # Get the maximum number of digits in the array
        max_digits = max(arr)
        max_digit_count = len(str(max_digits))

        # Call the helper function to perform MSD Radix Sort
        _radix_sort_msd(arr, max_digit_count)
        return arr

    def bubble_sort(self, arr: list[int]) -> list[int]:
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

    def quick_sort1(self, arr: list[int]) -> list[int]:
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

    def quick_sort2(self, arr: list[int]) -> list[int]:
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
