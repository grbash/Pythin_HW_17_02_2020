profit = int(input("Input profit: "))
loss = int(input("Input loss: "))

if profit >= loss:
    print("Your profit: ", profit - loss)
    workers_count = int(input("Input number of workers: "))
    print("Profit per employee: ", (profit - loss) / workers_count)
else:
    print("Your loss: ", profit - loss)
    workers_count = int(input("Enter number of workers: "))
    print("Loss per employee: ", (profit - loss) / workers_count)
