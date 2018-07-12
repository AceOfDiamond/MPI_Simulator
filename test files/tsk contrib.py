inputFile = open("CFile/test.c")
Idname = "world_rank"
n = 3
for line in inputFile:
    L = line.replace(" ", "")
    if L.find("if(" + Idname) != -1:
        break

for id in range(n):
    M1 = open("Txt Files/FileId0.txt", "r")
    M2 = open("Txt Files/FileOthermachine.txt", "r")
    Mx = open("text File/FileId" + str(id) + ".txt", "w")
    if L.find("if(" + Idname + "==") != -1:
        Line = L.split("==")
        idd = Line[1][0]
        if id == int(idd):
            for i in M1:
                Mx.write(i)
        else:
            for i in M2:
                Mx.write(i)
    if L.find("if(" + Idname + ">") != -1:
        Line = L.split(">")
        idd = Line[1][0]
        if id > int(idd):
            for i in M1:
                Mx.write(i)
        else:
            for i in M2:
                Mx.write(i)
    if L.find("if(" + Idname + "<") != -1:
        Line = L.split("<")
        idd = Line[1][0]
        if id < int(idd):
            for i in M1:
                Mx.write(i)
        else:
            for i in M2:
                Mx.write(i)