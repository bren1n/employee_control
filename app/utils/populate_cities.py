import csv
import html


cities_list = open('./cities.csv', 'r')

sql = ''
csv_reader = csv.reader(cities_list)
for row in csv_reader:
    sql += f'INSERT INTO app_city(name) VALUES ("{html.unescape(row[0])}");\n'
    
output = open('./output.sql', 'w')
output.write(sql)