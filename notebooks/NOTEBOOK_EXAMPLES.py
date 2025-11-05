# Example Notebook Cells for Using fibonacci_utils.py
# =====================================================
# Copy these cells into your Jupyter notebooks to use the consolidated module

# Cell 1: Import the consolidated module
# ---------------------------------------
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'code'))
from fibonacci_utils import *

# Cell 2: Basic Fibonacci examples
# ---------------------------------
# Generate first 20 Fibonacci numbers
fib_sequence = fibonacci(20)
print("First 20 Fibonacci numbers:")
print(fib_sequence)

# Get specific Fibonacci number
print(f"\n50th Fibonacci number: {fib(50)}")

# Cell 3: Check if numbers are Fibonacci
# ---------------------------------------
test_numbers = [1, 8, 10, 13, 21, 100, 144]
print("Fibonacci validation:")
for num in test_numbers:
    result = "✓" if is_fibonacci(num) else "✗"
    print(f"  {result} {num}")

# Cell 4: Zeckendorf representation
# ----------------------------------
numbers_to_decompose = [20, 42, 100, 255]
print("Zeckendorf Representation (sum of non-consecutive Fibonacci numbers):")
for num in numbers_to_decompose:
    zeck = zeckendorf_representation(num)
    print(f"  {num} = {' + '.join(map(str, zeck))}")

# Cell 5: Fibonacci spiral visualization
# ---------------------------------------
import matplotlib.pyplot as plt

# Generate spiral points
points = fibonacci_spiral_points(100, scale=0.5)
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Plot the spiral
plt.figure(figsize=(10, 10))
plt.scatter(x_coords, y_coords, c=range(len(points)), cmap='viridis', s=50, alpha=0.6)
plt.colorbar(label='Point Index')
plt.title('Fibonacci Spiral (100 points)')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.show()

# Cell 6: Fibonacci music scale
# ------------------------------
scale = fibonacci_music_scale(12, base_freq=440.0)
print("Fibonacci Musical Scale (based on A440):")
print("Note | Frequency (Hz)")
print("-----|---------------")
for note_num, freq in scale:
    print(f"  {note_num:2d}  | {freq:8.2f}")

# Cell 7: Prime numbers and GCD
# ------------------------------
# Find prime Fibonacci numbers
fib_seq = fibonacci(20)
prime_fibs = [n for n in fib_seq if is_prime(n)]
print(f"Prime Fibonacci numbers in first 20: {prime_fibs}")

# GCD examples
print(f"\nGCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 50) = {gcd(100, 50)}")

# Cell 8: Cipher encryption demo
# -------------------------------
message = "HELLO FIBONACCI WORLD"
encrypted = fibonacci_cipher(message, shift_magnitude=10)
print(f"Original message:  {message}")
print(f"Encrypted message: {encrypted}")

# Cell 9: Comprehensive demo
# ---------------------------
# Run the built-in demonstration
demonstrate_all_functions()
