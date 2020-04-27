import xmltodict
from pprint import pprint

# Get the XML file data
stream = open('sample.xml', 'r')

# Parse the XML file into an 'OderedDict'
xml = xmltodict.parse(stream.read())
pprint(xml)
print("\n")

print("Display all the people in the list:")


for e in xml["People"]["Person"]:
    print(e)

print("\n")

print("Display the second person in the list:")

person = xml["People"]["Person"][1]
print(person)

print("\n")
