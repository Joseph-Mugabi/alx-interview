# alx-interview
## 0x00-pascal_triangle
### 0-pascal_triangle.py

Pascal's Triangle is a mathematical pattern of numbers that forms a triangular shape. Each row of the triangle starts and ends with the number 1, and the interior numbers are the sum of the two numbers directly above them. The first few rows of Pascal's Triangle look like this:
```
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
   1 6 15 20 15 6 1
```
Creating a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
* Returns an empty list if n <= 0
* You can assume n will be always an integer
```
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x00-pascal_triangle$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x00-pascal_triangle$
```

```
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x00-pascal_triangle$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
josephgreen@JosephGreen-Mugabi:~/alx-interview-technical/0x00-pascal_triangle$ 
``