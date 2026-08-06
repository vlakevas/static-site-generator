from textnode import TextType, TextNode
from extract_images_links import extract_markdown_links,extract_markdown_images
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid MD syntax")

        parts = old_node.text.split(delimiter)

        for i,part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part,TextType.TEXT))
            else:
                new_nodes.append(TextNode(part,text_type))




    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        image_tuples = extract_markdown_images(old_node.text)

        if len(image_tuples) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for image in image_tuples:
            image_alt = image[0]
            image_url = image[1]
            sections = original_text.split(f"![{image_alt}]({image_url})",1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(image_alt,TextType.IMAGE,image_url))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        link_tuples = extract_markdown_links(old_node.text)

        if len(link_tuples) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for link in link_tuples:
            link_alt = link[0]
            link_url = link[1]
            sections = original_text.split(f"[{link_alt}]({link_url})",1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(link_alt,TextType.LINK,link_url))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT))
    return new_nodes


        