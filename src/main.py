from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    test_props = {
        "href":"www.maia.com"
    }
    test_node = LeafNode("a","I love maia",test_props)
    test_node2 = ParentNode("p",[test_node])
    print(test_node2.to_html())
    


if __name__ == "__main__":
    main()