output_dict = {}

with open("task06_text.txt", "r") as input_file:
    for line in input_file:
        subj_name, subj_hours = line.split(":")
        hours = sum(
            map(int, "".join([item for item in subj_hours if item == " " or (item >= "0" and item <= "9")]).split()))
        output_dict[subj_name] = str(hours) + "h"

print(f"{output_dict}")
