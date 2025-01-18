from typing import List
from textnode import TextType, TextNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> List[TextNode]:
    if not text:
        return [TextNode("", TextType.TEXT)]
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Use split_nodes_delimiter for bold, italic, and code
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Use your existing functions for images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes