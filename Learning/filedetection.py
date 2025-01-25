import os 

file_path='text.txt'

if os.path.exists(file_path):
    print(f"The File Path exists in {file_path} location!")
    if os.path.isfile(file_path):
        print(f"File is a file in {file_path} location!")
    elif os.path.isdir(file_path):
        print(f"File is a directory in {file_path} location!")
else:
    print(f"File does not exist in {file_path} location!")