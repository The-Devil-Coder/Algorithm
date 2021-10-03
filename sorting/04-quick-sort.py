def partition(input_numbers, left, right):
    pivot = input_numbers[right]
    i = left - 1
    for j in range(left, right + 1):
        if input_numbers[j] < pivot:
            i += 1
            input_numbers[i], input_numbers[j] = input_numbers[j], input_numbers[i]

    input_numbers[i + 1], input_numbers[right] = input_numbers[right], input_numbers[i + 1]
    return i + 1


def quick_sort(input_numbers, left, right):
    """
        Worst Case: O(n*n)
        Average Case: O(n*logn)
        Best case: O(n*logn)

        Auxiliary Space Complexity: O(1)
    """

    if left < right:
        mid = partition(input_numbers, left, right)
        quick_sort(input_numbers, left, mid - 1)
        quick_sort(input_numbers, mid + 1, right)
    return input_numbers


def main():
    input_numbers = list(map(int, input("Enter coma separated numbers:").split(',')))

    quick_sort_result = quick_sort(input_numbers, 0, len(input_numbers) - 1)
    print("Quick sort:", ','.join([str(item) for item in quick_sort_result]))


if __name__ == '__main__':
    main()
