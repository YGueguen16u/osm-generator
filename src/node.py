# src/node.py
import random

class Node:
    def __init__(self, id, lat, lon, tags=None):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.tags = tags or []

    def to_xml(self):
        tags_xml = ''.join([f'<tag k="{k}" v="{v}"/>' for k, v in self.tags])
        return f'<node id="{self.id}" lat="{self.lat}" lon="{self.lon}">{tags_xml}</node>'
