import unittest

from transform_markdown import extract_title, generate_page


class TestTransformMarkdown(unittest.TestCase):
    def test_valid_extract_title(self):
        title = extract_title("# Sample Title")
        self.assertEqual(title, "Sample Title")

    def test_invalid_extract_title(self):
        self.assertRaises(Exception, extract_title, "## Wrong Title")


if __name__ == "__main__":
    unittest.main()
