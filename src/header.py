# src/header.py

class OSMHeader:
    def __init__(self, generator="CGImap 0.9.3", version="0.6",
                 copyright="OpenStreetMap and contributors",
                 attribution="http://www.openstreetmap.org/copyright",
                 license="http://opendatacommons.org/licenses/odbl/1-0/",
                 bounds=None):
        self.version = version
        self.generator = generator
        self.copyright = copyright
        self.attribution = attribution
        self.license = license
        self.bounds = bounds or {"minlat": 45.0, "minlon": 4.0, "maxlat": 46.0, "maxlon": 5.0}

    def to_xml(self):
        bounds_xml = f'<bounds minlat="{self.bounds["minlat"]}" minlon="{self.bounds["minlon"]}" maxlat="{self.bounds["maxlat"]}" maxlon="{self.bounds["maxlon"]}"/>'
        header_xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
                      f'<osm version="{self.version}" generator="{self.generator}" '
                      f'copyright="{self.copyright}" attribution="{self.attribution}" '
                      f'license="{self.license}">\n'
                      f'{bounds_xml}\n')
        return header_xml

# src/generator.py
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
