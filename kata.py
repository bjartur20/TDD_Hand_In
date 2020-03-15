class NegativeError(Exception):
    pass

def add(numbers):
    if not numbers:
        return 0

    if numbers[:2] == '//':
        delimeter = numbers[2]
        number_list = numbers[4:].split(delimeter)
    else:
        number_list = numbers.replace('\n',',').split(',')

    neg_num_list = [num for num in number_list if int(num) < 0]

    if neg_num_list:
        raise NegativeError('Negatives not allowed: ' + ','.join(neg_num_list))

    return sum(int(number) for number in number_list if int(number) < 1001)