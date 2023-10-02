import csv

with open('basket_players.csv', 'r') as archivo_csv:
    datos = csv.reader(archivo_csv, delimiter=';')

    for i, row in enumerate(datos):
        name = row[0]
        team = row[1]
        postion = row[2]
        height = row[3]
        weight = row[4]
        age = row[5]
        print(f'{name};{team};{postion};{height};{weight};{age}')




