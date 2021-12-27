i = 0
same_number_counter = 1
first_num = 0
previous_num = 0
current_num = 0
while True:
    if i == 0:
        previous_num = int(input())
        first_num = previous_num
        i = 1
    elif i == 1:
        current_number = int(input())
        if previous_num == current_number:
            same_number_counter = same_number_counter + 1
            same_number_is = current_number
            previous_num = current_number
            unequal_attempt = 0
        else:
            previous_num = current_number
            if same_number_counter != 1:
                i = 2
        if current_number == 0: 
            break
    else:
        current_number = int(input())
        if previous_num == current_number:
            previous_num = current_number
        else:
            previous_num = current_number
        if current_number == 0: 
            break
        
if same_number_counter == 1:
    same_number_is = first_num
print(same_number_counter)
print(same_number_is)