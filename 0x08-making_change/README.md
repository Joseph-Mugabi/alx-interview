# Making Change

```
The makeChange function uses dynamic programming to calculate the fewest 
number of coins needed to meet the given amount total. It iterates through 
the available coins and calculates the minimum number of coins needed for 
each possible total amount up to the given total.
```
```
The function starts by checking if the total amount is 0 or less. If so, 
it returns 0 immediately because no coins are needed in this case.

The variable i is initialized to 0, which will be used to keep track of 
the number of coins used.

The coins list is sorted in descending order using the sort method. 
This ensures that the largest denomination coins are considered first during the greedy algorithm.

The loop iterates through each coin in the sorted coins list.

For each coin, the code calculates how many times the current coin can 
fit into the remaining total amount. The increment variable holds this value.

The total amount is updated by subtracting the product of increment and coin.
 This represents the remaining total after using the current coin(s).

The counter i is incremented by the value of increment, 
representing the number of coins used.
```

The loop continues until either the total amount becomes 0 (which means the total has been successfully achieved) or until all coins have been considered.

If the total becomes 0, the function returns the value of i, which represents the minimum number of coins used to achieve the target amount.

If the loop finishes without reaching a total of 0, it means that the total could not be achieved with the given coins. In this case, the function returns -1.