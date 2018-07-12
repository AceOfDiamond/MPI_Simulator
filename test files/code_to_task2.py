def C2T(id):

    bw = open("InputFiles/BandwidthFile.txt", "r")
    code = open("Txt Files/FileId" + str(id) + ".txt", "r")
    op = open("Machine/" + str(id) + "OPfile.txt", "r")
    task = open("task" + str(id) + ".txt", "w")

    while code:
        line = code.readline()
        if line == '': #EOF
            break

        Line = line.strip().split(', ')
        L = line.strip().split('(')
        if Line[0].find("MPI") != -1:
            mach = Line[3]
            while bw:
                band = bw.readline()
                Bw = band.strip().split(" ")
                if band == '': #EOF
                    break

                comm = str(id) + " " + mach
                if band.find(comm) != 1:
                    task.write(L[0] + " " + mach + " " + Bw[2] +"\n")
                    break
        op = open("Machine/" + str(id) + "OPfile.txt", "r")
        if Line[0].find("OP") != -1:
            for i in op:
                opera = i
                oper = opera.strip()
                Op = oper.split(" ")
                if oper == '': #EOF
                    break

                Oper = line.strip().split("(")
                comm = str(id) + " " + Oper[0]
                if oper.find(comm) != 1:
                    task.write(Oper[0] + " " + str(id) + " " + Op[2] +"\n")
                    break
        op.close()

for i in range (3):
    C2T(i)