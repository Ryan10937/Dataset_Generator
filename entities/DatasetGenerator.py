import inspect
from .ConfigReader import Config_Reader
import os
import pandas as pd
import sys
import os
sys.path.append('Dataset_Generator/')
import utils.transformation_functions as tfuncts 
class Dataset_Generator():
  '''
  Class that receives a folder of objects and folder of labels and returns a dataset generator 
  '''
  def __init__(self,config_path):
    self.config_path = config_path
    self.config = Config_Reader(self.config_path).config
    
  def _get_objects(self,item_name,item_extensions):
    
    item_path = self.config[item_name]
    if None in [item_path,item_name,item_extensions]:
      return []
    paths = []
    for root,folders,objects in os.walk(item_path):
      for object in objects:
        if object.split('.')[-1] in self.config[item_extensions]:
          paths.append(os.path.join(root,object))
    return paths
  def _get_item_label_pairs(self):
    objects = self._get_objects('object_folder','object_extensions')
    labels = self._get_objects('label_folder','label_extensions')

    def get_name(row,col_name):
      return row[col_name].split(os.sep)[-1].split('.')[0]
    objects = pd.DataFrame({'objects':objects})
    objects['name'] = objects.apply(get_name,col_name='objects',axis=1)
    labels = pd.DataFrame({'labels':labels})
    labels['name'] = labels.apply(get_name,col_name='labels',axis=1)
    objects = objects.merge(labels,how='inner',on='name')
    labels.to_csv('./tmp.csv')
    objects.to_csv('./tmp1.csv')
    # self.dataset_labels = [tfuncts.dataset_label(row['objects'],None if 'labels' not in row.keys() else row['labels']) for i,row in objects.iterrows()]
    self.dataset_labels = [tfuncts.dataset_label(row['objects'],row['labels']) for i,row in objects.iterrows()]

  def find_transformation_function(self):
    functions = inspect.getmembers(tfuncts,inspect.isfunction)
    self.transformation_function = [y for x,y in functions if x==self.config['transformation_function']][0]
    
  def run_pipeline(self):
    self._get_item_label_pairs()
    self.find_transformation_function()
    return (self.transformation_function(row) for row in self.dataset_labels)
