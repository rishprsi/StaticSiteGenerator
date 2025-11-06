import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_invalid_leaf_node(self):
        node = LeafNode(None, None, None)
        print(node)
        self.assertRaises(ValueError, node.to_html)

    def test_tagged_output(self):
        node = LeafNode("p", "Some value", None)
        print(node)
        self.assertEqual(node.to_html(), "<p>Some value</p>")

    def test_non_tagged_output(self):
        node = LeafNode(None, "Some value", None)
        print(node)
        self.assertEqual(node.to_html(), "Some value")

    def test_tagegd_with_argument(self):
        node = LeafNode("a", "Link", {"href": "https://www.google.com"})
        print(node)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Link</a>')


if __name__ == "__main__":
    unittest.main()
