import unittest

from text_to_html import text_node_to_html_node, TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("alt text", TextType.IMAGE, "https://www.boot.dev/image")
        print(node.__dict__)  # This will show us the attributes
        # Test regular text
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"

        # Test bold text
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "Bold text"

        # Test italic text
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "i"
        assert html_node.value == "Italic text"

        # Test code text
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "code"
        assert html_node.value == "Code text"

        # Test link
        text_node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "Click me"
        assert html_node.props["href"] == "https://www.boot.dev"

        # Test image
        text_node = TextNode("Alt text", TextType.IMAGE, "https://www.boot.dev/image")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        print("Props:", html_node.props)
        assert html_node.props["src"] == "https://www.boot.dev/image"
        assert html_node.props["alt"] == "Alt text"

        # Test invalid type
        try:
            text_node = TextNode("Invalid", "invalid_type")
            text_node_to_html_node(text_node)
            assert False, "Invalid type should raise an exception"
        except Exception:
            assert True

if __name__ == "__main__":
    unittest.main()