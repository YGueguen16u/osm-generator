# src/way.py
class Way:
    def __init__(self, id, nodes, tags=None):
        self.id = id
        self.nodes = nodes
        self.tags = tags or []

    def to_xml(self):
        nodes_xml = ''.join([f'<nd ref="{node.id}"/>' for node in self.nodes])
        tags_xml = ''.join([f'<tag k="{k}" v="{v}"/>' for k, v in self.tags])
        return f'<way id="{self.id}">{nodes_xml}{tags_xml}</way>'