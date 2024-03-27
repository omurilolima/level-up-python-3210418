import os
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        #  Use os.walk for search the files in a directory
        #  The fist element of for, root, is the path to a directory
        #  The second is a list of the subdirectories within the root. 
        #    - Use _ to indicate that is an unused variable
        #  The third element is a list of all the files in the root directory
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path, file))

zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')