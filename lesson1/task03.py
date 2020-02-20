# почему-то файл task3.py создать не удалось
n = int(input("Input n: "))
k = 1

while n // k > 0:
    k = k * 10

print(n * k * k + 2 * n * k + 3 * n)
