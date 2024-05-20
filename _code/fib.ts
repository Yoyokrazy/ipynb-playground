export function sum(a, b) {
	return a + b;
}

import { something } from "./codeMyDude";
import { MultiDocumentHighlight } from "./codeMyDude";

export function sub(a, b) {
	return a - b;
}

const apple = 10

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

