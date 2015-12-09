"""
It is a class implementing the Caesar Cipher concept.
The method shift_message will receive the message that you want to encrypt or decrypt. You can pass
the amount of positions to shift with the second param and choose the direction passing True or
False. if you pass True, the direction will be left; False will move to the right.

Caesar Cipher : http://en.wikipedia.org/wiki/Caesar_cipher
"""


class CaesarCypher(object):
    alphabet_size = 26
    ord_points = {
        'upper': {
            'begin': ord('A'),
            'end': ord('Z')
        },
        'lower': {
            'begin': ord('a'),
            'end': ord('z')
        }
    }

    def shift_message(self, message, shift=3, left=False):
        shift = self.__normalize_shift_size(shift)
        if left:
            shift = -shift

        return ''.join([self.__moving(char, shift) for char in message])

    def __moving(self, char, shift):
        case = self.__get_case(char)
        if not case:
            return char

        position = ord(char) + shift
        if position > self.ord_points[case]['end']:
            position = position - self.alphabet_size
        elif position < self.ord_points[case]['begin']:
            position = position + self.alphabet_size

        return chr(position)

    def __get_case(self, char):
        if ord(char) >= self.ord_points['upper']['begin'] and\
                ord(char) <= self.ord_points['upper']['end']:
            return 'upper'
        elif ord(char) >= self.ord_points['lower']['begin'] and\
                ord(char) <= self.ord_points['lower']['end']:
            return 'lower'
        else:
            return False

    def __normalize_shift_size(self, shift):
        while shift > self.alphabet_size:
            shift = shift - self.alphabet_size

        return shift
