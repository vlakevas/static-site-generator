import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from textnode import TextType,TextNode
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )
    def test_plain_text(self):
        text = "Just a plain string without markdown."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("Just a plain string without markdown.", TextType.TEXT)],
            nodes,
        )
    def test_multiple_bold(self):
        text = "This has **two** different **bold** sections."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
                TextNode(" different ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" sections.", TextType.TEXT),
            ],
            nodes,
        )
    def test_adjacent_types(self):
        text = "**bold**_italic_`code`"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
            ],
            nodes,
        )