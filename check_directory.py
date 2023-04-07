import os
import shutil

# use os.path.expanduser() to get the user's home directory
home_dir = os.path.expanduser("~")

# use os.path.join() to construct the path to the source directory
source_dir = os.path.join(home_dir, 'Pictures')

# use os.path.join() to construct the path to the destination directory
destination_dir = os.path.join(home_dir, 'Desktop')


""" if os.path.exists(source_dir):
    print("Source directory exists.")
else:
    print("Source directory does not exist.")
if os.access(source_dir, os.R_OK):
    print("You have read access to the source directory.")
else:
    print("You do not have read access to the source directory.")
files = os.listdir(source_dir)
if files:
    print("Source directory contains files.")
    for file in files:
        if file.endswith('.jpg'):
            print(file)
else:
    print("Source directory is empty.") """


