
positions = [(40,3),(5,5),(20,10),(40,10),(40,5),(5,5),(11,8),(20,10),(30,3),(40,10),(40,5),(0,10),(10,10),(20,10),(30,10),
(40,10),(40,3),(10,10),(18,10),(25,10),(40,3),(10,10),(18,10),(25,15),(0,0)]
positions.sort()

#print(positions)
station = list(dict.fromkeys(positions))
#print(station)
station.pop(0)

for i in range(len(station)):
    for j in range(len(station[i])):
        print(station[i][j])
        r = station[i][j]
