import utils
import read_csv
import charts

data = [{
  'Country': 'Colombia',
  'Population': 300
}, {
  'Country': 'Bolivia',
  'Population': 300
}]

def run():
  # 
  data_csv = read_csv.read_csv('./data.csv')
  country = input('Type Country =>')

  result = utils.population_by_country(data_csv, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population_csv(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
  # 

  # keys, values = utils.get_population()
  # print(keys, values)

  # print(utils.a)

  # country = input('Type Country => ')
  # result = utils.population_by_country(data, country)
  # print(result)

if __name__ == '__main__':
  run()