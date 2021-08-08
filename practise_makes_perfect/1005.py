number = int(input())
input_list = list(map(int,input().split()))
#4 -6 3 -2 6 -4 -6 6        4,-6,3,-2,6,-4,-6,6
#number = 12
#input_list = [1,1,1,1,1,-6,1,1,1,1,1,1]
temp_max = 0
real_max = 0
first_pointer = 0
step_pointer = 0
real_max_first_pos = 0
real_max_last_pos = 0
for _ in iter(int,1):
    if (step_pointer) == (len(input_list)+1):
        break
    temp_max = sum(input_list[first_pointer:step_pointer])
    if temp_max <= 0:
        first_pointer = step_pointer
    elif temp_max > real_max:
        real_max_first_pos = first_pointer
        real_max_last_pos = step_pointer
        real_max = temp_max
    temp_max = 0
    step_pointer += 1
if real_max == 0:
    real_max = "Empty sequence"
    print(real_max)
else:
    print(*input_list[real_max_first_pos:real_max_last_pos])
    print(real_max)