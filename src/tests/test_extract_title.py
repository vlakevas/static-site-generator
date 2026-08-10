from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title1(self):
        self.assertEqual(extract_title("# HeaderTitle"),"HeaderTitle")