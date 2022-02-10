# Phineas
Primax are authorized to operate over a road of length L. Each primax station is able to sell fuel over a specific area of influence, 
defined as the closed interval [x−r, x+r], where x is the primax station’s location on the road (0≤x≤L) and r is its radius of coverage (0&lt;r≤L). 
The points covered by a primax station are those within its radius of coverage. It is clear that the areas of influence may interfere, causing 
disputes among the corresponding primax stations. It seems to be better to close some primax stations, trying to minimize such interferences 
without reducing the service availability along the road. The owners have agreed to close some primax stations in order to avoid as many 
disputes as possible. You have been hired to write a program to determine the maximum number of primax stations that may be closed, so that 
every point on the road is in the area of influence of some remaining primax station. By the way, if some point on the road is not covered 
by any gas primax station, you must acknowledge the situation and inform about it.  
Input 
The input consists of several test cases. The first 
line of each test case contains two integer numbers L and G (separated by a column), representing the length of the road and the number of 
gas primax stations, respectively (1≤L≤10^8 , 1≤G≤10^4). Each one of the next G lines contains two integer numbers xi and ri (separated by a column) 
where xi is the location and ri is the radius of coverage of the i-th gas primax station (0≤xi≤L, 0 &lt;ri≤L). The last test case is followed by a 
line containing two zeros. The input must be read from Excel the file (check attached file).  
Output 
For each test case, print a line with the 
maximum number of gas primax stations that can be eliminated, so that every point on the road belongs to the area of influence of some not closed 
primax station. If some point on the road is not covered by any of the initial G gas primax stations, print −1 as the answer for such a case.
