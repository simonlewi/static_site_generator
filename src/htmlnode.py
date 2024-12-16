class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        self.props = {} if props is None else props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        attributes = []
        for key, value in self.props.items():
            formatted = f'{key}="{value}"'
            attributes.append(formatted)
        
        return ' '.join(attributes)
    
    def __repr__(self):
        children_repr = f'Children({len(self.children)})' if self.children else 'No Children'
        props_repr = f'Props({len(self.props)})' if self.props else 'No Props'
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, {children_repr}, {props_repr})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required for rendering HTML")
        if self.tag is None:
            return self.value
        
        html = '<' + self.tag

        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
            
        html += '>'
        html += self.value
        html += f'</{self.tag}>'

        return html
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag present")
        if self.children == None:
            raise ValueError("Children is missing!")
    
        html = '<' + self.tag + '>'
    
        for child in self.children:
            child_html = child.to_html()
            html += child_html

        html += f'</{self.tag}>'
        return html


            
        

        
    




    
    





