from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    test_props = {
        "href":"www.maia.com"
    }
    test_node = LeafNode("a","I love maia",test_props)
    print(test_node.to_html())
    print(None)


if __name__ == "__main__":
    main()