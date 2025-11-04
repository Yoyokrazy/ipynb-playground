import time
from functools import lru_cache
import math

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

def fibonacci_spiral_points(n, scale=1.0):
    """
    Generate coordinates for a Fibonacci spiral visualization.
    Uses the golden ratio to create spiral points based on Fibonacci numbers.

    Args:
        n (int): Number of points to generate
        scale (float): Scale factor for the spiral

    Returns:
        list: List of (x, y) coordinates
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

def fibonacci_word(n):
    """
    Generate the nth Fibonacci word.
    Fibonacci words follow the pattern: S(0)='b', S(1)='a', S(n)=S(n-1)+S(n-2)

    Args:
        n (int): The nth Fibonacci word to generate

    Returns:
        str: The Fibonacci word
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

def zeckendorf_representation(n):
    """
    Find the Zeckendorf representation of a number.
    Every positive integer can be uniquely represented as a sum of non-consecutive Fibonacci numbers.

    Args:
        n (int): The number to represent

    Returns:
        list: List of Fibonacci numbers that sum to n
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

def fibonacci_music_scale(n, base_freq=440.0):
    """
    Generate musical frequencies using Fibonacci ratios.
    Creates a unique musical scale where each note's frequency is based on Fibonacci ratios.

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

def fibonacci_cipher(text, shift_magnitude=5):
    """
    Encrypt text using Fibonacci numbers as shifting keys.
    Each character is shifted by a Fibonacci number modulo 26.

    Args:
        text (str): Text to encrypt
        shift_magnitude (int): Controls the Fibonacci sequence length for shifting

    Returns:
        str: Encrypted text
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

def fibonacci_fractal_depth(x, y, max_depth=20):
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

def fibonacci_collision_hash(s, table_size=1000):
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

def main():
    print("=== Classic Fibonacci Sequence ===")
    n = 20
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f"Fibonacci sequence up to {n} terms: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    print("=== Fibonacci Music Scale ===")
    music_scale = fibonacci_music_scale(8, base_freq=440.0)
    print("Fibonacci-based musical scale (Hz):")
    for note_num, freq in music_scale:
        print(f"  Note {note_num}: {freq} Hz")
    print()

    print("=== Fibonacci Cipher ===")
    original_text = "Hello Fibonacci World"
    encrypted = fibonacci_cipher(original_text, shift_magnitude=8)
    print(f"Original:  {original_text}")
    print(f"Encrypted: {encrypted}")
    print()

    print("=== Fibonacci Fractal Depth ===")
    test_points = [(0.0, 0.0), (-0.5, 0.5), (0.3, -0.3), (-1.0, 0.0)]
    print("Fibonacci fractal escape depths:")
    for x, y in test_points:
        depth = fibonacci_fractal_depth(x, y, max_depth=20)
        print(f"  Point ({x:5.1f}, {y:5.1f}): depth = {depth}")
    print()

    print("=== Fibonacci Hashing ===")
    test_strings = ["fibonacci", "golden", "ratio", "spiral", "fibonacci"]
    print("Fibonacci hash values (table_size=1000):")
    for s in test_strings:
        hash_val = fibonacci_collision_hash(s, table_size=1000)
        print(f"  '{s}': {hash_val}")
    print()

    print("=== Fibonacci Spiral Points ===")
    spiral_points = fibonacci_spiral_points(10, scale=2.0)
    print(f"First 10 spiral coordinates (based on golden ratio):")
    for i, (x, y) in enumerate(spiral_points):
        print(f"  Point {i}: ({x:.2f}, {y:.2f})")
    print()

    print("=== Zeckendorf Representation ===")
    test_numbers = [20, 42, 100]
    for num in test_numbers:
        zeck = zeckendorf_representation(num)
        print(f"  {num} = {' + '.join(map(str, zeck))}")

if __name__ == "__main__":
    main()
