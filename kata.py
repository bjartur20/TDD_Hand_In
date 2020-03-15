def add(numbers):
    if not numbers:
        return 0

    number_list = numbers.split(',')
    sumation = sum(int(number) for number in number_list)

    return sumation


if __name__ == "__main__":
    print(add('1'))