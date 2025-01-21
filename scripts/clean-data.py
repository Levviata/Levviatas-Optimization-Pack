import os
import glob

# Set the path to the folder
folder_path = '../data'

# Get all .json files in the folder
json_files = glob.glob(os.path.join(folder_path, '*.json'))

# Delete each .json file
for file in json_files:
    os.remove(file)
    print(f"Deleted: {file}")