import utils
import readcsv
import charts


def run():
  # lee el archivo csv y lo convierte en una lista de diccionarios
  data = readcsv.read_csv('./app/data.csv') 
  # le decimos que pais queremos saber la poblacion
  country = input('Type Country => ')

  # obtenemos la poblacion de ese pais
  result = utils.population_by_country(data, country)
  
  # si no hay resultados, mostramos un mensaje
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

def run1():
  data = readcsv.read_csv('./app/data.csv')
  countries = list(map(lambda x: x['Country/Territory'], data))
  print(countries)
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  print(percentages)
  charts.generate_pie_chart(countries, percentages)
  



  

if __name__ == '__main__':
  #run()
  run1()
  