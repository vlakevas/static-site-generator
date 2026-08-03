import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Testing Link", {"href": "www.link.com", "att": "value"})
        self.assertEqual(
            node.to_html(), '<a href="www.link.com" att="value">Testing Link</a>'
        )

    def test_no_tag(self):
        node = LeafNode(None, "some raw text")
        self.assertEqual(node.to_html(), "some raw text")

    def test_missing_value(self):
        node = LeafNode("h1", None)
        self.assertRaises(ValueError, node.to_html)
