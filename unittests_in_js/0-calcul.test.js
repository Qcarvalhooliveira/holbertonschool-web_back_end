const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Test the calculateNumber sum', function() {
    it('should return the sum of rounded a and b', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
        assert.strictEqual(calculateNumber(2.5, 0.7), 4);
        assert.strictEqual(calculateNumber(0, 6.7), 7);
        assert.strictEqual(calculateNumber(6.8, 1), 8);
    });
});
