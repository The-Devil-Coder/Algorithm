def bubble_sort(input_numbers):
    """
    Worst Case: O(n^2)
    Average Case: O(n*logn)
    Best case: O(n*logn)

    Auxiliary Space Complexity: O(1)
    """

    for i in range(len(input_numbers)):
        for j in range(i + 1, len(input_numbers)):
            if input_numbers[i] > input_numbers[j]:
                temp = input_numbers[j]
                input_numbers[j] = input_numbers[i]
                input_numbers[i] = temp

    return input_numbers


def main():
    input_numbers = list(map(int, input("Enter coma separated numbers:").split(',')))

    bubble_sort_result = bubble_sort(input_numbers)
    print("Bubble sort:", ','.join([str(item) for item in bubble_sort_result]))


if __name__ == '__main__':
    main()
