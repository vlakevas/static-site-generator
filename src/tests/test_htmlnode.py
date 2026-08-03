import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_1(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, test_props)
        matching_case = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), matching_case)

    def test_props_to_html_2(self):
        node = HTMLNode()
        matching_case = ""
        self.assertEqual(node.props_to_html(), matching_case)

    def test_props_to_html_3(self):
        test_props = {}
        node = HTMLNode(None, None, test_props)
        matching_case = ""
        self.assertEqual(node.props_to_html(), matching_case)

