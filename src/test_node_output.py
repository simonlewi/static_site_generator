from textnode import TextNode, TextType
from inline_markdown import split_nodes_link, split_nodes_image

def test_split_links():
    # Test case 1 - ending with a link
    node1 = TextNode(
        "Hello [world](https://example.com)",
        TextType.TEXT
    )

    # Test case 2 - ending with text
    node2 = TextNode(
        "Hello [world](https://example.com) goodbye",
        TextType.TEXT
    )

    print("\nTest 1 (ending with link):")
    result1 = split_nodes_link([node1])
    for node in result1:
        print(f"Node type: {node.text_type}, Text: '{node.text}', URL: '{node.url if hasattr(node, 'url') else 'None'}'")

    print("\nTest 2 (ending with text):")
    result2 = split_nodes_link([node2])
    for node in result2:
        print(f"Node type: {node.text_type}, Text: '{node.text}', URL: '{node.url if hasattr(node, 'url') else 'None'}'")

if __name__ == "__main__":
    test_split_links()