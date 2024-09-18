
from entities.ConfigReader import Config_Reader
from entities.DatasetGenerator import Dataset_Generator
if __name__ == '__main__':
  dataset_generator = Dataset_Generator('configs/brain_tumor_classification_dataset.yaml')
  generator = dataset_generator.run_pipeline()
  for _ in range(10):
    print(next(generator))
