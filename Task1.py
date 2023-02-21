import sys


def read_input_to_list():
    random_list = []
    for i in range(0, 12):
        value = int(input())
        if value < 0 or value > 200:
            print("Invalid input. Value should be within 0 to 200")
            break
        random_list.append(value)
    return random_list


def find_index_identical_values(values: list):
    master_counter = 0
    master_index = -1

    counter = 0
    index = -1
    for i, item in enumerate(values):
        if i == 0:
            continue
        if values[i - 1] == item:
            if index == -1:
                index = i - 1
            counter += 1
        else:
            if master_counter < counter:
                master_counter = counter
                counter = 0
                master_index = index
                index = -1

    if counter > master_counter:
        master_index = index
    print("Start index of same numbers: " + str(master_index))


def sum_of_pair_elements(values: list):
    copy_list = values.copy()
    sum_of_pair_numbers = 0

    for i, val in enumerate(copy_list):
        for j, value in enumerate(copy_list[i + 1:], start=i + 1):
            if value == -1:
                continue
            if val == value:
                sum_of_pair_numbers += val * 2
                copy_list[i] = -1
                copy_list[j] = -1
    print("Sum of pair elements: " + str(sum_of_pair_numbers))


def multiply(values: list):
    result = 1
    lowest = sys.maxsize
    lowest_index = -1

    highest = -1
    highest_index = -1

    for i, item in enumerate(values):
        if lowest > item:
            lowest = item
            lowest_index = i
        if highest < item:
            highest = item
            highest_index = i

    start_index = lowest_index if lowest_index < highest_index else highest_index
    end_index = lowest_index if lowest_index > highest_index else highest_index
    for i, item in enumerate(values[start_index:end_index]):
        result *= item
    print("Multiply numbers between lowest and highest numbers: " + str(result))


if __name__ == '__main__':
    numbers = read_input_to_list()
    print(numbers)
    find_index_identical_values(numbers)
    sum_of_pair_elements(numbers)
    multiply(numbers)