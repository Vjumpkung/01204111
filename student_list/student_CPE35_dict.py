import pandas as pd
data = pd.read_csv(r"CPE35_student_list.csv")
find_your_id = int(input("enter your student id "))
print("รหัสนิสิต :",find_your_id)   
print("ชื่อ(ไทย) :",*list(data[data["student_id"] == find_your_id]['thai_name']))
print("ชื่อ(อังกฤษ) :",*list(data[data["student_id"] == find_your_id]['english_name']))
print("ชื่อเล่น :",*list(data[data["student_id"] == find_your_id]['nickname']))
print("เบอร์โทร :",(str(*list(data[data["student_id"] == find_your_id]['telephone_number']))).replace("-",""))
print("เมลล์มหาลัย :",*list(data[data["student_id"] == find_your_id]['university_email']))