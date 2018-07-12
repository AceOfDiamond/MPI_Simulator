"""     return the id of the machine master  (Code Devider)"""
Idname = "world_rank"
inputFile = open("../CFile/test.c")
accOpen = 0
accClose = 0
tab = []

for line in inputFile:
    L = line.replace(" ", "")
    accClose = 0
    accOpen = 0
    if L.find("if") != -1:
        accOpen += 1
        while accOpen - accClose != 0:
            if L.find("if") != -1:
                line = inputFile.readline()
                while accOpen - accClose != 0:
                    outputFile = open("../Txt Files/FileIf.txt", "a")
                    outputFile.write(line)
                    line = inputFile.readline()
                    if '}' in line:
                        accClose += 1
                    if '{' in line:
                        accOpen += 1
                outputFile.write(line)
                outputFile.close()
    if L.find("else") != -1:
        line = inputFile.readline()
        accOpen += 1
        while accOpen - accClose != 0:
            outputFile = open("../Txt Files/FileOthermachine.txt", "a")
            outputFile.write(line)
            line = inputFile.readline()
            if '}' in line or '}' in line:
                accClose += 1
            if '{' in line or '{' in line:
                accOpen += 1
        outputFile.write(line)
        outputFile.close()
inputFile.close()
for k in tab:
    Test = open("../Files/Fileid" + k + ".txt", "r")
    print ("=========================")
    print ("====== File ID" + k + " =========")
    print ("=========================")
    for ligne in Test:
        print (ligne)