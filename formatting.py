
def add_numbers(first, second):
    add_sum = first + second
    return add_sum


num_sum = add_numbers(1, 2)
print("adding numbers sum: %d" % num_sum)


def fibonacci(length):
    perv_value = 1
    current_value = 1
    while current_value < length:
        current_value += perv_value
        perv_value = current_value
    return current_value


fibonacci_value = fibonacci(5)
print("Fibonacci value: %d" % fibonacci_value)
