#from pprint import pp #do not use in python 3.7
flight_data = []
#1
def AddData():
    FlightData = {}
    Add_Data = input("Add data : ")
    Add_Data = Add_Data.split()
    HowToAddID = ["id","from","to","reserve","maximum"]
    HowToAddData = [0,1,3,4,6]
    for i in range(len(HowToAddID)):
        if HowToAddData[i] in (4,6):
            FlightData.setdefault(HowToAddID[i],int(Add_Data[HowToAddData[i]]))
        else:
            FlightData.setdefault(HowToAddID[i],Add_Data[HowToAddData[i]])
    FlightData.setdefault("MoreReserved",[])
    flight_data.append(FlightData)
#2
def showFlightData():
    enter_code = input("Enter code : ")
    flightid = list_flight_data()[0]
    i = flightid.index(enter_code)
    print(f"{flight_data[i]['id']} is from {flight_data[i]['from']} to {flight_data[i]['to']}, number of people booking is {flight_data[i]['reserve']}/{flight_data[i]['maximum']}")
#3
def All_flight_data():
    print("All flight data")
    for i in range(len(flight_data)):
        print(f"{flight_data[i]['id']} is from {flight_data[i]['from']} to {flight_data[i]['to']}, number of people booking is {flight_data[i]['reserve']}/{flight_data[i]['maximum']}")
#4
def Passenger_buy_Tua_Kleang_Bin ():
    get_flight_data = list_flight_data()
    getFlightId = get_flight_data[0]
    getreserve = get_flight_data[1]
    getmaximum = get_flight_data[2]
    Name = input("Enter your name : ")
    Fight = input("Enter flight code : ")
    if (Fight in getFlightId) and (getreserve[getFlightId.index(Fight)] < getmaximum[getFlightId.index(Fight)]):
        print("Success")
        flight_data[getFlightId.index(Fight)]['MoreReserved'].append(Name)
        flight_data[getFlightId.index(Fight)]['reserve'] += 1
    else:
        print("The flight is full, Sorry")
#5
def show_people_fight_data():
    ur_name = input("Enter your name : ")
    id_reserved = [flight_data[i]['id'] for i in range(len(flight_data)) if ur_name in flight_data[i]['MoreReserved']]
    print(f"{ur_name} is booking flight code = ",end="")
    print(*(id_reserved[::-1]))
#others
def list_flight_data():
    getFlightId     = [flight_data[i]['id']           for i in range(len(flight_data))]
    getreserve      = [flight_data[i]['reserve']      for i in range(len(flight_data))]
    getmaximum      = [flight_data[i]['maximum']      for i in range(len(flight_data))]
    getMoreReserved = [flight_data[i]['MoreReserved'] for i in range(len(flight_data))]
    return(getFlightId,getreserve,getmaximum,getMoreReserved)
#main
def main():
    print("Select menu :\n1. add flight data\n2. flight data by code\n3. show all flight data\n4. flight booking\n5. show people flight data\n6. exit")
    while True:
        menu = int(input("menu : "))
        if   menu == 6: break
        elif menu == 1: AddData()
        elif menu == 2: showFlightData()
        elif menu == 3: All_flight_data()
        elif menu == 4: Passenger_buy_Tua_Kleang_Bin()
        elif menu == 5: show_people_fight_data()
main()
print("EXIT!!!!!!!!!!!!!!!")