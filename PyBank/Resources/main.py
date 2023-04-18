import os, csv
csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)
    contador_mes = 0
    contador_pro = 0
    contador_maximo = 0
    maximo = 0
    menor = 0
    valor_maximo = 0
    m=[]
    n=[]
    y=[]
    for row in csvreader:
        x=int(row[1])
        dia=row[0]
        contador_pro = contador_pro + x
        m.append(x)
        y.append(dia)
        contador_mes = contador_mes + 1

        if contador_mes > 1:
            maximo = x - m[contador_mes-2]
            contador_maximo = contador_maximo + maximo
            n.append(maximo)
        
        if contador_mes == 3:
            segundo=n[contador_mes-2]
            primero=n[contador_mes-3]
            if segundo>primero:
                valor_maximo=segundo
                valor_minimo=primero
                dia_mes = (y[contador_mes-1])
                dia_mes_m = (y[contador_mes-1])
            else:
                valor_maximo=primero
                dia_mes = (y[contador_mes-1])
                valor_minimo=segundo
                dia_mes_m = (y[contador_mes-1])
        if contador_mes > 3:
            if n[contador_mes-2]>valor_maximo:
                valor_maximo= n[contador_mes-2]
                dia_mes = (y[contador_mes-1])
            if n[contador_mes-2]<valor_minimo:
                valor_minimo= n[contador_mes-2]
                dia_mes_m = (y[contador_mes-1])
    
archivo = os.path.join('analysis.txt')      
with open (archivo, 'w') as file_object:
    file_object.write('Financial Analysis \n')
    file_object.write('---------------------------- \n')
    file_object.write(f'Total Months: {contador_mes}\n')
    file_object.write(f'Total: {contador_pro}\n')
    file_object.write(f'Average Change: {contador_maximo/len(n):.2f}\n')
    file_object.write(f'Greatest Increase in Profits: {dia_mes} ({valor_maximo})\n')
    file_object.write(f'Greatest Decrease in Profits: {dia_mes_m} ({valor_minimo})\n')
     