"""

Implementation of the Merge Sort algorithm.

Merge Sort is a recursive divide-and-conquer algorithm:

1. Split the list into two halves.

2. Recursively sort both halves.

3. Merge the sorted halves back together.

The sorting is performed in-place on the given list.

"""
import matplotlib.pyplot as plt


def assign(target_list, target_index, source_list, source_index):
    """

    Copies an element from a source list into a target list.

    """
    target_list[target_index] = source_list[source_index]


def merge_sort(values):
    """

    Sorts a list using the Merge Sort algorithm.

    Args:

        values: The list to be sorted.

    """
    if (len(values) < 1):
        return 

    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):

        if left_half[left_index] <= right_half[right_index]:
            assign(values, merged_index, left_half, left_index)
            left_index += 1

        else:
            assign(values, merged_index, right_half, right_index)
            right_index += 1
        merged_index += 1

    while left_index < len(left_half):
        assign(values, merged_index, left_half, left_index)
        left_index += 1
        merged_index += 1

    while right_index < len(right_half):
        assign(values, merged_index, right_half, right_index)
        right_index += 1
        merged_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

merge_sort(my_list)

x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
