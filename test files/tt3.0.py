from Python_Functions import ClassesFile as Clfile

FA = open("../Machine/Machine0", 'r')
FB = open("../Machine/Machine1", 'r')
FC = open("../Machine/Machine2", 'r')
m0 = Clfile.Machine(0, FA)
m1 = Clfile.Machine(1, FB)
m2 = Clfile.Machine(2, FC)
ta = tas = tae = tb = tbe = tbs = tc = tce = tcs = 0
gantt = []

while 1:
    lineA = FA.readline().strip()
    lineB = FB.readline().strip()
    lineC = FC.readline().strip()
    if (lineA == '') and (lineB == '') and (lineC == ''):
        break
    try:
        LineA = lineA.split(' ')
        LineB = lineB.split(' ')
        LineC = lineC.split(' ')
        m0.set_mach_comm(LineA[1])
        m1.set_mach_comm(LineB[1])
        m2.set_mach_comm(LineC[1])
    except IndexError as e:
        pass
        continue

    if LineA[1].find("0") != -1:
        m0.set_mach_comm(LineA[1])
        ta = tae
        tas = ta
        tae = tas + int(LineA[2])
    elif LineA[1].find("0") == -1:
        if LineA[1].find(m1.get_mach_comm()) == -1 :
            m0.set_mach_comm(lineA[1])
            ta = max (m0.get_te(), m1.get_te())
            tas = ta
            tae = tas + int(LineA[2])
        elif LineA[1].find(m2.get_mach_comm()) == -1 :
            m0.set_mach_comm(lineA[1])
            ta = max (m0.get_te(), m2.get_te())
            tas = ta
            tae = tas + int(LineA[2])

    if LineB[1].find("1") != -1:
        m1.set_mach_comm(LineB[1])
        tb = tbe
        tbs = tb
        tbe = tbs + int(LineB[2])
    elif LineB[1].find("1") == -1:
        if LineB[1].find(m0.get_mach_comm()) == -1 :
            m1.set_mach_comm(LineB[1])
            tb = max (m0.get_te(), m1.get_te())
            tbs = tb
            tbe = tbs + int(LineB[2])
        elif LineB[1].find(m2.get_mach_comm()) == -1 :
            m1.set_mach_comm(LineB[1])
            tb = max (m0.get_te(), m2.get_te())
            tbs = tb
            tbe = tbs + int(LineB[2])

    if LineC[1].find("2") != -1:
        m2.set_mach_comm(LineC[1])
        tc = tce
        tcs = tc
        tce = tcs + int(LineC[2])
    elif LineC[1].find("2") == -1:
        if LineC[1].find(m0.get_mach_comm()) == -1 :
            m2.set_mach_comm(LineC[1])
            tc = max (m2.get_te(), m0.get_te())
            tcs = tc
            tce = tcs + int(LineC[2])
        elif LineC[1].find(m1.get_mach_comm()) == -1 :
            m2.set_mach_comm(LineC[1])
            tc = max (m2.get_te(), m1.get_te())
            tcs = tc
            tce = tcs + int(LineC[2])

    m0.set_t_time(ta)
    m0.set_ts(tas)
    m0.set_te(tae)
    gantt.append(dict(Operation='op', start=str(tas), end=str(tae)))
    m0.set_Diag("A work from : " + str(tas) + " to " + str(tae))
    m1.set_t_time(tb)
    m1.set_ts(tbs)
    m1.set_te(tbe)
    gantt.append(dict(Operation='op', start=str(tbs), end=str(tbe)))
    m1.set_Diag("B work from : " + str(tbs) + " to " + str(tbe))
    m2.set_t_time(tc)
    m2.set_ts(tcs)
    m2.set_te(tce)
    gantt.append(dict(Operation='op', start=str(tcs), end=str(tce)))
    m2.set_Diag("C work from : " + str(tcs) + " to " + str(tce))

"""
for i in m0.DiagramTab:
    print(i)

"""
for line in gantt:
    print (line)
