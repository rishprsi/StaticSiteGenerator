import unittest

from markdown_management import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownManagement(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_check_heading_type(self):
        md = "# This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_check_first_heading_type(self):
        md = "### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_check_second_heading_type(self):
        md = "###### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_check_invalid_heading_type(self):
        md = "####### This is a heading"
        self.assertNotEqual(block_to_block_type(md), BlockType.HEADING)

    def test_check_code_type(self):
        md = """``` This is a heading```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_check_invalid_code(self):
        md = """``Invalid code```"""
        self.assertNotEqual(block_to_block_type(md), BlockType.CODE)

    def test_check_multiline_code(self):
        md = """```
        Invalid code

        ```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_valid_quotes(self):
        md = """> Quote 1
> Quote 2
> Quote 3"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_invalid_quotes(self):
        md = """> Quote 1
> Quote 2
 Quote 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_valid_olist(self):
        md = """1. List 1
2. List2
3. List 3"""
        self.assertEqual(block_to_block_type(md), BlockType.OLIST)

    def test_invalid_olist(self):
        md = """1. List 1
2. List 2
 List 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.OLIST)

    def test_unordered_olist(self):
        md = """2. List 1
2. List 2
3. List 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.OLIST)

    def test_valid_ulist(self):
        md = """- UList 1
- UList 2
- UList 3"""
        self.assertEqual(block_to_block_type(md), BlockType.ULIST)

    def test_invalid_ulist(self):
        md = """- UList 1
- UList2
 UList 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.ULIST)


if __name__ == "__main__":
    unittest.main()
