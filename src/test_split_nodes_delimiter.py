import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("Normal value **Bold Value** Normal Value")
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "Bold Value")
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_italic(self):
        node = TextNode("Normal value _Italic Value_ Normal Value")
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "Italic Value")
        self.assertEqual(result[1].text_type, TextType.ITALIC)

    def test_code(self):
        node = TextNode("Normal value `Code Value` Normal Value")
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "Code Value")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_spacing(self):
        node = TextNode("Normal value `First``Code Value` Normal Value `Third`")
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2].text, "Code Value")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_nested(self):
        node = TextNode("Normal value `First**Bold Value**` Normal Value `Third`")
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[2].text, " Normal Value ")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/) and another [second link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com"),
            ],
            new_nodes,
        )

    def test_split_consequetive_links(self):
        node = TextNode(
            "[link](https://i.imgur.com/)[second link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/"),
                TextNode("second link", TextType.LINK, "https://i.imgur.com"),
            ],
            new_nodes,
        )

    def test_split_links_and_images(self):
        node = TextNode(
            "[link](https://i.imgur.com/)![image](https://i.imgur.com/lkajsdf.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes[1] = split_nodes_image([new_nodes[1]])[0]
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/lkajsdf.png"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
