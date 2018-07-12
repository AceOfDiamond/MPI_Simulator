from Python_Functions import Functions as func

#import plotly.plotly as py
#import plotly.figure_factory as ff
#import plotly

def Plot_Gantt (tab):
    pass
def main(nbMach):
    """"""
    """ reset the file each execution """

    for i in range(nbMach):
        open("Txt Files/FileIf.txt", "w").close()
        open("Txt Files/FileOthermachine.txt", "w").close()
        open("Machine/task" + str(i) + ".txt", "w").close()
    """ end """

    CFile = open("CFile/test.c")
    Idname = func.meId(CFile, "MPI_Comm_rank")
    func.Compute_time(nbMach)
    func.CodeBlock2(Idname)
    func.tsk_contrib(nbMach, Idname)
    func.CodetoTask(nbMach)
    func.diagram()
    tab = func.diagram()
    for i in tab:
        print (i)
    #Plot_Gantt(tab)
if __name__ == '__main__':
    main(3)