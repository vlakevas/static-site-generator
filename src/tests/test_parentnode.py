import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_deeply_nested(self):
        leaf_node = LeafNode("b", "deepest text")
        great_grandchild_node = ParentNode("span", [leaf_node])
        grandchild_node = ParentNode("p", [great_grandchild_node])
        parent_node = ParentNode("div", [grandchild_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><span><b>deepest text</b></span></p></div>",
        )

    def test_to_html_mixed_children(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                ParentNode("span", [LeafNode("i", "nested italic")]),
                LeafNode(None, "Just some text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold text</b><span><i>nested italic</i></span>Just some text</div>",
        )
