import unittest
from markdown_blocks import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")
        self.assertNotEqual(block_to_block_type("####### Invalid heading"), "heading")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nCode block\n```"), "code")
        self.assertNotEqual(block_to_block_type("` Not a code block"), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), "quote")
        self.assertNotEqual(block_to_block_type("Not a quote"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertNotEqual(block_to_block_type("Item 1\nItem 2"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1. First\n3. Third\n2. Second"), "ordered_list")
        self.assertNotEqual(block_to_block_type("Not an ordered list"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), "paragraph")
        self.assertNotEqual(block_to_block_type("# This is a heading"), "paragraph")

if __name__ == "__main__":
    unittest.main()
