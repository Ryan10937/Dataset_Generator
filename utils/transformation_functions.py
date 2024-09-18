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
