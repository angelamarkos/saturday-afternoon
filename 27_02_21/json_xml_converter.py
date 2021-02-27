import json

from xml.etree import ElementTree

def create_xml_tree(root, data):
    for k, v in data.items():
        if type(v) != dict:
            ElementTree.SubElement(root, k).text = str(v)
        else:
            create_xml_tree(ElementTree.SubElement(root, k), v)

    return root


with open('test.json', 'r') as json_file:
    data = json.loads(json_file.read())
    print(data)

    root = ElementTree.Element('widgets')
    create_xml_tree(root, data)
    tree = ElementTree.ElementTree(root)
    tree.write('new.xml')