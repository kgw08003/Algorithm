N, M = map(int, input().split())
first_set = {input().strip() for _ in range(N)}
count = 0

for _ in range(M):
    if input().strip() in first_set:
        count += 1

print(count)