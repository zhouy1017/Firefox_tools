import shutil
from pathlib import Path

file_types = ["c","h","cpp","hpp","rs","py","js","modules"]
for extension in file_types:
    i = 0
    des_filename = "process_result_"+extension
    result_path = "/home/chow/Projects/Thesis/Results_by_Lang/"
    des_path = Path(result_path+des_filename)
    des_file = open(des_path,"wb")
    while i < 12:
        try:
            source_filename = "file_to_process_" + str(i) + "_result_"+extension
            source_path = "/home/chow/Projects/Thesis/File_Process/"
            source_full_path = Path(source_path+source_filename)
            source_file = open(source_full_path,"rb")
            shutil.copyfileobj(source_file,des_file)
            source_file.close()
            i = i + 1
        except:
            i = i + 1
            continue
    des_file.close()
     
