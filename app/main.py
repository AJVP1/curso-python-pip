import utils
import readcsv
import charts


def run():
  # lee el archivo csv y lo convierte en una lista de diccionarios
  data = readcsv.read_csv('data.csv') 
  data = list(filter(lambda x: x['Continent'] == 'South America', data))

  # filtramos por sur america para mostrar el porcentaje de cada pais
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  
  # le decimos que pais queremos saber la poblacion
  country = input('Type Country => ')
  # obtenemos la poblacion de ese pais
  result = utils.population_by_country(data, country)
  
  # si no hay resultados, mostramos un mensaje
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

def run1():
  data = readcsv.read_csv('data.csv')
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  



  

if __name__ == '__main__':
  run()
  #run1()
  