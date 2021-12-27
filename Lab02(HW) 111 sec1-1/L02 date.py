day = int(input("d: "))
month = int(input("m: "))
year = int(input("y: "))
total_days_from_month = 0
i = 1
while i <= int(month-1):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        this_month = 31
        total_days_from_month = total_days_from_month + this_month
    elif i == 4 or i == 6 or i == 9 or i == 11:
        this_month = 30
        total_days_from_month = total_days_from_month + this_month
    elif i == 2:
        if year%4 == 0 and year%100 != 0:
            this_month = 29
        elif year%400==0:
            this_month = 29
        else:
            this_month = 28
        total_days_from_month = total_days_from_month + this_month
    i = i+1
print(day + total_days_from_month)