def is_prime(numbers):
    for num in numbers:
        for n in range(2, num):
            if num % n == 0:
                return False
    return True