import unittest
from inline_markdown import (
    extract_markdown_images, extract_markdown_links
)

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        # Define test cases: (input_text, expected_output)
        image_test_cases = [
            ("No images here", []),
            ("![alt text](http://example.com/image.jpg)", [("alt text", "http://example.com/image.jpg")]),
            ("Some text with two images ![first](http://example.com/first.jpg) and ![second](http://example.com/second.jpg)",
             [("first", "http://example.com/first.jpg"), ("second", "http://example.com/second.jpg")])
        ]

        # Test the image extraction
        for input_text, expected_output in image_test_cases:
                result = extract_markdown_images(input_text)
                self.assertEqual(result, expected_output, f"Failed for input: {input_text}")

    def test_extract_links(self):
        # Define test cases: (input_text, expected_output)
        link_test_cases = [
            ("No links here", []),
            ("Here's a [link](http://example.com)", [("link", "http://example.com")]),
            ("Multiple links [first](http://example.com/first) and [second](http://example.com/second)",
             [("first", "http://example.com/first"), ("second", "http://example.com/second")])
        ]

        # Test the link extraction
        for input_text, expected_output in link_test_cases:
            result = extract_markdown_links(input_text)
            self.assertEqual(result, expected_output, f"Failed for input: {input_text}")
        

if __name__ == '__main__':
    unittest.main()
