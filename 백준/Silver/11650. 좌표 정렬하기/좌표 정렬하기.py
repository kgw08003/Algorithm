import sys
input = sys.stdin.readline
lst = []
 
for i in range(int(input())):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort()
 
for i, j in lst:
    print(f'{i} {j}')