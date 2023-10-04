import csv

def translate_position(position):
    position_translations = {
        'Point Guard': 'Base',
        'Shooting Guard': 'Escorta',
        'Small Forward': 'Aler',
        'Power Forward': 'Ala-Pivot',
        'Center': 'Pivot'
    }
    return position_translations.get(position, position)

def print_player_info(name, team, position, height, weight, age):
    print(f'{name};{team};{position};{height};{weight};{age}')

def process_csv():
    with open('basket_players.csv', 'r') as archivo_csv:
        datos = csv.DictReader(archivo_csv, delimiter=';')
        print("Nom;Equip;Posició;Altura;Pes;Edad")
        for i, row in enumerate(datos):
            name = row['Name']
            team = row['Team']
            position = translate_position(row['Position'])
            height = round(float(row['Heigth']) * 2.54, 2)
            weight = round(float(row['Weigth']) * 0.45, 2)
            age = row['Age']
            print_player_info(name, team, position, height, weight, age)

def exercici_1():
    process_csv()

exercici_1()


