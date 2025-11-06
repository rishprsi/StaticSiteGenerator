from markdown_management import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode, TextType
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from text_to_textnode import text_to_textnodes


def markdown_to_htmlnode(markdown) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        nodes.append(block_to_htmlnode(block))

    return ParentNode("div", nodes)


def block_to_htmlnode(block):
    type = block_to_block_type(block)
    if type == BlockType.PARAGRAPH:
        return paragraph_to_htmlnode(block)
    if type == BlockType.HEADING:
        return heading_to_htmlnode(block)
    if type == BlockType.CODE:
        return code_to_htmlnode(block)
    if type == BlockType.QUOTE:
        return quote_to_htmlnode(block)
    if type == BlockType.ULIST:
        return ulist_to_htmlnode(block)
    if type == BlockType.OLIST:
        return olist_to_htmlnode(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children


def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)


def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_htmlnode(block):
    text = block[4:-3]
    node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(node)
    code = ParentNode("code", [html_node])
    return ParentNode("pre", [code])


def quote_to_htmlnode(block):
    new_lines = []
    for line in block.split("\n"):
        text = line[2:].strip()
        new_lines.append(text)
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def ulist_to_htmlnode(block):
    lists = []
    for line in block.split("\n"):
        text = line[2:]
        children = text_to_children(text)
        lists.append(ParentNode("li", children))

    return ParentNode("ul", lists)


def olist_to_htmlnode(block):
    lists = []
    for line in block.split("\n"):
        text = line[3:]
        children = text_to_children(text)
        lists.append(ParentNode("li", children))

    return ParentNode("ol", lists)
