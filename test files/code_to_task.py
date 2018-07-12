def C2T(id):

    bw = open("InputFiles/BandwidthFile.txt", "r")
    code = open("Txt Files/FileId" + str(id) + ".txt", "r")
    op = open("Machine/" + str(id) + "OPfile.txt", "r")
    task = open("task" + str(id) + ".txt", "w")

    while code:
        line = code.readline()
        if line == '':
            break
        Line = line.strip().split(', ')
        if Line[0].find("MPI") != -1:
            mach = Line[3]
            while bw:
                band = bw.readline()
                if band == '':
                    break
                comm = str(id) + " " + mach
                if band.find(comm) != 1:
                    task.write(band)
                    break
        if Line[0].find("OP") != -1:
            op = open("Machine/0OPfile.txt", "r")
            while op:
                opera = op.readline()
                oper = opera.strip()
                # if oper == '':
                #    break
                Oper = line.strip().split("(")
                comm = str(id) + " " + Oper[0]
                if oper.find(comm) != 1:
                    task.write(opera)
                    break
            op.close()

for i in range (3):
    C2T(i)