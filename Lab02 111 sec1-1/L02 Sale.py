all_of_price = []
how_many_days = int(input("How many day : "))
i = 1
while i <= how_many_days:
    input_it = float(input(f"Input price in day {i} : "))
    all_of_price.append(input_it)
    i = i+1
discount = 0.95
for j in range(len(all_of_price)):
    all_of_price[j] = all_of_price[j]*discount
    discount = discount - 0.01
txt = "Summary price = {total_all_of_price:.2f}"
print(txt.format(total_all_of_price = sum(all_of_price)))