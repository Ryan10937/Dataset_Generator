import xmltodict
import json
import pandas as pd
class dataset_label():
  def __init__(self,media_path,label_path):
    self.media_path = media_path
    self.label_path = label_path
    self.value = None
    self.tree = None
  def open_json(self):
    with open(self.label_path) as f:
      label=json.load(f)
    self.value=label
    return label
  def open_xml(self):
    print("opening ",self.label_path)
    try:
      with open(self.label_path,'r') as f:
        label=f.read()
      self.value=xmltodict.parse(label)#problem is that every time the label is opened, it resets its self value and doesnt get sent through the transformation function
      return self.value###remove
    except:
      print('Error when reading XML')
      return None
  

##################################################################
##################################################################
####################Transformation Functions######################
############# Should always accept and return label ##############
##################################################################

def get_class_from_image_path(label):
  import os
  return label.media_path,label.media_path.split(os.sep)[-2]


def get_class_from_fashion_xml(label):
  if label == None:
    print('label is none')
  if label.label_path == None:
    print('label_path is none')
    return label
  label_dict = label.open_xml()
  if label_dict == None:
    print('label_dict is none')
    return label
  print(label_dict['annotation'].keys())
  
  coords_dict = {'xmin':float(label_dict['annotation']['object']['bndbox']['xmin']),
                'ymin':float(label_dict['annotation']['object']['bndbox']['ymin']),
                'xmax':float(label_dict['annotation']['object']['bndbox']['xmax']),
                'ymax':float(label_dict['annotation']['object']['bndbox']['ymax'])}
  label.value = coords_dict
  # return label.media_path,coords_dict
  return label

def get_brain_mri_class_from_json(label):

  if label.label_path == None or pd.isna(label.label_path):
    return label
  else:
    print("opening json")
    print('not ready to open json yet')