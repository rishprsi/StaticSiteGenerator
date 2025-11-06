import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        node = HTMLNode(
            "p", "Value", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        node_props = node.props_to_html()
        self.assertEqual(node_props, ' href="https://www.google.com" target="_blank"')

    def test_return(self):
        node = HTMLNode("p", "Something", None, {"href": "www.xyz.com"})
        representation = repr(node)
        self.assertEqual(
            representation, "HTMLNode(p, Something, None, {'href': 'www.xyz.com'})"
        )

    def test_none_props_eq(self):
        node = HTMLNode("p", "This is a text node", None, None)
        node_props = repr(node)
        self.assertEqual(node_props, "HTMLNode(p, This is a text node, None, None)")


#    def test_invalid_def(self):
#        self.assertRaises(Exception, HTMLNode, "p", None, None, None)


if __name__ == "__main__":
    unittest.main()
