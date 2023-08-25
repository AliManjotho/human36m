import os, zipfile

dir_extract = os.path.join('extracted')

for dir_path, dir_names, file_names in os.walk('./compressed'):
    dir = os.path.abspath(dir_path)
    
    for file in file_names:
        file_abs = os.path.join(dir, file)
        
        zip_ref = zipfile.ZipFile(file_abs)
        zip_ref.extractall(dir_extract)
        zip_ref.close()

        print(file, ' Done!')