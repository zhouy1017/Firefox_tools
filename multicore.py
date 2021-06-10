import multiprocessing as mp
import psutil
from pathlib import Path

def spawn():
    procs = list()
    n_cpus = psutil.cpu_count()
    for cpu in range(n_cpus):
        file_name = "file_to_process_" + str(cpu)
        d = dict(file_name=file_name)
        p = mp.Process(target=process_file, kwargs=d)
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
        print('joined')
## Only collect clang python rust and js 
def process_file(file_name):
    target_path = "/home/chow/Projects/Thesis/File_names/"
    file_path = Path(target_path + file_name)
    result_path = "/home/chow/Projects/Thesis/File_Process/"
    f = open(file_path, "r")
    f4 = open(Path(result_path+file_name+"_result"+"_modules"),"w")
    while True:
        line = f.readline()
        line = line.strip('\n')
        file_types = ["c","h","cpp","hpp","rs","py","js"]
        if not line:
            break
        f2=open(line,"r")
        print("Processing: "+line.removeprefix("/media/chow/907256CD7256B7A4/Mozzila/"))
        if "." not in line:
            continue
        else:
            line_words = line.split(".")
            extension = line_words[-1].lower()
            if extension not in file_types:
                continue
        file_process_path = Path(result_path + file_name+"_result_"+extension)
        f3 = open(file_process_path,"a")
        save = False
        count = 0
        while True:
            try:
                line2 = f2.readline()
                line2 = line2.strip('\n')
            except:
                break
            if not line2:
                count = count + 1
                if (count > 10):
                    break
                else:
                    continue
            else:
                count = 0
            line2 = line2.lower()
            if save:
                f3.write(line2+"\n")
            else:
                if "copyright" in line2:
                    f3.write(line+"\n")
                    save = True
                    f3.write(line2+"\n")
                    f4.write(line.removeprefix("/media/chow/907256CD7256B7A4/Mozzila/")+"\n")

        f3.close()



    f.close()
    f4.close()



if __name__ == '__main__':
    spawn()