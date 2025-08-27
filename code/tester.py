# memoize this code
def fibonacci_sequence(n):
    """Generate the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def fibonacci_nth(n):
    """Return the nth Fibonacci number (0-indexed)."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_fibonacci(num):
    """Check if a number is in the Fibonacci sequence."""
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b or num == 0


def fibonacci_less_than(limit):
    """Return a list of Fibonacci numbers less than the given limit."""
    result = []
    a, b = 0, 1
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    fib_100 = fibonacci_sequence(100)
    for idx, num in enumerate(fib_100, 1):
        print(f"{idx}: {num}")
    print("\nThe 50th Fibonacci number is:", fibonacci_nth(50))
    print("Is 144 a Fibonacci number?", is_fibonacci(144))
    print("Is 145 a Fibonacci number?", is_fibonacci(145))
    print("Fibonacci numbers less than 1000:")
    print(fibonacci_less_than(1000))
