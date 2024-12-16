from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, other):
        if not isinstance(other, TextNode):
        # check if 'other' is an instance of TextNode
            return False
            # if not, return false as they cannot be equal
        
        # compare 'self' and 'other' properties
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"
    
def main():
    test_node = TextNode("Hello", TextType.BOLD, None)
    print(test_node)

main()

if __name__ == "__main__":
    main()
    



        
        
 