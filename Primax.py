import csv

def extractStation(stations):
    #Tomar las estaciones
    con = 0 #Cuantas estaciones se eliminan
    totalCover = True #Controlar si no se cubre un espacio, en caso contrario mostrar el -1
    p = 1
    s=[]

    while p<=len(stations):
        stn = stations[p-1][1]
        cont = 0
        for e in range(p,p+stn):
            s.append([stations[e][0]-stations[e][1],stations[e][0]+stations[e][1]])
            print(s[0][0])
            #rng1 = set(range(s[0][0],s[0][1]+1))
            #rng2 = set(range(s[1][0],s[1][1]+1))
            #rng3 = set(range(s[2][0],s[2][1]+1))
            #rng1|=rng3
            #rango = rng1.issuperset(rng2)
            #print(rango)
        print(len(s))
        s = []
        p = p+1+stn
    

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

extractStation(coordinates)
