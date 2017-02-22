<?php

use PHPUnit\Framework\TestCase;

include 'prime.php';
class PrimeTest extends TestCase
{
    /**
     * @dataProvider addDataProvider
     */
    public function testFirstPrimesShouldReturnsNFirstsPrimeNumbersWithNAsANumber($n, $expects)
    {
        $firstsNPrimes = Prime::first($n);
        $this->assertEquals($firstsNPrimes, $expects);
        $this->assertEquals($n, count($firstsNPrimes));
    }

    public function addDataProvider()
    {
        return [
            [1, [2]],
            [2, [2, 3]],
            [5, [2, 3, 5, 7, 11]],
            [20, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]]
        ];
    }
}
