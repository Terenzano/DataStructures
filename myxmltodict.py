import xmltodict
from pprint import pprint

xml_example = open("xml_example.xml").read()
pprint(xml_example)

print("\n")

xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
pprint(xml_dict)

print("\n")

pprint(int_name)

print("\n")

xml_data = xmltodict.unparse(xml_dict)
pprint(xml_data)

print("\n")

