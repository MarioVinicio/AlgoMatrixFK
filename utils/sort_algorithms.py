from typing import List


class SortAlgorithms:
    def radix_sort(self, arr: List[int]) -> List[int]:
        """
        Radix sort is a non-comparative sorting algorithm that works by distributing elements into buckets
        according to their individual digits. The algorithm processes the digits from the least significant
        to the most significant or vice versa. Radix sort can be applied to integers, strings, or other
        data types where a meaningful ordering can be defined for the individual digits.
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
