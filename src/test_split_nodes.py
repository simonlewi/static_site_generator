import unittest
from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode("This is text with an image ![alt text](https://example.com/image.png)", TextType.TEXT)
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is plain text.", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is plain text.", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "Text with multiple images ![image1](https://example.com/img1.png) and ![image2](https://example.com/img2.png)",
            TextType.TEXT
        )
        expected = [
            TextNode("Text with multiple images ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://example.com/img1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://example.com/img2.png")
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Text with multiple links [link1](https://example.com/1) and [link2](https://example.com/2)",
            TextType.TEXT
        )
        expected = [
            TextNode("Text with multiple links ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "https://example.com/1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "https://example.com/2")
        ]
        self.assertEqual(split_nodes_link([node]), expected)

if __name__ == "__main__":
    unittest.main()