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
	if (n <= 1) return n;
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

const a = 5;
const b = 3;

a

const multiplication = mul(a, b);
const addition = sum(a, b);
const subtraction = sub(a, b);
const fibonacci = fib(10);
const primeCheck = isPrime(7);
const primeCheck = isPrime(7);
const primeCheck = isPrime(7);

console.log("Multiplication:", multiplication);
console.log("Addition:", addition);
console.log("Subtraction:", subtraction);
console.log("Fibonacci:", fibonacci);
console.log("Prime Check:", primeCheck);

class Test {
	constructor() {
		console.log('Test constructor2');
	}
}
