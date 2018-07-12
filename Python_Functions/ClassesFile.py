class Machine:
    DiagramTab = []
    ts = 0
    te = 0
    t_time = 0
    mach_comm = ''

    def __init__(self, x, y):
        self.ID = x
        self.task_file = y

    def get_id(self):
        return self.ID

    def set_ts(self, ts):
        self.ts = ts

    def set_te(self, te):
        self.te = te

    def set_t_time(self, t):
        self.t_time = t

    def set_mach_comm(self, mach):
        self.mach_comm = mach

    def get_ts(self):
        return self.ts

    def get_te(self):
        return self.te

    def get_t_time(self):
        return self.t_time

    def get_mach_comm(self):
        return self.mach_comm

    def set_Diag (self, couple):
        self.DiagramTab.append(couple)