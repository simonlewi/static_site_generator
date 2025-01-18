import unittest
from textnode import TextType, TextNode
from inline_markdown import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    
    # Tests if the function correctly detects and parses bold text (**bold**)
    def test_bold_text(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[2].text, " text.")
    
    # Tests if the function correctly detects and parses italic text (*italic*)
    def test_italic_text(self):
        text = "This is *italic* text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[2].text, " text.")

    # Tests if the function correctly detects and parses code text (`code`)
    def test_code_text(self):
        text = "This is `code` text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[2].text, " text.")

    # Tests if the function correctly detects and parses an image markdown with alt text and URL
    def test_image_text(self):
        text = "This is an ![alt text](http://example.com/image.jpg) in text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is an ")
        self.assertEqual(nodes[1].text, "alt text")
        self.assertEqual(nodes[1].url, "http://example.com/image.jpg")
        self.assertEqual(nodes[2].text, " in text.")
    
    # Tests if the function correctly detects and parses a link markdown with text and URL
    def test_link_text(self):
        text = "This is a [link](http://google.com) in text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].url, "http://google.com")
        self.assertEqual(nodes[2].text, " in text.")

    # Tests if the function can correctly parse multiple patterns in a single string
    def test_multiple_patterns(self):
        text = "This is **bold**, *italic*, and `code` with a ![image](http://example.com) and a [link](http://google.com)."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 11)  # 5 formatted nodes + 6 text nodes
        # Check text types in order
        expected_types = [
            TextType.TEXT,    # "This is "
            TextType.BOLD,    # "bold"
            TextType.TEXT,    # ", "
            TextType.ITALIC,  # "italic"
            TextType.TEXT,    # ", and "
            TextType.CODE,    # "code"
            TextType.TEXT,    # " with a "
            TextType.IMAGE,   # "image"
            TextType.TEXT,    # " and a "
            TextType.LINK,    # "link"
            TextType.TEXT,    # "."
        ]
        for i, node in enumerate(nodes):
            self.assertEqual(node.text_type, expected_types[i])

    # Tests if the function returns an empty list when no patterns are matched
    def test_no_patterns(self):
        text = "This is plain text with no formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is plain text with no formatting.")

    # Tests if the function correctly handles an empty string
    def test_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "")

if __name__ == "__main__":
    unittest.main()