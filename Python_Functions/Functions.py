from Python_Functions import ClassesFile as ClFile


def meId (file, command):
    """     return the id of the machine master  """
    block = []
    temp = ''
    for line in file:
        temp = line.upper()
        Comm = command.upper()
        if temp.find(Comm) != -1:
            block = (line.split(','))
            pass
    comm = block[1].strip()
    self = comm[1:-2]
    file.close()
    return self


def CommunicationMachine(comm):
    """     return the id of the machine in communication   """
    fr = open("txt","r")
    line = fr.readline()
    tt= []
    while True:
        if line.strip() == '':
            break
        else:
            command = comm.upper()
            temp = line.upper()
            if temp.find(command) != -1:
                tt = line.split(', ')
                break
            else:
                line = fr.readline()
    receiver_machine = tt[4]
    return receiver_machine


def Compute_time (nbmach):
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
                        op.write(str(i) + " " + CLine[1] + " " + CLine[2] + "\n")
        op.close()


def CodeBlock2(Idname):
    inputFile = open("CFile/test.c")
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
                        outputFile = open("Txt Files/FileIf.txt", "a")
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
                outputFile = open("Txt Files/FileOthermachine.txt", "a")
                outputFile.write(line)
                line = inputFile.readline()
                if '}' in line or '}' in line:
                    accClose += 1
                if '{' in line or '{' in line:
                    accOpen += 1
            outputFile.write(line)
            outputFile.close()
    inputFile.close()


def CodeBlock(Idname):
    """     return the id of the machine master  (Code Devider)"""
    inputFile = open("CFile/test.c")
    accOpen = 0
    accClose = 0
    tab = []

    for line in inputFile:
        L = line.replace(" ", "")
        accClose = 0
        accOpen = 0
        if L.find("if("+Idname+"==") != -1:
            index = L.index("==")
            index2 = L.index(")")
            j = L[index + 2:index2]
            tab.append(j)
            accOpen += 1
            while accOpen - accClose != 0:
                if L.find("if("+Idname+"==" + j + ")") != -1:
                    line = inputFile.readline()
                    while accOpen - accClose != 0:
                        outputFile = open("Txt Files/FileId" + j + ".txt", "a")
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
                outputFile = open("Txt Files/FileOthermachine.txt", "a")
                outputFile.write(line)
                line = inputFile.readline()
                if '}' in line or '}' in line:
                    accClose += 1
                if '{' in line or '{' in line:
                    accOpen += 1
            outputFile.write(line)
            outputFile.close()
    inputFile.close()

"""def compte_time_distributer ():

    Cfile = open("InputFiles/ClusterFile.txt", "r")
    Mfile = open("InputFiles/MachineFile.txt", "r")
    OpFile = open("Machine/OperationFile.txt", "w")

    for Cline in Cfile:
        line = Cline.strip()
        t1 = line.split(' ')
        Cl = t1[0]
        OP = t1[1]
        Time = t1[2]
        MCfile = open("InputFiles/MachClusFile.txt", "r")
        for MCline in MCfile:
            if Cl in MCline:
                line = MCline.strip()
                t2 = line.split(' ')
                Pline = t2[0] + " " + OP + " " + Time + "\n"
                OpFile.write(Pline)
        MCfile.close()
    OpFile.close()
    Cfile.close()
    Mfile.close()
    
    ################
    ################
    ################
    
    Mfile = open("InputFiles/MachineFile.txt", "r")

    for Mline in Mfile:
        line = Mline.strip()
        MachFile = open("Machine/" + line + "OPfile.txt", "w")
        OpFile = open("Machine/OperationFile.txt", "r")
        for Opline in OpFile:
            if Opline.find(line) != -1:
                MachFile.write(Opline)
        OpFile.close()
        MachFile.close()
"""


#def tsk_distribute(n):

#    for id in range(1, n):
#        M1 = open("Txt Files/FileOthermachine.txt", "r")
#        Mx = open("Txt Files/FileId" + str(id) + ".txt", "w")

#        for line in M1:
#            Mx.write(line)


def tsk_contrib (n, Idname):
    inputFile = open("CFile/test.c")

    for line in inputFile:
        L = line.replace(" ", "")
        if L.find("if(" + Idname) != -1:
            break

    for id in range(n):
        M1 = open("Txt Files/FileIf.txt", "r")
        M2 = open("Txt Files/FileOthermachine.txt", "r")
        Mx = open("text Files/FileId" + str(id) + ".txt", "w")
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


def CodetoTask(nbmach):
    def C2T(id):
        task = open("Machine/task" + str(id) + ".txt", "w")
        code = open("text Files/FileId" + str(id) + ".txt", "r")

        while code:
            line = code.readline()
            if line == '':  # EOF
                break
            Linecomp = line.strip().replace(' ', '').split('(')
            Linecomm = line.strip().replace(' ', '').split(',')
            bw = open("InputFiles\BandwidthFile.txt", "r")
            for c in bw:
                C = c.strip().split(' ')
                try:
                    if c.find(str(id) + " " + Linecomm[3]) != -1:
                        task.write(Linecomp[0] + " " + Linecomm[3] + " " + C[2] + "\n")
                except IndexError:
                    pass
            bw.close()

            op = open("Machine/" + str(id) + "OPfile.txt", "r")
            for i in op:
                I = i.strip().split(' ')
                try:
                    if Linecomp[0].find(I[1]) != -1:
                        task.write(I[1] + " " + str(id) + " " + I[2] + "\n")
                except IndexError:
                    pass
            op.close()

    for i in range(nbmach):
        C2T(i)


