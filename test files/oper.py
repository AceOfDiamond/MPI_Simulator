def C2T(id):
    task = open("task" + str(id) + ".txt", "w")
    code = open("Txt Files/FileId" + str(id) + ".txt", "r")

    while code:
        line = code.readline()
        if line == '':  # EOF
            break
        Linecomp = line.strip().replace(' ', '').split('(')
        Linecomm = line.strip().replace(' ', '').split(',')
        bw = open("InputFiles\BandwidthFile.txt", "r")
        for c in bw:
            C = c.strip().split(' ')
            print(C)
            try:
                if c.find(str(id) + " " + Linecomm[3]) != -1:
                    task.write(Linecomp[0] + " " + Linecomm[3] + " " + C[2] + "\n")
            except IndexError:
                pass
        bw.close()

        op = open("Machine/" + str(id) + "OPfile.txt", "r")
        for i in op:
            I = i.strip().split(' ')
            print(I)
            try:
                if Linecomp[0].find(I[1]) != -1:
                    task.write(I[1] + " " + str(id) + " " + I[2] + "\n")
            except IndexError:
                pass
        op.close()

for i in range (3):
    C2T(i)