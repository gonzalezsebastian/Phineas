import csv

def extractStation(stations,nst):
    #Tomar las estaciones
    con = 0 #Cuantas estaciones se eliminan
    totalCover = True #Controlar si no se cubre un espacio, en caso contrario mostrar el -1
    
    cont = 0
    for station in stations:
        stations[cont] = (station[0]-station[1],station[0]+station[1])
        cont +=1
    rng1 = set(range(stations[0][0],stations[0][1]+1))
    rng2 = set(range(stations[1][0],stations[1][1]+1))
    rng3 = set(range(stations[2][0],stations[2][1]+1))
    rng1|=rng3
    rango = rng1.issuperset(rng2)
    if(rango!=False):
        stations.pop(2)
        cont += 1
        
    if(totalCover==True):
        print(cont)
    else:
        print(-1)
    
    return stations

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

aux = coordinates[0][1]
auxL = coordinates[1:aux+1]



del coordinates[0:aux+1]
print(coordinates)
