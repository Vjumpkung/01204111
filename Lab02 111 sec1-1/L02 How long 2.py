kilo = int(input("Input distance(kilometer): "))
minute = kilo*10
hour = minute//60
remiander_from_hour = minute%60
if minute == 60:
    total_time = remiander_from_hour
else:
    additional_time = hour*10
    total_time = remiander_from_hour + additional_time
print(f"It takes {hour} hours and {total_time} minutes to reach the destination.")