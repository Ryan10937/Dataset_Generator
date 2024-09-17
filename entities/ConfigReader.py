import yaml
class Config_Reader():
  def __init__(self,config_path) -> None:
    self.config_path = config_path
    self.config = self.open_config()
  def open_config(self):
    with open(self.config_path) as f:
      try:
          config = yaml.safe_load(f)
      except yaml.YAMLError as exc:
          print(exc)
          return None
    return config
  ## def 
  # verify item and label paths
