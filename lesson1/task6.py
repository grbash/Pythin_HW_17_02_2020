start = int(input("Input a: "))
target = int(input("Input b: "))
days = 1

while target > start:
    days = days + 1
    start = start + start * 0.1

print(days)
