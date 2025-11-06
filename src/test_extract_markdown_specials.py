import unittest

from extract_markdown_specials import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownSpecials(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com)"
        )
        self.assertListEqual([("link", "https://i.imgur.com")], matches)

    def test_extract_markdown_invalid(self):
        matches = extract_markdown_links("This is text with an ![invalid]i.imgur.com)")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
