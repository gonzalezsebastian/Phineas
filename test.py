# Checking if the radius collapse
def checkRange(stations):
    return print(len(stations))

#Extracting stations and coordinates (For now it only works with the first case as a test)
def extractStation(stations):
    cont = 0
    for station in stations:
        stations[cont] = (station[0]-station[1],station[0]+station[1])
        cont +=1
    rng1 = set(range(stations[0][0],stations[0][1]+1))
    rng2 = set(range(stations[1][0],stations[1][1]+1))
    rng3 = set(range(stations[2][0],stations[2][1]+1))
    rng1|=rng3
    rango = rng1.issuperset(rng2)
    if(rango==False):
        print("Se queda")
    return stations


positions = [(40,3),(5,5),(20,10),(40,10),(40,5),(5,5),(11,8),(20,10),(30,3),(40,10),(40,5),(0,10),(10,10),(20,10),(30,10),
(40,10),(40,3),(10,10),(18,10),(25,10),(40,3),(10,10),(18,10),(25,15),(0,0)]

L = positions[0][0]
R = positions[0][1]

stations = positions[1:(positions[0][1])+1]
#checkRange(stations)
print(stations)
extractStation(stations)
print(stations)
