import json

output_list = []
with open("task7_text_output.txt", "w") as output_file:
    with open("task7_text_input.txt", "r") as input_file:
        profit = {}
        for line in input_file:
            firm_name = line.split()[0]
            firm_profit = int(line.split()[2]) - int(line.split()[3])
            profit[firm_name] = firm_profit
        output_list.append(profit)
        major_profit_firms = []
        for el in profit.values():
            if int(el) > 0:
                major_profit_firms.append(int(el))
        avg_profit = sum(major_profit_firms) / len(major_profit_firms)
        output_list.append({"avg_profit": round(avg_profit, 2)})
    json.dump(output_list, output_file)
