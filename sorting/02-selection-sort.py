def selection_sort(input_numbers):
    """
        Worst Case: O(n*n)
        Average Case: O(n*logn)
        Best case: O(n*logn)

        Auxiliary Space Complexity: O(1)
    """

    for i in range(len(input_numbers)):

        min_value_position = i
        for j in range(i + 1, len(input_numbers)):
            if input_numbers[min_value_position] > input_numbers[j]:
                min_value_position = j

        input_numbers.insert(i, input_numbers.pop(min_value_position))

    return input_numbers


def main():
    input_numbers = list(map(int, input("Enter coma separated numbers:").split(',')))

    selection_sort_result = selection_sort(input_numbers)
    print("Selection sort:", ','.join([str(item) for item in selection_sort_result]))


if __name__ == '__main__':
    main()
