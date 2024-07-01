import os
import shutil

# C:\Users\pansh\Downloads

my_path = input('Enter the path of the folder to organize: ')
folder_files = os.listdir(my_path)  # returns a list containing the names of the files within the given directory

for every_file in folder_files:
    # Splitext or split extension generate tuples with a file name and its extension
    file_name, extension = os.path.splitext(every_file)
    extension = extension[1:]

    if os.path.exists(my_path + '/' + extension + '_files'):
        shutil.move(my_path + '/' + every_file, my_path + '/' + extension + '_files')

    else:
        os.makedirs(my_path + '/' + extension + '_files')
        shutil.move(my_path + '/' + every_file, my_path + '/' + extension + '_files')

