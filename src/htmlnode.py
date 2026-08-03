class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag: str | None  = tag
        self.value: str | None = value
        self.chidlren: list[HTMLNode] | None = children
        self.props: dict | None = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        result = ""
        if self.props is None:
            return result
        
        for key in self.props.keys():
            result+=f'{key}="{self.props[key]}" '
        return result

    def __repr__(self):
        print(f"Tag : {self.tag}")
        print(f"Value : {self.value}")
        print(f"Children : {str(self.chidlren)}")
        print(f"Props : {self.props_to_html()}")

        