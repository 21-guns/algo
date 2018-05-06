try:
    from xml.etree import cElementTree as ET
except Exception as e:
    from xml.etree import ElementTree as ET

file_name = "data.xml"
doc = ET.parse(file_name)