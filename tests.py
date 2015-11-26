import os
import app
import unittest
import tempfile

class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_manipulator(self):
        from app.textManipulate import Text
        text = Text('brian')

        assert text.backwards() == 'nairb'
        assert text.palindrome() == 'brianairb'
        assert text.piglatin() == 'ianbray'

    def test_encoder(self):
        from app.textEncode import encodeText
        assert encodeText("Brian") == "29915"


if __name__ == '__main__':
    unittest.main()
