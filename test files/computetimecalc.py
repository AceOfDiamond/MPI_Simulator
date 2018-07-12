from Python_Functions import ClassesFile as ClFile

f0 = open("Machine/Machine0", "r")
f1 = open("Machine/Machine1", "r")
f2 = open("Machine/Machine2", "r")
#f0 = open("task0.txt", "r")
#f1 = open("task1.txt", "r")
#f2 = open("task2.txt", "r")

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
                op0 = "communicate with 1"
                m0.set_mach_comm(m1.get_id())
                t0 = max(m0.get_te(), m1.get_te())
                t0s = t0
                t0e = t0s + int(Tab0[2])
                line0 = f0.readline().strip()
            # if 0 communicate with 2
            elif m0.get_id() == m2.get_mach_comm():
                op0 = "communicate with 2"
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
            op1 = "compte"
            m1.set_mach_comm(m1.get_id())
            t1 = t1e
            t1s = t1
            t1e = t1s + int(Tab1[2])
            line1 = f1.readline().strip()
        # if 1 communicate
        elif Tab1[1].find("1") == -1:
            # if 1 communicate with 0
            if m1.get_id() == m0.get_mach_comm():
                op1 = "communicate with 0"
                m1.set_mach_comm(m0.get_id())
                t1 = max(m0.get_te(), m1.get_te())
                t1s = t1
                t1e = t1s + int(Tab1[2])
                line1 = f1.readline().strip()
            # if 1 communicate with 2
            elif m1.get_id() == m2.get_mach_comm():
                op1 = "communicate with 2"
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
            op2 = "compte"
            m2.set_mach_comm(m2.get_id())
            t2 = t2e
            t2s = t2
            t2e = t2s + int(Tab2[2])
            line2 = f2.readline().strip()
        # if 2 communicate
        elif Tab2[1].find("2") == -1:
            # if 2 communicate with 1
            if m2.get_id() == m0.get_mach_comm():
                op2 = "communicate with 0"
                m2.set_mach_comm(m0.get_id())
                t2 = max(m2.get_te(), m0.get_te())
                t2s = t2
                t2e = t2s + int(Tab2[2])
                line2 = f2.readline().strip()
            # if 2 communicate with 2
            elif m2.get_id() == m1.get_mach_comm():
                op2 = "communicate with 1"
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
    gantt.append(dict(Operation='op', start=str(t0s), end=str(t0e)))
    m0.set_Diag("A work from : " + str(t0s) + " to " + str(t0e))
    m1.set_t_time(t1)
    m1.set_ts(t1s)
    m1.set_te(t1e)
    gantt.append(dict(Operation='op', start=str(t1s), end=str(t1e)))
    m1.set_Diag("B work from : " + str(t1s) + " to " + str(t1e))
    m2.set_t_time(t2)
    m2.set_ts(t2s)
    m2.set_te(t2e)
    gantt.append(dict(Operation='op', start=str(t2s), end=str(t2e)))
    m2.set_Diag("C work from : " + str(t2s) + " to " + str(t2e) + "\n////////////")

    #print ("::::::::::::::::::::")
    #print ("machine 0: " + op0 + " from " + str(t0s) + " ===> " + str(t0e))
    #print("machine 1: " + op1 + " from " + str(t1s) + " ===> " + str(t1e))
    #print("machine 2: " + op2 + " from " + str(t2s) + " ===> " + str(t2e))

for line in m0.DiagramTab:
    print(line)