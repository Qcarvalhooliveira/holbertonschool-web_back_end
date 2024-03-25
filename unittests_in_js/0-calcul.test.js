const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Test the calculateNumber sum', function() {
    it('should return the sum of rounded a and b', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should correctly round a and b upwards', function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
});
