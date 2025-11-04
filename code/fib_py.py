import time
from functools import lru_cache

# gh test

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Generate a Fibonacci sequence of n terms.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: The Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize array for Fibonacci sequence
    fib_array = [0] * n
    fib_array[0] = 0
    fib_array[1] = 1

    # Calculate Fibonacci numbers using array
    for i in range(2, n):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]

    return fib_array

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The GCD of a and b (always positive)
    """
    a, b = abs(a), abs(b)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def main():
    # Fibonacci example
    n = 20
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f"Fibonacci sequence up to {n} terms: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # Prime check example
    number = 29
    start_time = time.time()
    result = is_prime(number)
    end_time = time.time()
    print(f"Is {number} a prime number? {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # GCD example
    a, b = 48, 18
    start_time = time.time()
    result = gcd(a, b)
    end_time = time.time()
    print(f"GCD of {a} and {b}: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
