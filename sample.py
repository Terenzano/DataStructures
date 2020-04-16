import xml.etree.ElementTree as ET 

#Get the XML file data
stream = open('sample.xml','r')

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #print the "Id" attribute of the Element object
    print(e.get("Id"))

    