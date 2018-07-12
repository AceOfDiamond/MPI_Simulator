n = 3
M0 = open("../Txt Files/FileId0.txt", "r")

for id in range(1,n):
    M1 = open("../Txt Files/FileOthermachine.txt", "r")
    print ("hello")
    Mx = open("../Txt Files/FileId"+ str(id) +".txt", "w")
    for line in M1:
        Mx.write(line)


for id in range(n):
    print ("bello")
    Mx = open("../Txt Files/FileId" + str(id) + ".txt", "r")
    print("==============")
    print ("file id ",id," :\n")
    print("==============")
    for line in Mx:
        print (line)
    Mx.close()
    print("==============")
