# Dataset_Generator

## Purpose
To save time on arranging data to feed to a model, this script uses paths specified in the config file to return a generator of media-label pairs. 

## Usage
1. Clone this repository with https://github.com/Ryan10937/Dataset_Generator.git
1. Create a transformation function in utils/transformation_functions.py that will be used to transform your label into a customizable value 
1. Fill out fields in config file
   1. Object_folder: path to a folder of media to later pass to your model
    1. Object_extensions: extensions to look for (txt,jpg,xml)
    1. Label_folder: path to a folder of labels to later pass to your model (can be None)
    1. Label_extensions: extensions to look for (txt,jpg,xml)
    1. Transformation_function: name of function in utils/transformation_functions.py that receives a dataset_label class (see utils/transformation_functions.py) and returns a customizable value.
1. Import the DatasetGenerator class
1. Instantiate DatasetGenerator class and pass the path to your config file as a parameter ex: Dataset_Generator('configs/brain_tumor_classification_dataset.yaml')
1. Call the get_generator() method