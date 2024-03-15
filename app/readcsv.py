import csv

def read_csv(path):
  with open(path, 'r') as cvsfile:
    # lee el archivo csv delimitado por comas
    reader = csv.reader(cvsfile, delimiter=',')
    # obtiene los atributos a partir de la primera fila
    header = next(reader)
    # creamos una lista donde guardar los diccionarios
    data = []
    for row in reader:
      # unimos el header con el row para crear una lista de tuplas
      iterable = zip(header, row)
      # convierte la lista de tuplas en un diccionario
      country_dict = {key: value for key, value in iterable}
      # agregamos el diccionario a la lista
      data.append(country_dict)
    return data

# para poder correr el archivo como script desde la terminal
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  
