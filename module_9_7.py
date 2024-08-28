def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        is_prime = True
        for i in range(2, res):
            if res % i == 0:
                is_prime = False
        if is_prime == True:
            return (f'Простое \n{res}')
        else:
            return (f'Составное \n{res}')
    return wrapper
@ is_prime
def sum_three(*value):
    res = sum(value)
    return res


result = sum_three(2, 3, 6)
print(result)