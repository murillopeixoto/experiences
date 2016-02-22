import pytest
from prime import Primes


class TestPrime(object):
    def test_primes_firsts(self):
        assert Primes.first(1) == [2]
        assert Primes.first(2) == [2, 3]
        assert Primes.first(5) == [2, 3, 5, 7, 11]
        assert Primes.first(20)[-5:] == [53, 59, 61, 67, 71]
        assert Primes.first(100)[99] == 541
        assert Primes.first(20004)[79] == 409
