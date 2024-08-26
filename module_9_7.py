def is_prime(func):
    def wrapper(*args):
        mediator = func(*args)
        for i in range(2,mediator):
            if not (mediator % i):
                print('Составное')
                return mediator
        print('Простое')
        return mediator
    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total


result = sum_three(2, 3, 6)
print(result)
