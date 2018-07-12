
bw = open("InputFiles/BandwidthFile.txt", "r")
id = 0
code = open("Txt Files/FileId"+str(id)+".txt", "r")
op = open("Machine/"+str(id)+"OPfile.txt", "r")
task = open("task"+str(id)+".txt", "w")

while code:
    line = code.readline()
    if line == '':
        break
    Line = line.strip().split(', ')
    if Line[0].find("MPI") != -1:
        mach = Line[3]
        print (mach)
        while bw:
            band = bw.readline()
            if band == '':
                break
            comm = str(id) + " " + mach
            if band.find(comm) != 1:
                task.write(comm+"\n")
                print ("writing communication into task file ...")
                break
    if Line[0].find("OP") != -1:
        op = open("Machine/0OPfile.txt", "r")
        while op:
            oper = op.readline().strip()
            #if oper == '':
            #    break
            Oper = line.strip().split("(")
            comm = str(id) + " " + Oper[0]
            if oper.find(comm) != 1:
                task.write(comm+"\n")
                print("writing operation into task file ...")
                break
        op.close()