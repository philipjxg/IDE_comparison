# Description
# 
#____

import os
from os import walk


# Output full path of an inputted file name (incl. extension)
def get_fullPath_of_fileName(fileName):

    # Get full path of current directory 
    directoryFullPath = os.getcwd()

    # Identify all occurences of the file name in entire directory and add them to a list, where an element is the full path of the file name
    listOfFilesFound=[]
    for root, _, files in walk(directoryFullPath):
        for file in files:
            if file.lower() == fileName.lower(): 
                fileNameFullPath = os.path.join(root, file)
                listOfFilesFound.append(fileNameFullPath)
                break

    # Check if the file name is found and only occurs once
    listOfFilesFoundCount = len(listOfFilesFound)
    if listOfFilesFoundCount != 1:
        raise Exception(fileName + " occurs "+str(listOfFilesFoundCount)+" times  in the directory: "+ directoryFullPath)

    # Return full path of the file name
    return str( listOfFilesFound[0] )

# Run entire file or script
def run_fileName(fileName):
    fileNameFullPath = get_fullPath_of_fileName(fileName)
    exec( open(fileNameFullPath).read() )