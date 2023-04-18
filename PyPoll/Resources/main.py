import os, csv
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    csv_header= next (csvreader)
   

    contador_votos=0
    contador_charles=0
    contador_diana=0
    contador_raymo=0

    for row in csvreader:
        x=row[2]
        if x=='Charles Casper Stockham':
            contador_charles= contador_charles +1
        if x=='Diana DeGette':
            contador_diana=  contador_diana +1
        if x=='Raymon Anthony Doane':
            contador_raymo= contador_raymo +1
        
        contador_votos = contador_votos + 1

archivo = os.path.join('Resources','analysis.txt')     
with open (archivo, 'w') as file_object:
    file_object.write('Election Results\n')
    file_object.write('-------------------------\n')
    file_object.write(f'Total Votes: {contador_votos}\n')
    file_object.write('-------------------------\n')
    file_object.write(f'Charles Casper Stockham: {(contador_charles/contador_votos)*100.:.2f}% ({contador_charles})\n')
    file_object.write(f'Diana DeGette: {(contador_diana/contador_votos)*100.:.2f}% ({contador_diana})\n')
    file_object.write(f'Raymon Anthony Doane: {(contador_raymo/contador_votos)*100.:.2f}% ({contador_raymo})\n')
    file_object.write('-------------------------\n')
    if contador_charles>contador_diana and contador_charles>contador_raymo:
       file_object.write('Winner: Charles Casper Stockham\n')
    if contador_diana>contador_charles and contador_diana>contador_raymo:
       file_object.write('Winner: Diana DeGette\n')
    if contador_raymo>contador_charles and contador_raymo>contador_diana:
       file_object.write('Raymon Anthony Doane\n')
    file_object.write('-------------------------\n')