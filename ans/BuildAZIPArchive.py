import os
from fs.osfs import OSFS # requirement pip install fs
from zipfile import ZipFile

'''def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path, file))
    get_zip_info(output_path)
'''
# https://www.linkedin.com/learning/python-code-challenges/build-a-zip-archive
def find_files(folderPath, files_ext):

    # create a basic file walker
    with OSFS(folderPath) as myfiles:
        path_files_list = list()
        for path in myfiles.walk.files(filter=files_ext):

            path_files_list.append(path)
    return path_files_list

def my_zip_all(folderPath='my_stuff/', files_ext=['bird.png'], zip_file_name='my_stuff2.zip'):
    path_files_list = find_files(folderPath, files_ext)

    with ZipFile(zip_file_name, "w") as zfile:
        for path in path_files_list:
            relative_path = f'{folderPath}{path[1:]}'

            # Put the bytes from filename into the archive under the name arcname.
            zfile.write(filename=relative_path, arcname=path)
    get_zip_info(zip_file_name)
    

def get_zip_info(zip_file_name):
    with ZipFile(zip_file_name, "r") as zfile:
        for fileInfo in zfile.infolist(): print(fileInfo.filename, fileInfo.file_size)
    
    
if __name__ == '__main__': 
    my_zip_all()
    # zip_all('my_stuff/', ['.png'], 'my_stuff1.zip')