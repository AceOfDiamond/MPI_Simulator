import plotly.plotly as py
import plotly.figure_factory as ff
import plotly
df = []
gntt = open("../gantt.txt", "r")
for line in gntt:
      Line = line.strip().split(' ')
      if len(Line[1]) == 4:
            start = '' + Line[1]
      if len(Line[1]) == 3:
            start = '0' + Line[1]
      if len(Line[1]) == 2:
            start = '00' + Line[1]
      if len(Line[1]) == 1:
            start = '000' + Line[1]
      if len(Line[2]) == 4:
            end = '' + Line[2]
      if len(Line[2]) == 3:
            end = '0' + Line[2]
      if len(Line[2]) == 2:
            end = '00' + Line[2]
      if len(Line[2]) == 1:
            end = '000' + Line[2]

      df.append(dict(Task=Line[0], Start= start + '-01-01', Finish= end + '-01-01', Resource=Line[3]))

for i in df:
    print(i)

colors = {'communicate': 'rgb(0, 105, 185)',
          'compute': 'rgb(255, 145, 0)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
py.plot(fig, filename='gantt-group-tasks-together', world_readable=True)