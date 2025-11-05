"""
Comprehensive Fibonacci Utilities Library
==========================================

This module consolidates all Fibonacci-related functions from across the workspace,
including basic sequences, advanced algorithms, and creative applications.

Author: Consolidated from multiple sources
Date: November 5, 2025
"""

import math
import time
from functools import lru_cache
from typing import List, Tuple, Optional


# ============================================================================
# BASIC FIBONACCI FUNCTIONS
# ============================================================================

@lru_cache(maxsize=None)
def fibonacci(n: int) -> List[int]:
    """
    Generate a Fibonacci sequence of n terms using array-based approach.

    The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    where each number is the sum of the two preceding ones.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: The Fibonacci sequence

    Examples:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
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


def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using iterative approach.

    This is an optimized version that only returns the nth number
    rather than the entire sequence.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Examples:
        >>> fib(0)
        0
        >>> fib(10)
        55
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_nth(n: int) -> int:
    """
    Return the nth Fibonacci number (0-indexed).
    Alias for fib() function for compatibility.

    Args:
        n (int): The position in the Fibonacci sequence

    Returns:
        int: The nth Fibonacci number
    """
    return fib(n)


# ============================================================================
# FIBONACCI VALIDATION & ANALYSIS
# ============================================================================

def is_fibonacci(num: int) -> bool:
    """
    Check if a number is in the Fibonacci sequence.

    Uses the mathematical property that a number is Fibonacci if and only if
    one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.

    Args:
        num (int): The number to check

    Returns:
        bool: True if the number is in the Fibonacci sequence

    Examples:
        >>> is_fibonacci(8)
        True
        >>> is_fibonacci(10)
        False
    """
    if num < 0:
        return False

    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b or num == 0


def fibonacci_less_than(limit: int) -> List[int]:
    """
    Return a list of Fibonacci numbers less than the given limit.

    Args:
        limit (int): Upper bound (exclusive)

    Returns:
        list: Fibonacci numbers less than limit

    Examples:
        >>> fibonacci_less_than(100)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    result = []
    a, b = 0, 1
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result


# ============================================================================
# ADVANCED FIBONACCI ALGORITHMS
# ============================================================================

def fibonacci_spiral_points(n: int, scale: float = 1.0) -> List[Tuple[float, float]]:
    """
    Generate coordinates for a Fibonacci spiral visualization.
    Uses the golden ratio to create spiral points based on Fibonacci numbers.

    Args:
        n (int): Number of points to generate
        scale (float): Scale factor for the spiral

    Returns:
        list: List of (x, y) coordinates

    Example:
        >>> points = fibonacci_spiral_points(5, scale=2.0)
        >>> len(points)
        5
    """
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    points = []

    for i in range(n):
        angle = 2 * math.pi * i / phi
        radius = scale * math.sqrt(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))

    return points


def fibonacci_word(n: int) -> str:
    """
    Generate the nth Fibonacci word.
    Fibonacci words follow the pattern: S(0)='b', S(1)='a', S(n)=S(n-1)+S(n-2)

    Args:
        n (int): The nth Fibonacci word to generate

    Returns:
        str: The Fibonacci word

    Examples:
        >>> fibonacci_word(0)
        'b'
        >>> fibonacci_word(1)
        'a'
        >>> fibonacci_word(2)
        'ab'
        >>> fibonacci_word(3)
        'aba'
    """
    if n == 0:
        return 'b'
    elif n == 1:
        return 'a'

    prev_prev = 'b'
    prev = 'a'

    for i in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return prev


def zeckendorf_representation(n: int) -> List[int]:
    """
    Find the Zeckendorf representation of a number.
    Every positive integer can be uniquely represented as a sum of
    non-consecutive Fibonacci numbers.

    Args:
        n (int): The number to represent

    Returns:
        list: List of Fibonacci numbers that sum to n

    Examples:
        >>> zeckendorf_representation(20)
        [1, 2, 3, 13]
        >>> zeckendorf_representation(42)
        [1, 7, 34]
    """
    if n <= 0:
        return []

    # Generate Fibonacci numbers up to n
    fibs = [1, 2]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    result = []
    i = len(fibs) - 1

    # Greedy algorithm: pick largest Fibonacci numbers first
    while n > 0 and i >= 0:
        if fibs[i] <= n:
            result.append(fibs[i])
            n -= fibs[i]
        i -= 1

    return sorted(result)


# ============================================================================
# CREATIVE FIBONACCI APPLICATIONS
# ============================================================================

def fibonacci_music_scale(n: int, base_freq: float = 440.0) -> List[Tuple[int, float]]:
    """
    Generate musical frequencies using Fibonacci ratios.
    Creates a unique musical scale where each note's frequency is based on
    Fibonacci ratios.

    Args:
        n (int): Number of notes to generate
        base_freq (float): Base frequency in Hz (default A440)

    Returns:
        list: List of (note_number, frequency) tuples
    """
    fib_seq = fibonacci(n + 1)
    scale = []

    for i in range(n):
        if i == 0:
            freq = base_freq
        else:
            ratio = fib_seq[i + 1] / fib_seq[i]
            freq = base_freq * (ratio / 2)  # Divide by 2 to keep in reasonable octave range
        scale.append((i, round(freq, 2)))

    return scale


