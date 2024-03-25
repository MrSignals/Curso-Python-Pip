import matplotlib.pyplot as plt
import read_csv
import utils as u

def generate_bar_chart(name, labels,values):
  fig, ax = plt.subplots()
  plt.ticklabel_format(style = 'plain')
  ax.bar(labels, values)
  plt.savefig(f'imgs/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

data = read_csv.read_csv('data.csv')



if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100,200,300]
  generate_bar_chart(labels, values)
  #generate_pie_chart(labels,values)
  