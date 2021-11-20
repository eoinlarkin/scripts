# Script to convert files to folders

# Get filename without the file extension
# Example code sourced from following StackOverFlow post:
# https://stackoverflow.com/questions/22207936/how-to-find-files-and-skip-directories-in-os-listdir

import os   # for scaning and checking directory
import shutil # for moving files

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

createFiles = yes_or_no('Do you want to create folders from filenames?')

dir = '.'
for item in os.scandir(dir):
    if item.is_dir():
        print('This is a directoy: ' + item.name)
    else:
        print('This is a file: ' + item.name)
        print('This is a file with no filename: ' + item.name.rsplit('.', 1)[0])
        print('This is the file extension: ' + item.name.rsplit('.', 1)[1])

        fName = item.name
        dirName = item.name.rsplit('.', 1)[0]

        if (not os.path.isdir(dirName)) and (createFiles) and(item.name.rsplit('.', 1)[1] != 'py'):
            os.makedirs(dirName)
            shutil.move(fName, "./" + dirName + "/" + fName)



