import sys,os
from pathlib import Path
def getListOfFiles(dirName):
    # https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    listOfFile = [f for f in listOfFile if not f[0] == '.']
    
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles    
def write_to_file(content):
    f = open("raw_key_words.txt", "a")
    f.write(content)
    f.close()


dirName = "/media/chow/907256CD7256B7A4/Mozzila"
target_path = "/home/chow/Projects/Thesis/File_names/"
listOfFiles = getListOfFiles(dirName)
listOfFiles = [f for f in listOfFiles if not f[0] == '.']
list_of_all_files = []
for elem in listOfFiles:
    list_of_all_files.append(elem)

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    if "test" in dirpath:
        continue
    else:
        filenames = [f for f in filenames if not f[0] == '.']
        dirnames[:] = [d for d in dirnames if not d[0] == '.']
        
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    

for elem in listOfFiles:
    list_of_all_files.append(elem)
list_of_all_files = [f for f in list_of_all_files if f.find("test")==-1]
num_per_file = len(list_of_all_files)/12 + 1
i = 0
j = 0
file_name = "file_to_process_" + str(j)
file_path = Path(target_path+file_name)
f = open(file_path, "a")
for ele in list_of_all_files:

    if i < num_per_file :
        f.write(ele + "\n")
        i = i + 1
    else:
        f.close()
        i = 0
        j = j + 1
        file_name = "file_to_process_" + str(j)
        file_path = Path(target_path+file_name)
        f = open(file_path, "a")

