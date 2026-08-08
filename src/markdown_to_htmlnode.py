from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks,block_to_block_type,BlockType
from text_to_textnodes import text_to_textnodes
from textnode import TextType,  TextNode, text_node_to_html_node
def markdown_to_html_node(markdown) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div",children)


def block_to_html_node(block:str) -> ParentNode:
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return p_to_html_node(block)
    if block_type == BlockType.HEADING:
        return h_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ul_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ol_to_html_node(block)

    raise ValueError(f"{block} has an invalid type")

def text_to_children(text:str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def p_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def h_to_html_node(block:str):
    hash_count = 0
    for char in block:
        if char == "#":
            hash_count+=1
        else:
            break
    if hash_count + 1 >= len(block):
        raise ValueError(f"invalid heading level: {hash_count}")
    text = block[hash_count+1:]
    children = text_to_children(text)
    return ParentNode(f"h{hash_count}",children)

def code_to_html_node(block:str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text,TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code",[child])
    return ParentNode("pre",[code])

def quote_to_html_node(block:str) -> ParentNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid code block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ul_to_html_node(block:str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ul",html_items)
        

def ol_to_html_node(block:str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ",1)
        children = text_to_children(parts[1])
        html_items.append(ParentNode("li",children))
    return ParentNode("ol",html_items)



