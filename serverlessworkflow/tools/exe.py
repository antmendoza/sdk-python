import os
import re
from os import listdir

from serverlessworkflow.tools.property_py import PropertyPy


class ClassPy:
    def __init__(self, class_name, properties: [PropertyPy]):
        self.class_name = class_name
        self.properties = properties


    def write(self):
        file = open("../"+self.class_name+".py", "w")
        file.write("class "+self.class_name+":")
        file.write("\n ")


        file.write("    def __init__(self, " )
        file.write("\n ")
        propert: PropertyPy
        properties = [prop for prop in self.properties if prop.property_name != "sourceModel"]
        for propert in properties:
            file.write("        "+propert.property_name +": None,")
            file.write("\n ")
        file.write("        ):" )
        file.write("\n ")
        for propert in properties:
            file.write("        self."+propert.property_name +"="+propert.property_name)
            file.write("\n ")


def method_name(file):
    print(file.name)
    properties: [PropertyPy] = []
    class_name: str
    reading: bool = False
    for line in file.readlines():

        striped_line = line.strip()
        if striped_line == "":
            continue

        if striped_line.startswith("constructor"):
            break

        if reading:
            if striped_line.startswith("/") or striped_line.startswith("*")\
                    or striped_line.startswith("|")\
                    or striped_line.startswith("[")\
                    or striped_line.startswith("}")\
                    :
                continue

            properties.append(PropertyPy(striped_line))

        if "export class" in line:
            class_name = re.search('export class (.+?) {', line).group(1)
            reading = True



    return ClassPy(class_name, properties)





examples_dir = os.path.join(os.path.dirname(__file__), './classes')
examples = listdir(examples_dir)
for example in examples:
    with open(examples_dir + "/" + example, "r") as swf_file:
        classPy = method_name(swf_file)
        classPy.write()


