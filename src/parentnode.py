from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("!All parent nodes must have a value!")

        if self.children is None:
            raise ValueError("!All parent nodes must have children")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result+=child.to_html()
        result+=f"</{self.tag}>"
        return result