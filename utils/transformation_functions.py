import xml.etree.ElementTree as ET
class dataset_label():
  def __init__(self,media_path,label_path):
    self.media_path = media_path
    self.label_path = label_path
  def open_json(self):
    pass
  def open_xml(self):
    pass
def get_class_from_image_path(label):
  import os
  return label.media_path,label.media_path.split(os.sep)[-2]
def get_class_from_fashion_xml(label):
  if label == None:
    print('label is none')
    return label.media_path,{}
  if label.label_path == None:
    print('label_path is none')
    return label.media_path,{}
  root = ET.parse(label.label_path).getroot()
  coords = root[6][4]
  coords_dict = {'xmin':float(coords[0].text),
                'ymin':float(coords[1].text),
                'xmax':float(coords[2].text),
                'ymax':float(coords[3].text)}
  return label.media_path,coords_dict

