<?php

class Prime
{
    private static $num = 3;
    private static $primes = [2];
    private static $primesLength = 1;

    public static function first($firsts): array
    {
        $num = self::$num;
        $primesLength = self::$primesLength;

        while ($primesLength < $firsts) {
            if (self::isPrime($num) && !in_array($num, self::$primes)) {
                array_push(self::$primes, $num);
                $primesLength += 1;
            }
            $num += 2;
        }
        self::$primesLength = $primesLength;

        return array_slice(self::$primes, 0, $firsts);
    }

    private static function isPrime($num): bool
    {
        for ($divisor = 3; $divisor <= ceil(sqrt($num)); $divisor += 2) {
            if (!($num % $divisor)) {
                return false;
            }
        }

        return true;
    }
}
