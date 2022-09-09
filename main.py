from functools import wraps
from timeit import default_timer


def show_timing(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        amount = default_timer() - start_time
        print(
            'Выполнили функцию',
            func,
            'за {:.10f} сек.'.format(amount),
            'и получили',
            result,
        )
        return result

    return wrapper


@show_timing
def power_numbers(*numbers, power=3):
    list_num = []
    for num in numbers:
        list_num.append(num ** power)
    return list_num


power_numbers(1, 2, 3, 4, 5, 6, 7)


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


@show_timing
def filter_numbers(numbers, fil):
    if fil == EVEN:
        num_list = (list(filter(lambda i: i % 2 == 0, numbers)))
        return num_list
    if fil == ODD:
        num_list = (list(filter(lambda i: i % 2 != 0, numbers)))
        return num_list
    if fil == PRIME:
        num_list = []
        for num in numbers:
            k = 0
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    k = k + 1
            if k <= 0 and num != 1:
                num_list.append(num)
        return num_list


print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ODD))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], EVEN))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], PRIME))
