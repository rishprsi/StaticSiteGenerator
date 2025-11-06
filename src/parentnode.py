from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Node has no tag present")
        if not self.children:
            raise ValueError("Node has no children")

        final = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            final += child.to_html()

        final += f"</{self.tag}>"
        return final
