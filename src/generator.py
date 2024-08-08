# src/generator.py
import random

from node import Node
from way import Way
from header import OSMHeader

class OSMGenerator:
    def __init__(self):
        self.nodes = []
        self.ways = []
        self.header = OSMHeader()

    def generate_node(self, id):
        lat = random.uniform(45.0, 46.0)
        lon = random.uniform(4.0, 5.0)
        node = Node(id, lat, lon)
        self.nodes.append(node)
        return node

    def generate_way(self, id, node_ids):
        nodes = [self.nodes[node_id] for node_id in node_ids]
        way = Way(id, nodes)
        self.ways.append(way)
        return way

    def to_xml(self):
        nodes_xml = ''.join([node.to_xml() for node in self.nodes])
        ways_xml = ''.join([way.to_xml() for way in self.ways])
        header_xml = self.header.to_xml()
        return f'{header_xml}{nodes_xml}{ways_xml}</osm>'

# main.py
if __name__ == "__main__":
    generator = OSMGenerator()
    for i in range(10):
        generator.generate_node(i)
    generator.generate_way(1, [0, 1, 2, 3, 4])
    print(generator.to_xml())
