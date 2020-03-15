# -*- coding: utf-8 -*-
interpreter = {"One": "Odin", "Two": "Dva", "Three": "Tri", "Four": "4etire"}

with open("task4_text_output.txt", "a") as output_file:
    with open("task4_text_input.txt", "r") as input_file:
        for line in input_file:
            line = line.split()
            output_file.writelines(interpreter[line[0]] + " - " + line[1] + "\n")
