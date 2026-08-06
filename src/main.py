from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from split_delimiter import split_nodes_delimiter


def main():
    

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    print(new_nodes)
    


if __name__ == "__main__":
    main()