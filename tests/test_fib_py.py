"""
Unit tests for consolidated fibonacci_utils.py functions
"""
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from fibonacci_utils import fibonacci, is_prime, gcd


def test_fibonacci():
    """Test fibonacci function"""
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("✓ All fibonacci tests passed")


def test_is_prime():
    """Test is_prime function"""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    print("✓ All is_prime tests passed")


def test_gcd():
    """Test gcd function"""
    assert gcd(48, 18) == 6
    assert gcd(17, 19) == 1
    assert gcd(5, 0) == 5
    assert gcd(0, 7) == 7
    assert gcd(60, 48) == 12
    assert gcd(100, 50) == 50
    # Test with negative numbers
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6
    print("✓ All gcd tests passed")


if __name__ == "__main__":
    test_fibonacci()
    test_is_prime()
    test_gcd()
    print("\n✅ All tests passed successfully!")
