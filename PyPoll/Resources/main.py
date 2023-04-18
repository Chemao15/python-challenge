import os, csv
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    csv_header= next (csvreader)
    print(f'CSV Header {csv_header}')

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

    
    
print('Election Results')
print('-------------------------')
print(f'Total Votes: {contador_votos}')
print('-------------------------')
print(f'Charles Casper Stockham: {(contador_charles/contador_votos)*100.:.2f}% ({contador_charles})')
print(f'Diana DeGette: {(contador_diana/contador_votos)*100.:.2f}% ({contador_diana})')
print(f'Raymon Anthony Doane: {(contador_raymo/contador_votos)*100.:.2f}% ({contador_raymo})')
print('-------------------------')
if contador_charles>contador_diana and contador_charles>contador_raymo:
    print ('Winner: Charles Casper Stockham')
if contador_diana>contador_charles and contador_diana>contador_raymo:
    print('Winner: Diana DeGette')
if contador_raymo>contador_charles and contador_raymo>contador_diana:
    print('Raymon Anthony Doane')
print('-------------------------')