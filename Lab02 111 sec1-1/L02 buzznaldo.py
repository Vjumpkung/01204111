total_time = int(input("How long have Buzz played ?: "))
hours = int(total_time//60)
remain_time = int(total_time%60)
if remain_time > 20:
    hours = hours + 1
    remain_time = 0
discount = 100
if 2 <= hours < 4:
    discount = 90
elif 4 <= hours < 5:
    discount = 80
elif hours >= 5:
    discount = 70
print(f"Total price is {int(hours*900*discount/100)} baht.")