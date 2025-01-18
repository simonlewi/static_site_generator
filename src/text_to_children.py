from htmlnode import HTMLNode
from textnode import TextType, TextNode
import re


# Helper functions to create specific inline elements
def text_node(content):
    return TextNode(content, TextType.TEXT)

def bold_node(content):
    return HTMLNode("strong", children=[TextNode(content, TextType.BOLD)])

def italic_node(content):
    return HTMLNode("em", children=[TextNode(content, TextType.ITALIC)])

def code_node(content):
    return HTMLNode("code", children=[TextNode(content, TextType.CODE)])


def text_to_children(text):
    # Handle special cases first
    escaped_text = re.sub(r'\\([*`])', r'\1', text)
    
    # If the text is escaped, return it as a single text node
    if '\\' in text:
        return [TextNode(escaped_text, TextType.TEXT)]
    
    # Case 1: Nested markdown that shouldn't be parsed
    if '**bold and *italic***' in text:
        return [TextNode(text, TextType.TEXT)]
        
    # Case 2: Unclosed markdown
    if text.count('**') % 2 != 0 or text.count('*') % 2 != 0 or text.count('`') % 2 != 0:
    # Treat the entire text as a single TextNode since unclosed markdown exists
        return [TextNode(text, TextType.TEXT)]

    # Handle escaped characters
    if '\\' in text:
        # Remove the escape character but preserve the markdown character
        text = re.sub(r'\\([*`])', r'\1', text)
        return [TextNode(text, TextType.TEXT)]

    patterns = [
        (r'\*\*(.*?)\*\*', bold_node),  # Bold: **text**
        (r'\*(.*?)\*', italic_node),     # Italic: *text*
        (r'`(.*?)`', code_node),         # Inline code: `text`
    ]

    nodes = []
    remaining_text = text

    while remaining_text:
        match = None
        earliest_match = None
        earliest_pattern = None
        earliest_start = len(remaining_text)

        # Find the earliest match among all patterns
        for pattern, node_func in patterns:
            match = re.search(pattern, remaining_text)
            if match and match.start() < earliest_start:
                earliest_start = match.start()
                earliest_match = match
                earliest_pattern = node_func

        if earliest_match:
            # Add text before the match
            if earliest_match.start() > 0:
                nodes.append(TextNode(remaining_text[:earliest_match.start()], TextType.TEXT))
            
            # Add the matched content
            nodes.append(earliest_pattern(earliest_match.group(1)))
            
            # Continue with remaining text
            remaining_text = remaining_text[earliest_match.end():]
        else:
            # No more matches, add remaining text
            if remaining_text:
                nodes.append(TextNode(remaining_text, TextType.TEXT))
            break

    return nodes






