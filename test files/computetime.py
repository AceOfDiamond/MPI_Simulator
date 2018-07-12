nbmach = 3

for i in range(nbmach):
    Clfile = open("InputFiles/ClusterFile.txt", "r")
    MachClFile = open("InputFiles/MachClusFile.txt", "r")
    op = open("Machine/" + str(i) + "OPfile.txt", "w")
    while MachClFile:
        MCline = MachClFile.readline()
        if MCline == '':
            break
        MCLine = MCline.strip().split(' ')
        if MCLine[0].find(str(i)) != -1:
            while Clfile:
                Cline = Clfile.readline()
                if Cline == '':
                    break
                CLine = Cline.strip().split(' ')
                if MCLine[1].find(CLine[0]) != -1:
                    print (str(i) + " " + CLine[1] + " " + CLine[2] + "\n")
                    op.write(str(i) + " " + CLine[1] + " " + CLine[2] + "\n")
    op.close()