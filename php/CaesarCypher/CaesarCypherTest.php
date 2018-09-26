<?php

use PHPUnit\Framework\TestCase;

include 'caesar_cypher.php';

class CaesarCypherTest extends TestCase
{
    public function setUp()
    {
        $this->caesarCypher = new CaesarCypher();
    }

    /**
     * @dataProvider addDataProvider
     */
    public function testShiftMessage($message, $shift, $left, $expected)
    {
        $messageShifted = $this->caesarCypher->shiftMessage($message, $shift, $left);

        $this->assertEquals($messageShifted, $expected);
    }

    public function addDataProvider(): array
    {
        return [
            ['abcd', 1, false, 'bcde'],
            ['THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, true,
                'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23, false, 'XYZABCDEFGHIJKLMNOPQRSTUVW'],
            ['I came, I saw, I conquered. (Julius Caesar)', 3, true,
                'F zxjb, F pxt, F zlknrboba. (Grifrp Zxbpxo)'],
            ['Bumbofbkzb fp qeb qbxzebo lc xii qefkdp. (Grifrp Zxbpxo)', 3, false,
                'Experience is the teacher of all things. (Julius Caesar)'],
            ['Ljnbja\'b fron vdbc kn jkxen bdbyrlrxw. (Sdurdb Ljnbja)', 9, true,
                'Caesar\'s wife must be above suspicion. (Julius Caesar)'],
            ['I found Rome a city of bricks and left it a city of marble. (Augustus)', 1, false,
                'J gpvoe Spnf b djuz pg csjdlt boe mfgu ju b djuz pg nbscmf. (Bvhvtuvt)'],
            ['Young men, hear an old man to whom old men hearkened when he was young. (Augustus)',
                40, false,
                'Mcibu asb, vsof ob czr aob hc kvca czr asb vsofysbsr kvsb vs kog mcibu. (Oiuighig)'],
        ];
    }
}
