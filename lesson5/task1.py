while True:
    input_line = input("Введите строку: ").split()
    if not input_line:
        break
    with open("task1_text.txt", "a") as output_file:
        for i in range(len(input_line)):
            print(input_line[i], file=output_file)