import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Arrange
        node = HTMLNode(props={})
        
        # Act
        result = node.props_to_html()
        
        # Assert
        self.assertEqual(result, "", "props_to_html with empty props should return an empty string")
    
    def test_props_to_html_with_data(self):
        # Arrange
        props = {"href": "https://www.example.com", "target": "_blank"}
        node = HTMLNode(props=props)
        
        # Act
        result = node.props_to_html()
        
        # Assert
        expected = 'href="https://www.example.com" target="_blank"'
        self.assertEqual(result, expected, "props_to_html did not format props correctly")

class TestLeafNode(unittest.TestCase):
    def test_simple_leaf_node(self):
    # Create a paragraph node with text
        node = LeafNode("p", "Hello, world!")
    
    # Test that it renders correctly
        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>",
            "LeafNode did not render simple tag correctly"
        )
    def test_leaf_node_no_tag(self):
    # Create a leaf node with no tag, just text
        node = LeafNode(None, "Just plain text")
    
    # Test that it renders just the text without any tags
        self.assertEqual(
            node.to_html(),
            "Just plain text",
            "LeafNode with no tag should return just the text value"
        )
    def test_leaf_node_no_value(self):
    # Test that creating a leaf node with no value raises ValueError
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_leaf_node_with_props(self):
    # Create a leaf node with href attribute
        node = LeafNode(
            "a", 
            "Click me!",
            {"href": "https://www.boot.dev", "target": "_blank"}
        )
    
    # Test that it renders with the attributes
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev" target="_blank">Click me!</a>',
            "LeafNode did not render props correctly"
        )
class TestParentNode(unittest.TestCase):
    # Test 1: Verify that ParentNode requires children parameter
    def test_no_children(self):
        try:
            # Try to create a ParentNode without required children parameter
            node = ParentNode("div")
            self.fail("Test failed - should have raised TypeError")
        except TypeError:
            pass
    
    # Test 2: Verify that empty children list is valid
    def test_empty_children_list(self):
        try:
            # Create node with empty children list
            node = ParentNode("div", [])
            html = node.to_html()
            # Check if it creates proper empty div tags
            self.assertEqual(html, "<div></div>")
        except ValueError:
            self.fail("Should allow empty children list")

    # Test 3: Verify nested ParentNode structures work
    def test_nested_parent_nodes(self):
        # Create nested structure: main -> div -> span
        child_node = ParentNode("div", [LeafNode("span", "Hello")])
        parent_node = ParentNode("main", [child_node])
        html = parent_node.to_html()
        # Verify correct nesting and HTML generation
        self.assertEqual(html, "<main><div><span>Hello</span></div></main>")

    # Test 4: Verify mixture of ParentNodes and LeafNodes work together
    def test_mixed_children(self):
        # Create complex structure with both types of nodes
        children = [
            LeafNode("b", "Bold"),
            ParentNode("div", [LeafNode("span", "Nested")])
        ]
        node = ParentNode("p", children)
        html = node.to_html()
        # Verify correct HTML generation with mixed node types
        self.assertEqual(html, "<p><b>Bold</b><div><span>Nested</span></div></p>")

    # Test 5: Verify that ParentNode requires a valid tag
    def test_no_tag(self):
        try:
            # Create a ParentNode with None as tag (invalid)
            node = ParentNode(None, [LeafNode("span", "Test")])
            # Try to generate HTML from invalid node
            node.to_html()
            self.fail("Should have raised ValueError")
        except ValueError:
            # ValueError should be raised when trying to generate HTML with no tag
            pass


if __name__ == "__main__":
    unittest.main()

