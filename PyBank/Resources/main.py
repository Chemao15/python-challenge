import os, csv
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)
    contador_mes = 0
    contador_pro = 0
    contador_maximo = 0
    maximo = 0
    menor = 0
    m=[]
    n=[]
    for row in csvreader:
        x=int(row[1])
        contador_pro = contador_pro + x
        m.append(x)
        contador_mes = contador_mes + 1

        if contador_mes > 1:
            maximo = x - m[contador_mes-2]
            contador_maximo = contador_maximo + maximo
            n.append(maximo)
        
        if contador_mes > 2:
            n[contador_mes]>n[contador_mes-1]


    print ('Financial Analysis')
    print (f'Total Months: {contador_mes}')
    print (f'Total: {contador_pro}')
    print (f'Average Change: {contador_maximo/len(n)}')
    print (f'Greatest Increase in Profits: {max (n)}')
    print (f'Greatest Decrease in Profits: {min (n)}')
    