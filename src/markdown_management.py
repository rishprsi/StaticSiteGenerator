from enum import Enum

import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


block_regexes = {
    BlockType.HEADING: r"^#{1,6}\s(.+)$",
    BlockType.CODE: r"^```([\s\S]*?)```$",
    BlockType.QUOTE: r"^(>.*)$",
    BlockType.ULIST: r"^(-\s.*)$",
    BlockType.OLIST: r"^(\d+\.\s.*)$",
}


def markdown_to_blocks(markdown) -> list[str]:
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block:
            new_blocks.append(block.strip())

    return new_blocks


def block_to_block_type(block) -> BlockType:
    if re.fullmatch(block_regexes[BlockType.HEADING], block):
        return BlockType.HEADING
    if re.fullmatch(block_regexes[BlockType.CODE], block):
        return BlockType.CODE
    lines = block.split("\n")
    failed = False
    for line in lines:
        if not re.fullmatch(block_regexes[BlockType.QUOTE], line):
            failed = True
            break
    if not failed:
        return BlockType.QUOTE

    failed = False
    # print("Lines before ordered list", lines)
    for index in range(len(lines)):
        if (
            not lines[index]
            or not re.fullmatch(block_regexes[BlockType.OLIST], lines[index])
            or (int(lines[index].split(".")[0]) != (index + 1))
        ):
            failed = True
            break
    if not failed:
        return BlockType.OLIST

    failed = False
    for line in lines:
        if not re.fullmatch(block_regexes[BlockType.ULIST], line) or not line:
            failed = True
            break
    if not failed:
        return BlockType.ULIST

    return BlockType.PARAGRAPH
