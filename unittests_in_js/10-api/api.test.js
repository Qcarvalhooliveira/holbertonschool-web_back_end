const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('should return correct status code and result', (done) => {
    request('http://localhost:7865', (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.equal('Welcome to the payment system');
      done();
    });
  });
});

  describe('Cart page', () => {
    it('returns correct status code when id is a number', (done) => {
      request('http://localhost:7865/cart/123', (err, res, text) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(200);
        expect(text).to.include('Payment methods for cart 123');
        done();
      });
    });
  
    it('returns 404 status code when id is NOT a number', (done) => {
      request('http://localhost:7865/cart/not-a-number', (err, res, text) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
});

describe('/available_payments endpoint', () => {
  it('returns available payment methods', (done) => {
    request('http://localhost:7865/available_payments', { json: true }, (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('/login endpoint', () => {
  it('welcomes the user by username', (done) => {
    request.post(
      {
      url: 'http://localhost:7865/login',
      form: {
        userName: 'Betty',
      },
    },

    (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.equal('Welcome Betty');
      done();
    });
  });
});

