from textnode import TextNode, TextType
from extract_markdown_specials import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        split_values = old_node.text.split(delimiter)

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if len(split_values) == 1:
            new_nodes.append(old_node)
            continue
        elif len(split_values) == 2:
            raise ValueError("Invalid use of tags")
        else:
            for index in range(len(split_values)):
                if split_values[index]:
                    if index % 2 == 0:
                        new_nodes.append(
                            TextNode(split_values[index], old_node.text_type, url=None)
                        )
                    else:
                        new_nodes.append(
                            TextNode(split_values[index], text_type, url=None)
                        )

    # print(delimiter, new_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        cursor = 0
        for link in links:
            sub = f"[{link[0]}]({link[1]})"
            index = old_node.text.find(sub, cursor)
            if index != cursor:
                new_nodes.append(TextNode(old_node.text[cursor:index], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, url=link[1]))
            cursor = index + len(sub)

        if cursor < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[cursor:], TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_images(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        cursor = 0
        for link in links:
            sub = f"![{link[0]}]({link[1]})"
            index = old_node.text.find(sub, cursor)
            if index != cursor:
                new_nodes.append(TextNode(old_node.text[cursor:index], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.IMAGE, url=link[1]))
            cursor = index + len(sub)

        if cursor < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[cursor:], TextType.TEXT))
    return new_nodes
