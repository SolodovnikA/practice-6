n, k, m = map(int, input().split())
time = 0

while n > k:
    time += m
    n -= k

time += m
print(time * 2)