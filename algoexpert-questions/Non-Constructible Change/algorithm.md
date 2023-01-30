## Non - Constructible Change

**Brute Force Algorithm**
- Loop through all positive integers until you hit one that you cannot create
- Non Optimal because every single interation need to look to all the coins.

**Optimal Solution**
*actually more simple*

- Sort the input array (in arrays questions always try to see if sort the array will help you)
- Create an variable "possible change" to keep track of the possible amount of change to be created.
- Loop through the coins array and see how much change can make it.

- If we hit a new value that is greather tan the amount of change that we can make with the previous coins + 1, that means that we cannot make the amount of change that we want.

- So , if our coin is greather than the change + 1

- Just return the previous possible change

## Complexity
**Time :** O(N log N)

**Space :** O(1)