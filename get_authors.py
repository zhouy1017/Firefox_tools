import nltk
from pathlib import Path

file_types = ["c","h","cpp","hpp","rs","py","js"]
for extension in file_types:
    des_filename = "process_result_"+extension
    result_path = "/home/chow/Projects/Thesis/Results_by_Lang/"
    des_path = Path(result_path+des_filename)
    des_file = open(des_path,"rb")
    
    des_file.close()
