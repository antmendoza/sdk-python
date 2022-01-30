import os
import re
from os import listdir


class PropertyPy:
    def __init__(self, raw_name: str):
        self.raw_name = raw_name

    @property
    def property_name(self):
        return self.raw_name.split(":")[0].strip().replace("?", "")

    @property
    def property_type(self):
        # txt = re.search('export class (.+?) {', line).group(1)
        result = self.raw_name
        result = result.split(":")[1].strip().replace(";", "")
        if "*/" in self.raw_name:
            result = self.raw_name[self.raw_name.index("*/")+2:]
        return result.replace(";","")


def __repr__(self):
        return str({
            "raw_name": self.raw_name
        })


constructor_body="""
# duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated


            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
"""


class ClassPy:
    def __init__(self, class_name, properties: [PropertyPy]):
        self.class_name = class_name
        self.properties = properties


    def write(self):

        property: PropertyPy
        properties = [prop for prop in self.properties if prop.property_name != "sourceModel"]

        file = open("./output/"+re.sub(r'(?<!^)(?=[A-Z])', '_', self.class_name).lower()+".py", "w")
        file.write("class "+self.class_name+":")
        file.write("\n ")
        for property in properties:
            file.write("    "+property.property_name + " : " +
                       self.propertyType(property.property_type) + " = None")
            file.write("\n ")


        file.write("    def __init__(self, " )
        file.write("\n ")
        for property in properties:
            file.write("        " + property.property_name + " : " +
                       self.propertyType(property.property_type) + " = None,")
            file.write("\n ")
        file.write("        **kwargs):" )
        file.write("\n ")
        for property in properties:
            #file.write("        self."+propert.property_name +"="+propert.property_name)
            #file.write("\n ")
            pass
        file.write(constructor_body)

    def propertyType(self, property_type: str):


        #result = property_type.lower();
        result = property_type;


        result = result.replace("string", "str")
        result = result.replace("boolean", "bool")

        if "|" in property_type:
            result = result.replace("|", ",")
            result = "Union[" + result + "]"



        if "[]]"  in property_type:
            result = result.removeprefix("[")
            result = result[:result.index(",")]
            result = "["+result+"]"
        elif "[]" in property_type:
            result = result.removesuffix("[]")
            result = "[" + result + "]"

        return result


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
        print(swf_file.name)
        if not swf_file.name.endswith("action.ts"):
            # continue
            pass

        classPy = method_name(swf_file)
        classPy.write()


