# Convert TextNode to HTMLNode
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    # "If you see this type of text, here's how to convert it"
    text_type_to_node = {
        TextType.TEXT: lambda node: LeafNode(None, node.text),
        TextType.BOLD: lambda node: LeafNode("b", node.text),
        TextType.ITALIC: lambda node: LeafNode("i", node.text),
        TextType.CODE: lambda node: LeafNode("code", node.text),
        TextType.LINK: lambda node: LeafNode("a", node.text, {"href": node.url}),
        TextType.IMAGE: lambda node: LeafNode("img", "", {"src": node.url, "alt": node.text})
    }

    if text_node.text_type in text_type_to_node:
        # Check if we have a rule for this type of text
        return text_type_to_node[text_node.text_type](text_node)
    else:
        # If no, complain that we don't know how to handle it
        raise ValueError("Invalid text type")