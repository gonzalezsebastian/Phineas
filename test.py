""""
Primax are authorized to operate over a road of length L. Each primax station is able to sell fuel over a specific area of influence, defined as the closed interval [x−r, x+r], where x is the primax station’s location on the road (0≤x≤L) and r is its radius of coverage (0<r≤L). The points covered by a primax station are those within its radius of coverage. It is clear that the areas of influence may interfere, causing disputes among the corresponding primax stations. It seems to be better to close some primax stations, trying to minimize such interferences without reducing the service availability along the road. 

The owners have agreed to close some primax stations in order to avoid as many disputes as possible. You have been hired to write a program to determine the maximum number of primax stations that may be closed, so that every point on the road is in the area of influence of some remaining primax station. By the way, if some point on the road is not covered by any gas primax station, you must acknowledge the situation and inform about it.

Input
The input consists of several test cases. The first line of each test case contains two integer numbers L and G (separated by a column), representing the length of the road
and the number of gas primax stations, respectively (1≤L≤10^8 , 1≤G≤10^4). Each one of the next G lines contains two integer numbers xi and ri (separated by a column) where
xi is the location and ri is the radius of coverage of the i-th gas primax station (0≤xi≤L, 0 <ri≤L). The last test case is followed by a line containing two zeros.
The input must be read from Excel the file (check attached file).

Output
For each test case, print a line with the maximum number of gas primax stations that can be eliminated, so that every point on the road belongs to the area of influence of some not closed primax station. 
If some point on the road is not covered by any of the initial G gas primax stations, print −1 as the answer for such a case.
"""

positions = [(40,3),(5,5),(20,10),(40,10),(40,5),(5,5),(11,8),(20,10),(30,3),(40,10),(40,5),(0,10),(10,10),(20,10),(30,10),(40,10),
(40,3),(10,10),(18,10),(25,10),(40,3),(10,10),(18,10),(25,15),(0,0)]
#positions.sort()
"""

OtUTPUT: 0,2,3,-1,1

Caso de 40,3
40 m para 3 estaciones 
Side Area
5    0,10   
20   10,30
40   30,50

Caso de 40,5
Side Area
5    0,10  
11   3,19  
20   10,30 
30   27,33 
40   30,50  

Caso de 40,5 .2
Side Area
0    0,10 
10   0,20 
20   10,30 
30   20,40 
40   30,50 

Caso de 40,3 .2
10   0,10
18   8,26
25   15,35

Caso de 40,3 .3
10   0,10
18   8,26
25   10,40

"""

print(positions)

#Ordenar los casos teniendo en cuenta que el primer valor muestra la longitud de la vía y cuantas estaciones hay en ella. Teniendo en cuenta eso, trabajar con el número de estaciones propuestas y hacer la eliminación correspondiente.



#station = list(dict.fromkeys(positions))
#print(station)
#station.pop(0)

#for i in range(len(station)):
    #for j in range(len(station[i])):
        #print(station[i][j])
        #r = station[i][j]