def diagram():

    f0 = open("Machine/task0.txt", "r")
    f1 = open("Machine/task1.txt", "r")
    f2 = open("Machine/task2.txt", "r")
    m0 = ClFile.Machine(0, f0)
    m1 = ClFile.Machine(1, f1)
    m2 = ClFile.Machine(2, f2)

    gantt = []
    t0 = t0s = t0e = t1 = t1e = t1s = t2 = t2e = t2s = 0
    op0 = ""
    op1 = ""
    op2 = ""
    line0 = f0.readline().strip()
    line1 = f1.readline().strip()
    line2 = f2.readline().strip()

    while 1:

        if line0 == '' and line1 == '' and line2 == '':
            break

        try:
            Tab0 = line0.split(' ')
            Tab1 = line1.split(' ')
            Tab2 = line2.split(' ')
            m0.set_mach_comm(int(Tab0[1]))
            m1.set_mach_comm(int(Tab1[1]))
            m2.set_mach_comm(int(Tab2[1]))
        except IndexError:
            pass
        try:
            # if 0 compute
            if Tab0[1].find("0") != -1:
                op0 = "compute"
                m1.set_mach_comm(m1.get_id())
                t0 = t0e
                t0s = t0
                t0e = t0s + int(Tab0[2])
                line0 = f0.readline().strip()
            # if 0 communicate
            elif Tab0[1].find("0") == -1:
                # if 0 communicate with 1
                if m0.get_id() == m1.get_mach_comm():
                    #op0 = "communicate with 1"
                    op0 = "communicate"
                    m0.set_mach_comm(m1.get_id())
                    t0 = max(m0.get_te(), m1.get_te())
                    t0s = t0
                    t0e = t0s + int(Tab0[2])
                    line0 = f0.readline().strip()
                # if 0 communicate with 2
                elif m0.get_id() == m2.get_mach_comm():
                    #op0 = "communicate with 2"
                    op0 = "communicate"
                    m0.set_mach_comm(m2.get_id())
                    t0 = max(m0.get_te(),m2.get_te())
                    t0s = t0
                    t0e = t0s + int(Tab0[2])
                    line0 = f0.readline().strip()
        except IndexError:
            pass
        try:
            # if 1 compute
            if Tab1[1].find("1") != -1:
                op1 = "compute"
                m1.set_mach_comm(m1.get_id())
                t1 = t1e
                t1s = t1
                t1e = t1s + int(Tab1[2])
                line1 = f1.readline().strip()
            # if 1 communicate
            elif Tab1[1].find("1") == -1:
                # if 1 communicate with 0
                if m1.get_id() == m0.get_mach_comm():
                    #op1 = "communicate with 0"
                    op1 = "communicate"
                    m1.set_mach_comm(m0.get_id())
                    t1 = max(m0.get_te(), m1.get_te())
                    t1s = t1
                    t1e = t1s + int(Tab1[2])
                    line1 = f1.readline().strip()
                # if 1 communicate with 2
                elif m1.get_id() == m2.get_mach_comm():
                    #op1 = "communicate with 2"
                    op1 = "communicate"
                    m1.set_mach_comm(m2.get_id())
                    t1 = max(m1.get_te(), m2.get_te())
                    t1s = t1
                    t1e = t1s + int(Tab1[2])
                    line1 = f1.readline().strip()
        except IndexError:
            pass
        try:
            # if 2 compute
            if Tab2[1].find("2") != -1:
                op2 = "compute"
                m2.set_mach_comm(m2.get_id())
                t2 = t2e
                t2s = t2
                t2e = t2s + int(Tab2[2])
                line2 = f2.readline().strip()
            # if 2 communicate
            elif Tab2[1].find("2") == -1:
                # if 2 communicate with 1
                if m2.get_id() == m0.get_mach_comm():
                    #op2 = "communicate with 0"
                    op2 = "communicate"
                    m2.set_mach_comm(m0.get_id())
                    t2 = max(m2.get_te(), m0.get_te())
                    t2s = t2
                    t2e = t2s + int(Tab2[2])
                    line2 = f2.readline().strip()
                # if 2 communicate with 2
                elif m2.get_id() == m1.get_mach_comm():
                    #op2 = "communicate with 1"
                    op2 = "communicate"
                    m2.set_mach_comm(m1.get_id())
                    t2 = max(m2.get_te(), m1.get_te())
                    t2s = t2
                    t2e = t2s + int(Tab2[2])
                    line2 = f2.readline().strip()
        except IndexError:
            pass

        m0.set_t_time(t0)
        m0.set_ts(t0s)
        m0.set_te(t0e)
        gantt.append(dict(Operation=op0, start=str(t0s), end=str(t0e)))
        m0.set_Diag("machineA " + str(t0s) + " " + str(t0e) + " " + op0 + "\n")
        m1.set_t_time(t1)
        m1.set_ts(t1s)
        m1.set_te(t1e)
        gantt.append(dict(Operation=op1, start=str(t1s), end=str(t1e)))
        m1.set_Diag("machineB " + str(t1s) + " " + str(t1e) + " " + op1 + "\n")
        m2.set_t_time(t2)
        m2.set_ts(t2s)
        m2.set_te(t2e)
        gantt.append(dict(Operation=op2, start=str(t2s), end=str(t2e)))
        m2.set_Diag("machineC " + str(t2s) + " " + str(t2e) + " " + op2 + "\n")

        #print ("::::::::::::::::::::")
        #print ("machine 0: " + op0 + " from " + str(t0s) + " ===> " + str(t0e))
        #print("machine 1: " + op1 + " from " + str(t1s) + " ===> " + str(t1e))
        #print("machine 2: " + op2 + " from " + str(t2s) + " ===> " + str(t2e))
    gntt = open("gantt.txt", "w")
    for line in m0.DiagramTab:
        gntt.write(line)

    """ end Gantt diagram """
    return gantt