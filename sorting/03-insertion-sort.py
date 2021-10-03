def insertion_sort(input_numbers):
    """
        Worst Case: O(n*n)
        Average Case: O(n*logn)
        Best case: O(n*logn)

        Auxiliary Space Complexity: O(1)
    """

    for i in range(1, len(input_numbers)):
        key = input_numbers[i]
        j = i
        while j > 0 and key < input_numbers[j - 1]:
            input_numbers[j] = input_numbers[j - 1]
            j -= 1

        input_numbers[j] = key

    return input_numbers


def main():
    input_numbers = list(map(int, input("Enter coma separated numbers:").split(',')))

    insertion_sort_result = insertion_sort(input_numbers)
    print("Insertion sort:", ','.join([str(item) for item in insertion_sort_result]))


if __name__ == '__main__':
    main()
