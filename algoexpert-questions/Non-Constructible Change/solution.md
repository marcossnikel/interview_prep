# Tim Ruscia Conceptual Overview

Me -> Big Fail.

Array of just positive numbers
values -> number of coins.
-> we want the minimum amount of change we can create
[1,2,5,] = 4

Brute Force Approach:
-> Loop thourgh all positive integers until you hit one that you can´t create.
1,2,3,4....K -> we can´t create.
-> Non Optimal  how ? -> Every Single interation need to look to all the coins.


-> Optimal solution -> more simple.

* Sort the input array (always a nice thing to thing about it in array questions.)
[5,7,1,1,2,3,22]
[1,1,2,3,5,7,22]

-> create variable [change = K] => tell us how much change we can create
that means, for an example... we can go through 1... until K changes.

- loop thourgh the coins array and see how much change can make it
change = 0
loop thourgh the sorted array.
at value 1 -> we can make 1$ of change
change = 1
next value... also 1 , that means that we can make it now 2$
change = 2
next value.... now 2, that means that we can make it $4 now. [between 1 and 4]
change = 4
next value... we can make it 7.... etc


-> always that hit a new value that is greather than the amount of change that we can make with the previous coins + 1 , that means that we cannot make the amount of change that we want.

need to see if our coin is greather than the change + 1 -> stop here.

u = {1}  <+ v = 1
c = 1
if v > c + 1 -> we cannot make c+1 change.
return c+1
if v <= c+1 -> we can make the change (c+v)

algorithm :
- sort input array
- loop through one coin at a time and see how much change we can create
- and check for some coin that we add that are greather than our change + 1
- return change + 1

time : o(n log n) 
space : o(1)
