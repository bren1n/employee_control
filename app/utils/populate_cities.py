import csv
import html


cities_list = open('./cities.csv', 'r')
cities_names = []
sql = ''
csv_reader = csv.reader(cities_list)

for row in csv_reader:
    cities_names.append(html.unescape(row[0]))

cities_names = sorted(cities_names)

for city in cities_names:
    sql += f'INSERT INTO app_city(name) VALUES ("{city}");\n'
    
output = open('./output.sql', 'w')
output.write(sql)