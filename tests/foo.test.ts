import {expect, describe, it} from 'vitest';
import { mul, gcd } from '../code/fib';

describe('mul f<<CURSOR>>unction', () => { // CURSOR POSITION
	it('should return 6 for mul(2, 3)', () => {
		const result = mul(2, 3);
		expect(result).to.equal(6);
	});

	it('should return 0 for mul(0, 5)', () => {
		const result = mul(0, 5);
		expect(result).to.equal(0);
	});

	it('should return -15 for mul(-3, 5)', () => {
		const result = mul(-3, 5);
		expect(result).to.equal(-15);
	});

	it('should return 25 for mul(5, 5)', () => {
		const result = mul(5, 5);
		expect(result).to.equal(25);
	});

	it('should return 0 for mul(0, 0)', () => {
		const result = mul(0, 0);
		expect(result).to.equal(0);
	});

});

describe('gcd function', () => {
	it('should return 6 for gcd(48, 18)', () => {
		const result = gcd(48, 18);
		expect(result).to.equal(6);
	});

	it('should return 1 for gcd(17, 19)', () => {
		const result = gcd(17, 19);
		expect(result).to.equal(1);
	});

	it('should return 5 for gcd(5, 0)', () => {
		const result = gcd(5, 0);
		expect(result).to.equal(5);
	});

	it('should return 7 for gcd(0, 7)', () => {
		const result = gcd(0, 7);
		expect(result).to.equal(7);
	});

	it('should return 12 for gcd(60, 48)', () => {
		const result = gcd(60, 48);
		expect(result).to.equal(12);
	});
});