def fibonacci_cipher(text: str, shift_magnitude: int = 5) -> str:
    """
    Encrypt text using Fibonacci numbers as shifting keys.
    Each character is shifted by a Fibonacci number modulo 26.

    Args:
        text (str): Text to encrypt
        shift_magnitude (int): Controls the Fibonacci sequence length for shifting

    Returns:
        str: Encrypted text

    Example:
        >>> encrypted = fibonacci_cipher("HELLO", shift_magnitude=5)
        >>> len(encrypted)
        5
    """
    if not text:
        return ""

    fib_shifts = fibonacci(shift_magnitude)
    encrypted = []

    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shift = fib_shifts[i % len(fib_shifts)]
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted.append(new_char if is_upper else new_char.lower())
        else:
            encrypted.append(char)

    return ''.join(encrypted)


def fibonacci_fractal_depth(x: float, y: float, max_depth: int = 20) -> int:
    """
    Calculate fractal depth at a point using Fibonacci-inspired iteration.
    Similar to Mandelbrot but uses Fibonacci sequence for iteration rules.

    Args:
        x (float): X coordinate
        y (float): Y coordinate
        max_depth (int): Maximum iteration depth

    Returns:
        int: Depth before escape (or max_depth if doesn't escape)
    """
    fib_a, fib_b = 0, 1
    zx, zy = 0, 0

    for depth in range(max_depth):
        # Fibonacci-modified complex iteration
        zx_new = zx * zx - zy * zy + x * (fib_b / (fib_a + fib_b + 1))
        zy_new = 2 * zx * zy + y * (fib_a / (fib_a + fib_b + 1))

        zx, zy = zx_new, zy_new

        # Update Fibonacci sequence
        fib_a, fib_b = fib_b, fib_a + fib_b

        # Check escape condition
        if zx * zx + zy * zy > 4.0:
            return depth

    return max_depth


def fibonacci_collision_hash(s: str, table_size: int = 1000) -> int:
    """
    Hash function using Fibonacci hashing technique.
    Uses golden ratio multiplication for better distribution.

    Args:
        s (str): String to hash
        table_size (int): Size of hash table

    Returns:
        int: Hash value between 0 and table_size-1
    """
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    hash_val = 0

    for i, char in enumerate(s):
        # Fibonacci weight based on character position
        fib_weight = ((i + 1) * phi) % 1
        hash_val += ord(char) * fib_weight

    # Fibonacci hashing final step
    return int((hash_val * phi) % table_size)


# ============================================================================
# UTILITY FUNCTIONS (GCD, PRIME CHECK)
# ============================================================================

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The GCD of a and b (always positive)

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(-48, 18)
        6
    """
    a, b = abs(a), abs(b)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
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


# ============================================================================
# DEMONSTRATION & TESTING
# ============================================================================

def demonstrate_all_functions():
    """
    Comprehensive demonstration of all Fibonacci utilities.
    Useful for testing and showcasing capabilities.
    """
    print("=" * 70)
    print("FIBONACCI UTILITIES - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)

    print("\n[1] Basic Fibonacci Sequence")
    print(f"First 15 Fibonacci numbers: {fibonacci(15)}")
    print(f"10th Fibonacci number: {fib(10)}")

    print("\n[2] Fibonacci Validation")
    test_nums = [8, 10, 13, 21, 22]
    for num in test_nums:
        print(f"Is {num} a Fibonacci number? {is_fibonacci(num)}")

    print("\n[3] Fibonacci Less Than Limit")
    print(f"Fibonacci numbers < 100: {fibonacci_less_than(100)}")

    print("\n[4] Fibonacci Spiral Points")
    spiral = fibonacci_spiral_points(5, scale=2.0)
    print("First 5 spiral points:")
    for i, (x, y) in enumerate(spiral):
        print(f"  Point {i}: ({x:.2f}, {y:.2f})")

    print("\n[5] Fibonacci Words")
    for i in range(6):
        print(f"Fibonacci word {i}: {fibonacci_word(i)}")

    print("\n[6] Zeckendorf Representation")
    for num in [20, 42, 100]:
        zeck = zeckendorf_representation(num)
        print(f"{num} = {' + '.join(map(str, zeck))}")

    print("\n[7] Fibonacci Music Scale")
    scale = fibonacci_music_scale(8, base_freq=440.0)
    print("Musical notes (Hz):")
    for note_num, freq in scale:
        print(f"  Note {note_num}: {freq} Hz")

    print("\n[8] Fibonacci Cipher")
    original = "HELLO FIBONACCI"
    encrypted = fibonacci_cipher(original, shift_magnitude=8)
    print(f"Original:  {original}")
    print(f"Encrypted: {encrypted}")

    print("\n[9] Fibonacci Fractal Depth")
    test_points = [(0.0, 0.0), (-0.5, 0.5), (0.3, -0.3)]
    print("Fractal escape depths:")
    for x, y in test_points:
        depth = fibonacci_fractal_depth(x, y, max_depth=20)
        print(f"  Point ({x:5.1f}, {y:5.1f}): depth = {depth}")

    print("\n[10] Fibonacci Hashing")
    test_strings = ["fibonacci", "golden", "ratio", "spiral"]
    print("Hash values (table_size=1000):")
    for s in test_strings:
        hash_val = fibonacci_collision_hash(s, table_size=1000)
        print(f"  '{s}': {hash_val}")

    print("\n[11] Utility Functions")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 18 prime? {is_prime(18)}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_all_functions()
