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

# Lectura del archivo y manipulación de datos
def process_csv():
    with open('basket_players.csv', 'r') as archivo_csv:
        datos = csv.DictReader(archivo_csv, delimiter=';')
        for i, row in enumerate(datos):
            name = row['Name']
            team = row['Team']
            position = translate_position(row['Position'])
            height = round(float(row['Heigth']) * 2.54, 2)
            weight = round(float(row['Weigth']) * 0.45, 2)
            age = round(float(row['Age']))
            write_player_info_to_csv('jugadors_basket.csv', name, team, position, height, weight, age)

# Crear archivo csv con los datos cambiados
def write_player_info_to_csv(file_path, name, team, position, height, weight, age):
    file_exists = os.path.isfile(file_path)
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Nom', 'Equip', 'Posició', 'Altura', 'Pes', 'Edad']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames , delimiter = '^')

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Nom': name,
            'Equip': team,
            'Posició': position,
            'Altura': height,
            'Pes': weight,
            'Edad': age
        })

# Calcular estadísticas jugadores del archivo csv
def calculate_statistics(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='^')
        for row in reader:
            data.append(row)
    # Printar el jugador con el mayor peso
    max_weight_player = max(data, key=lambda x: float(x['Pes']))
    print('a) Nom del jugador amb el pes més alt:', max_weight_player['Nom'])

    # Printar el jugador con el menor peso
    min_height_player = min(data, key=lambda x: float(x['Altura']))
    print('b) Nom del jugador amb l’alçada més petita:', min_height_player['Nom'])

    # Printar cada equipo y su media de peso y media de altura.
    team_weights = defaultdict(list)
    team_heights = defaultdict(list)

    for player in data:
        team_weights[player['Equip']].append(float(player['Pes']))
        team_heights[player['Equip']].append(float(player['Altura']))

    print('c) Mitjana de pes i alçada de jugador per equip:')
    for team in team_weights:
        avg_weight = sum(team_weights[team]) / len(team_weights[team])
        avg_height = sum(team_heights[team]) / len(team_heights[team])
        print(f'   Equip: {team}, Mitjana de pes: {avg_weight:.2f}, Mitjana de alçada: {avg_height:.2f}')

    # Printar cada posición y el total de jugadores en esa posición
    position_counts = defaultdict(int)
    for player in data:
        position_counts[player['Posició']] += 1

    print('d) Recompte de jugadors per posició:')
    for position, count in position_counts.items():
        print(f'   Posició: {position}, Jugadors: {count}')

    # Printar el numero de jugadores que hay por edad
    age_distribution = defaultdict(int)
    for player in data:
        age_distribution[int(player['Edad'])] += 1

    print('e) Distribució de jugadors per edat:')
    for age, count in sorted(age_distribution.items()):
        print(f'   Edat: {age}, Jugadors: {count}')

# Main de la actividad
def __init__():
    process_csv()
    calculate_statistics('jugadors_basket.csv')
__init__()





