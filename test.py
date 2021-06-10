def process_file(file_name):
    f = open(file_name, "r")
    f3 = open(file_name+"_result","a")
    while True:
        line = f.readline()
        line = line.strip('\n')
        if not line:
            break
        f2=open(line,"r")
        print("Processing: "+line.removeprefix("/media/chow/907256CD7256B7A4/Mozzila/"))
        save = False
        count = 0
        while True:
            line2 = f2.readline()
            line2 = line2.strip('\n')
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


    f.close()
    f3.close()

process_file("test")