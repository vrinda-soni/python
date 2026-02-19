#Q35
'''
Write a script that scans a folder, groups files by extension (.txt, .jpg, .pdf etc.), and moves
each file into a subfolder named after its extension using os and shutil.
'''

import os
import shutil

folder = "different_files"

for f in os.listdir(folder):
    path = os.path.join(f,folder)

if os.path.isfile(path):
    name,ext =os.path.splitext(f)

if ext:
    ext_folder = ext[1:]

final_folder = os.path.join(path,ext_folder)

os.mkdirs(final_folder , exist_ok=True)

shutil.move(path , os.path.join(final_folder , f))