/**
 * Comprehensive Fibonacci Utilities Library (TypeScript)
 * =======================================================
 *
 * This module consolidates all Fibonacci-related functions from across the workspace,
 * providing basic sequences, mathematical utilities, and prime checking.
 *
 * @author Consolidated from multiple sources
 * @date November 5, 2025
 */


// ============================================================================
// BASIC ARITHMETIC OPERATIONS
// ============================================================================

/**
 * Add two numbers together.
 * @param a - First number
 * @param b - Second number
 * @returns Sum of a and b
 */
export function sum(a: number, b: number): number {
	return a + b;
}

/**
 * Subtract b from a.
 * @param a - Number to subtract from
 * @param b - Number to subtract
 * @returns Difference of a and b
 */
export function sub(a: number, b: number): number {
	return a - b;
}

/**
 * Multiply two numbers using repeated addition.
 * @param a - First number
 * @param b - Second number (multiplier)
 * @returns Product of a and b
 */
export function mul(a: number, b: number): number {
	let result = 0;
	const absB = Math.abs(b);
	for (let i = 0; i < absB; i++) {
		result = sum(result, a);
	}
	return b < 0 ? -result : result;
}


// ============================================================================
// FIBONACCI FUNCTIONS
// ============================================================================

/**
 * Calculate the nth Fibonacci number using iterative approach.
 *
 * The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
 * where each number is the sum of the two preceding ones.
 *
 * @param n - The position in the Fibonacci sequence (0-indexed)
 * @returns The nth Fibonacci number
 *
 * @example
 * ```typescript
 * fib(0)  // returns 0
 * fib(1)  // returns 1
 * fib(10) // returns 55
 * ```
 */
export function fib(n: number): number {
	if (n <= 1) return n;

	let a = 0;
	let b = 1;
	let temp: number;

	for (let i = 2; i <= n; i++) {
		temp = b;
		b = sum(a, b);
		a = temp;
	}

	return b;
}

/**
 * Generate a Fibonacci sequence up to n terms.
 * @param n - Number of terms to generate
 * @returns Array of Fibonacci numbers
 *
 * @example
 * ```typescript
 * fibonacciSequence(5)  // returns [0, 1, 1, 2, 3]
 * fibonacciSequence(10) // returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
 * ```
 */
export function fibonacciSequence(n: number): number[] {
	if (n <= 0) return [];
	if (n === 1) return [0];

	const sequence: number[] = [0, 1];

	for (let i = 2; i < n; i++) {
		sequence.push(sequence[i - 1] + sequence[i - 2]);
	}

	return sequence;
}

/**
 * Check if a number is in the Fibonacci sequence.
 * @param num - The number to check
 * @returns True if the number is a Fibonacci number
 *
 * @example
 * ```typescript
 * isFibonacci(8)  // returns true
 * isFibonacci(10) // returns false
 * ```
 */
export function isFibonacci(num: number): boolean {
	if (num < 0) return false;
	if (num === 0 || num === 1) return true;

	let a = 0;
	let b = 1;

	while (b < num) {
		const temp = b;
		b = a + b;
		a = temp;
	}

	return b === num;
}

/**
 * Get all Fibonacci numbers less than a given limit.
 * @param limit - Upper bound (exclusive)
 * @returns Array of Fibonacci numbers less than limit
 *
 * @example
 * ```typescript
 * fibonacciLessThan(100) // returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 * ```
 */
export function fibonacciLessThan(limit: number): number[] {
	const result: number[] = [];
	let a = 0;
	let b = 1;

	while (a < limit) {
		result.push(a);
		const temp = b;
		b = a + b;
		a = temp;
	}

	return result;
}


// ============================================================================
// MATHEMATICAL UTILITIES
// ============================================================================

/**
 * Check if a number is prime.
 * @param n - The number to check
 * @returns True if the number is prime, false otherwise
 *
 * @example
 * ```typescript
 * isPrime(7)  // returns true
 * isPrime(8)  // returns false
 * isPrime(17) // returns true
 * ```
 */
export function isPrime(n: number): boolean {
	if (n <= 1) return false;
	if (n <= 3) return true;
	if (n % 2 === 0 || n % 3 === 0) return false;

	for (let i = 5; i * i <= n; i += 6) {
		if (n % i === 0 || n % (i + 2) === 0) {
			return false;
		}
	}

	return true;
}

/**
 * Calculate the Greatest Common Divisor (GCD) using Euclidean algorithm.
 * @param a - First number
 * @param b - Second number
 * @returns The GCD of a and b (always positive)
 *
 * @example
 * ```typescript
 * gcd(48, 18)  // returns 6
 * gcd(-48, 18) // returns 6
 * gcd(17, 19)  // returns 1
 * ```
 */
