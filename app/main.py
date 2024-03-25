import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  new_data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], new_data))
  percentages = list(map(lambda x: x['World Population Percentage'], new_data))
  charts.generate_pie_chart(countries, percentages)
  
  labels , values = utils.get_percentages(data)
  
  
  country = input('Type Country ==> ')

  result = utils.population_by_country(data,country)
  #charts.generate_bar_chart(country, labels, values)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)    
  
#Entry Point
if __name__ == '__main__':
  run()