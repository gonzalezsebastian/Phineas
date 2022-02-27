import csv

def extractStation(stations):
    #Tomar las estaciones
    con = 0 #Cuantas estaciones se eliminan
    totalCover = True #Controlar si no se cubre un espacio, en caso contrario mostrar el -1
    
    cont = 0
    for station in stations:
        stations[cont] = (station[0]-station[1],station[0]+station[1])
        cont +=1

    if(totalCover==True):
        return con
    else:
        return -1

coordinates = []

#Extracting information from the input file
with open('input.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        coordinates.append(f"{row[0]}")


cont = 0
#Loading input into a list
for coord in coordinates:
    cord = coord.split(";")
    if (cont==0):
        cord[cont]=cord[0][3:5]
    coordinates[cont] = cord
    coordinates[cont][0] = int(coordinates[cont][0])
    coordinates[cont][1] = int(coordinates[cont][1])
    cont +=1

#while(bool(coordinates)):
#    extractStation(coordinates)
#    aux = coordinates[0][1]
#    print(aux)

#extractStation(coordinates)
aux = coordinates[0][1]
print(aux)
del coordinates[0:aux+1]
print(coordinates)
