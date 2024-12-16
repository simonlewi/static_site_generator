import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is not a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_textnode_not_equal_to_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, None)

    def test_textnode_url_equality(self):
        node1 = TextNode("Hello", "bold", "http://localhost:8888")
        node2 = TextNode("Hello", "bold", "http://localhost:8888")
        self.assertEqual(node1, node2)

    def test_textnode_no_url_equality(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bold")
        self.assertEqual(node1, node2)
    
    def test_text_node_different_url(self):
        node1 = TextNode("Hello", "bold", "https://localhost:8888")
        node2 = TextNode("Hello", "bold", "https://different.com")
        self.assertNotEqual(node1, node2)

    def test_text_node_repr_output(self):
        node = TextNode("Test", "code", "https://localhost:8888")
        expected_repr = "TextNode('Test', 'code', 'https://localhost:8888')"
        self.assertEqual(repr(node), expected_repr)
    

if __name__ == "__main__":
    unittest.main()
