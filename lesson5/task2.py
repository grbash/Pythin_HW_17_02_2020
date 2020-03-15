k = 0
with open("task2_text.txt", "r") as input_file:
    for input_line in input_file:
        k = k + 1
        if input_line[-1] == "\n": # для красоты вывода удалим все символы перевода на новую строку
            input_line = input_line[:-1]
        word_in_input_line = input_line.split()
        print(f"Количесвто слов в строке - '{input_line}' - {len(word_in_input_line)}")
    print(f"Количесвто строк в файле: {k}")