export function gcd(a: number, b: number): number {
	a = Math.abs(a);
	b = Math.abs(b);

	while (b !== 0) {
		const temp = b;
		b = a % b;
		a = temp;
	}

	return a;
}

/**
 * Calculate the Least Common Multiple (LCM).
 * @param a - First number
 * @param b - Second number
 * @returns The LCM of a and b
 *
 * @example
 * ```typescript
 * lcm(4, 6)  // returns 12
 * lcm(21, 6) // returns 42
 * ```
 */
export function lcm(a: number, b: number): number {
	if (a === 0 || b === 0) return 0;
	return Math.abs(a * b) / gcd(a, b);
}


// ============================================================================
// GOLDEN RATIO AND FIBONACCI RELATIONSHIPS
// ============================================================================

/**
 * The golden ratio (phi): (1 + sqrt(5)) / 2 ≈ 1.618033988749895
 */
export const PHI = (1 + Math.sqrt(5)) / 2;

/**
 * Calculate the nth Fibonacci number using Binet's formula (closed form).
 * Note: This method may have floating-point precision issues for large n.
 *
 * @param n - The position in the Fibonacci sequence
 * @returns Approximate nth Fibonacci number
 */
export function fibBinet(n: number): number {
	const psi = (1 - Math.sqrt(5)) / 2;
	return Math.round((Math.pow(PHI, n) - Math.pow(psi, n)) / Math.sqrt(5));
}

/**
 * Calculate the ratio of consecutive Fibonacci numbers (approaches golden ratio).
 * @param n - Position to calculate ratio at
 * @returns Ratio of F(n) / F(n-1)
 */
export function fibonacciRatio(n: number): number {
	if (n <= 1) return 0;
	return fib(n) / fib(n - 1);
}


// ============================================================================
// DEMONSTRATION FUNCTIONS
// ============================================================================

/**
 * Demonstrate all Fibonacci utilities with examples.
 * Useful for testing and showcasing capabilities.
 */
export function demonstrateAll(): void {
	console.log('='.repeat(70));
	console.log('FIBONACCI UTILITIES - COMPREHENSIVE DEMONSTRATION (TypeScript)');
	console.log('='.repeat(70));

	console.log('\n[1] Basic Arithmetic');
	console.log(`sum(5, 3) = ${sum(5, 3)}`);
	console.log(`sub(10, 4) = ${sub(10, 4)}`);
	console.log(`mul(6, 7) = ${mul(6, 7)}`);

	console.log('\n[2] Fibonacci Sequence');
	console.log(`First 15 Fibonacci numbers: ${fibonacciSequence(15).join(', ')}`);
	console.log(`10th Fibonacci number: ${fib(10)}`);
	console.log(`20th Fibonacci number: ${fib(20)}`);

	console.log('\n[3] Fibonacci Validation');
	const testNums = [8, 10, 13, 21, 22];
	testNums.forEach(num => {
		console.log(`Is ${num} a Fibonacci number? ${isFibonacci(num)}`);
	});

	console.log('\n[4] Fibonacci Less Than Limit');
	console.log(`Fibonacci numbers < 100: ${fibonacciLessThan(100).join(', ')}`);

	console.log('\n[5] Prime Number Checking');
	const primeTests = [2, 3, 4, 17, 20, 29];
	primeTests.forEach(num => {
		console.log(`Is ${num} prime? ${isPrime(num)}`);
	});

	console.log('\n[6] GCD and LCM');
	console.log(`gcd(48, 18) = ${gcd(48, 18)}`);
	console.log(`lcm(4, 6) = ${lcm(4, 6)}`);
	console.log(`gcd(17, 19) = ${gcd(17, 19)}`);

	console.log('\n[7] Golden Ratio');
	console.log(`Golden Ratio (φ) = ${PHI}`);
	console.log(`fib(10) using Binet's formula = ${fibBinet(10)}`);
	console.log(`Ratio F(20)/F(19) = ${fibonacciRatio(20)} (approaching φ)`);

	console.log('\n' + '='.repeat(70));
}


// ============================================================================
// EXPORTS FOR BACKWARD COMPATIBILITY
// ============================================================================

// Default export for module usage
export default {
	// Basic operations
	sum,
	sub,
	mul,

	// Fibonacci functions
	fib,
	fibonacciSequence,
	isFibonacci,
	fibonacciLessThan,
	fibBinet,
	fibonacciRatio,

	// Math utilities
	isPrime,
	gcd,
	lcm,

	// Constants
	PHI,

	// Demo
	demonstrateAll,
};
