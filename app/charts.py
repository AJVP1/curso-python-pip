import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  # colocamos dos variables, figura y coordenadas
  fig, ax = plt.subplots()
  
  # decimos que vamos a hacer grafica de barras
  ax.bar(labels, values)
  
  # mostramos la grafica
  plt.show()

def generate_pie_chart(labels, values):  
  # colocamos dos variables, figura y coordenadas
  fig, ax = plt.subplots()
  
  # decimos que vamos a hacer grafica de torta
  ax.pie(values, labels=labels)

  # decimos que vaya en el medio 
  ax.axis('equal')
  
  # mostramos la grafica
  plt.show()
  

if __name__ == '__main__':
  #generate_bar_chart()
  generate_pie_chart()
  