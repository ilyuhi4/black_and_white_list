import unittest

from main import main


class Test_main(unittest.TestCase):
    def setUp(self) -> None:
        self.white_words = {'god', 'blue'}
        self.black_words = {'pig', 'meat', 'kill'}
        self.good_text = "Отличный текст"
        self.bad_text = "Текст не годится"
        self.bad_words_in_texts = [
            'With this pig we will live together. With God we trust in blue skies.',
            ' With this man we will buy kill somebody. With God we trust in blue skies.',
            ' With this man we will buy kill this pig and eat its meat. With God we trust in blue skies.',
            ' I love this man',
            'Earth at the end of days'
        ]
        self.good_words_in_texts = [
            'Blue folder with my god',
            'God blue sea',
        ]

    def test_bad_words(self):
        for text in self.bad_words_in_texts:
            with self.subTest(text):
                self.assertEqual(main(text, self.white_words, self.black_words)
                                 , self.bad_text)

    def test_good_words(self):
        for text in self.good_words_in_texts:
            with self.subTest(text):
                self.assertEqual(main(text, self.white_words, self.black_words)
                                 , self.good_text)


if __name__ == '__main__':
    unittest.main()