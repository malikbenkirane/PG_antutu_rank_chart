import sys
import json

def parse_and_reverse_chart_data(chart_data_file):
  chart_data = json.load(chart_data_file)
  rev_index = {}
  for lineno, line_dict in enumerate(chart_data):
    for k,v in line_dict.items():
      if k <> 'model':
        v = int(v)
      if k in rev_index:
        rev_index[k].append(v)
      else:
        rev_index[k] = [v]
  return rev_index

if __name__ == '__main__':
  if len(sys.argv) == 2:
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    with open(sys.argv[1]) as chart_data_file:
      # generates plot data 
      rev_index = parse_and_reverse_chart_data(chart_data_file)
      n = len(rev_index['model'])

      def ticker(value, pos):
        models = rev_index['model']
        if value > -1 and value < n:
          return models[int(value)]
        else: return value

      t_formatter = FuncFormatter(ticker)
      
      # set up plot
      fig = plt.figure(figsize=(24,23))
      ax = fig.add_subplot(111)
      grid = range(n)
      plot = []

      fields = ['cpu_rate', '3d_rate', 'ux_rate', 'total_rate'] 
      colors = {
            'cpu_rate': 'red',
            '3d_rate': 'yellow',
            'ux_rate': 'black',
            'total_rate': 'blue'
            }
      
      # plots data
      for field in fields:
        plot.append(ax.scatter(
          rev_index[field], grid, label=field, color=colors[field]
          ))
      ax.yaxis.set_ticks(range(n))
      ax.yaxis.set_major_formatter(t_formatter)
      ax.legend()

      # shows plot
      plt.savefig('%s.png' % sys.argv[1])
