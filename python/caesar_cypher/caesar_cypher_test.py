import pytest
from caesar_cypher import CaesarCypher

testdata = [
    ('abcd', 1, False, 'bcde'),
    ('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, True,
        'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23, False, 'XYZABCDEFGHIJKLMNOPQRSTUVW'),
    ('I came, I saw, I conquered. (Julius Caesar)', 3, True,
        'F zxjb, F pxt, F zlknrboba. (Grifrp Zxbpxo)'),
    ('Bumbofbkzb fp qeb qbxzebo lc xii qefkdp. (Grifrp Zxbpxo)', 3, False,
        'Experience is the teacher of all things. (Julius Caesar)'),
    ('Ljnbja\'b fron vdbc kn jkxen bdbyrlrxw. (Sdurdb Ljnbja)', 9, True,
        'Caesar\'s wife must be above suspicion. (Julius Caesar)'),
    ('I found Rome a city of bricks and left it a city of marble. (Augustus)', 1, False,
        'J gpvoe Spnf b djuz pg csjdlt boe mfgu ju b djuz pg nbscmf. (Bvhvtuvt)'),
    ('Young men, hear an old man to whom old men hearkened when he was young. (Augustus)', 40,
        False, 'Mcibu asb, vsof ob czr aob hc kvca czr asb vsofysbsr kvsb vs kog mcibu. (Oiuighig)')
]


class TestCaesarCypher(object):
    caesar_cypher = CaesarCypher()

    @pytest.mark.parametrize("message,shift,left,expected", testdata)
    def test_shift_message(self, message, shift, left, expected):
        message_shifted = self.caesar_cypher.shift_message(message, shift, left)

        assert message_shifted == expected
