import os
import app
import unittest
import tempfile

class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
