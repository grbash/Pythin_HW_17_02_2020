n = int(input("Input number: "))
k = 10
max_digit = 0

while n // k > 0:
    if n % k > max_digit:
        max_digit = n % k
    n = n // 10
if n > max_digit:
    max_digit = n

print("max digit is", max_digit)

