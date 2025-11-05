import {expect, describe, it} from 'vitest';
import { mul } from '../code/fibonacci_utils';

describe('mul function', () => { // CURSOR POSITION
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

