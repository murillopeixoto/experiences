<?php

class CaesarCypher
{
    const ALPHABET_SIZE = 26;
    const ORDER_POINTS = [
        'upper' => [
            'begin' => 65, // ord('A')
            'end' => 90 // ord('Z')
        ],
        'lower' => [
            'begin' => 97, // ord('a')
            'end' => 122 // ord('z')
        ]
    ];

    public function shiftMessage($message, $shift=3, $left=false)
    {
        $shift = $this->normalizeShiftSize($shift);
        if ($left) {
            $shift = -$shift;
        }

        $shifted = [];
        foreach (str_split($message) as $char) {
            $shifted[] = $this->moving($char, $shift);
        }

        return implode($shifted);
    }

    private function moving($char, $shift)
    {
        $case = $this->getCase($char);
        if (!$case) {
            return $char;
        }

        $position = ord($char) + $shift;
        if ($position > self::ORDER_POINTS[$case]['end']) {
            $position = $position - self::ALPHABET_SIZE;
        } elseif ($position < self::ORDER_POINTS[$case]['begin']) {
            $position = $position + self::ALPHABET_SIZE;
        }

        return chr($position);
    }

    private function getCase($char)
    {
        if (ord($char) >= self::ORDER_POINTS['upper']['begin'] &&
                ord($char) <= self::ORDER_POINTS['upper']['end']) {
            return 'upper';
        } elseif (ord($char) >= self::ORDER_POINTS['lower']['begin'] &&
                ord($char) <= self::ORDER_POINTS['lower']['end']) {
            return 'lower';
        } else {
            return false;
        }
    }

    private function normalizeShiftSize($shift)
    {
        while ($shift > self::ALPHABET_SIZE) {
            $shift = $shift - self::ALPHABET_SIZE;
        }

        return $shift;
    }
}
