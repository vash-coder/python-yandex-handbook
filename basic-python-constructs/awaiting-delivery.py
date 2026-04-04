n = int(input())
m = int(input())
t = int(input())

hour = (n + ((m + t) // 60)) % 24
minute = (m + t) % 60

print(f'{hour:02}:{minute:02}')