def add(numbers):
    if not numbers:
        return 0

    number_list = numbers.replace('\n',',').split(',')
    sumation = sum(int(number) for number in number_list)

    return sumation