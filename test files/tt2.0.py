from Python_Functions import ClassesFile as Clfile

t_f = []    # array of opened task file
t_m = []    # array of Created Machine
t_t = []    # array of global clock of machine
t_ts = []   # array of Start time task file of machine
t_te = []   # array of End time task file of machine
t_l = []    # array of Line read form task file of machine
n = 2


def function(ListMachine):
    T = []
    List = ListMachine
    for i in List:
        T.append(List[i].get_te())
    return T


def operation (index):
    line = t_l[index]
    t_m[i].set_mach_comm(line[1])
    t_t[index] = t_te[index]
    t_ts[index] = t_t[index]
    t_te[index] = t_ts[index] + int(line[2])


def communication(index, line):
    line = line.split(' ')
    t_m[index].set_mach_comm(line[1])
    t_t[index] = max(t_te)
    t_ts[index] = t_t[index]
    t_te[index] = t_ts[index] + int(line[2])




for i in range(n):
    f = open("../Machine" + str(i), 'r')
    t_f.append(f)                           # append file to table of file
    t_m.append(Clfile.Machine(i, t_f[i]))   # create machine using the file
    t_t.append(0)                           # initialize the global clock
    t_ts.append(0)                          # initialize the Start Clock
    t_te.append(0)                          # initialize the End Clock

while 1:

    for i in range(n):
        t_l.append(t_m[i].task_file.readline().strip())
        if t_l[i] == '':
            break
        line = t_l[i].split(' ')
        t_m[i].set_mach_comm(line[1])

    for i in range (n):
        if t_l[i][1].find(str(i)) != -1:
            operation(i)
        elif t_l[i][1].find(str(i)) == -1:
            communication(i, t_l[i])

    for i in range(n):
        t_m[i].set_t_time(t_t[i])
        t_m[i].set_ts(t_ts[i])
        t_m[i].set_te(t_te[i])
        t_m[i].set_Diag(str(i) + " work from : " + str(t_ts[i]) + " to " + str(t_te[i]))
    t_l = []