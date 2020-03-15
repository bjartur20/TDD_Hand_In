def add(numbers):
    if not numbers:
        return 0

    number_list = numbers.replace('\n',',').split(',')
    return sum(int(number) for number in number_list if int(number) < 1001)