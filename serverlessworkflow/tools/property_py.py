import re


class PropertyPy:
    def __init__(self, raw_name: str):
        self.raw_name = raw_name

    @property
    def property_name(self):
        return self.raw_name.split(":")[0].strip().replace("?", "")

    @property
    def property_type(self):
       # txt = re.search('export class (.+?) {', line).group(1)
        return self.raw_name.split(":")[1].strip().replace(";", "")

    def __repr__(self):
        return str({
            "raw_name": self.raw_name
        })