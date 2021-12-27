i = 1
player_speed = 0
police_distance = []
while True:
    police_distance_input = int(input("Input distance: "))
    police_distance.append(police_distance_input)
    print(f"Police distance: {sum(police_distance)}")
    player_speed = player_speed + 2**i
    criminal_distence = 100 + player_speed
    print(f"Criminal distance: {criminal_distence}")
    i = i+1
    if sum(police_distance) >= criminal_distence:
        print("Caught him!")
        break
    else:
        continue