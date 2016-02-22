class Primes(object):
    num = 3
    primes = [2]
    primes_size = 1

    @classmethod
    def first(self, firsts):
        num = self.num
        primes_size = self.primes_size

        while primes_size < firsts:
            if self._is_prime(num):
                self.primes.append(num)
                primes_size += 1
            num += 2

        self.num = num
        self.primes_size = primes_size

        return Primes.primes[0:firsts]

    @classmethod
    def _is_prime(self, num):
        for divisor in xrange(3, int(num ** 0.5) + 1, 2):
            if not num % divisor:
                return False
        return True
