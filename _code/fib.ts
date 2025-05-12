// woohoo
// filepath: c:\Users\milively\Documents\_dev_work\playground-0\_code\fib.ts
export function sum(a, b) {
	return a + b;
}

export function sub(a, b) {
	return a - b;
}

export function mul(a, b) {
	let result = 0;
	for (let i = 0; i < b; i++) {
		result = sum(result, a);
	}
	return result;
}

export function fib(n) {
	let a = 0, b = 1, temp;
	for (let i = 2; i <= n; i++) {
		temp = b;
		b = sum(a, b)
		a = temp;
	}
	return b;
}

export function isPrime(n) {
	if (n <= 1) return false;
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (n % i === 0) return false;
	}
	return true;
}

// Example usage
const result = fib(10);
console.log("Fibonacci(10):", result);


