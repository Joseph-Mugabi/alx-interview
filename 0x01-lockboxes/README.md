# Lockboxes

```
The function canUnlockAll() initializes a list called unlocked with False values 
for each box. It sets unlocked[0] to True since the first box (index 0) is already unlocked.
Then, it iterates over each box in boxes. If a box is unlocked (unlocked[box] is True),
it checks the keys inside that box. If a key's index is within the valid range of boxes,
it marks the corresponding box as unlocked by setting unlocked[key] to True.

Finally, the function returns True if all boxes are unlocked (all(unlocked)), and False otherwise.
```

```
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x01-lockboxes$ cat main_0.py 
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x01-lockboxes$ 
```
```
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x01-lockboxes$ ./main_0.py    
True
True
False
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x01-lockboxes$ 
```
