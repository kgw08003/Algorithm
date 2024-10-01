a = 0
max_a = 0
psg = 0

for i in range(10):
    out_a, in_a = map(int, input().split())
    psg += (in_a - out_a)
    max_a = max(psg, max_a)
print(max_a)