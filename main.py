
from entities.ConfigReader import Config_Reader
from entities.DatasetGenerator import Dataset_Generator
if __name__ == '__main__':
  generator = Dataset_Generator('configs/dataset.yaml').run_pipeline()
  for _ in range(10):
    print(next(generator))
