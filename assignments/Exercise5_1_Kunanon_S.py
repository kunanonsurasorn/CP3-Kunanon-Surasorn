#นำเข้าตัวเลข 2 ตัวเข้ามาใส่ในตัวแปร first_number และ second_number
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

#กำหนดตัวแปรสำหรับการบวก(addition), การลบ(subtraction), การคูณ(multiplication) และ การหาร(division)
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
division = int(division)

#แสดงผลการคำนวณตามตัวแปรการบวก,การลบ,การคูณ และ การหารผ่านทางจอภาพ
print(first_number,"+",second_number,"=",addition)
print(first_number,"-",second_number,"=",subtraction)
print(first_number,"*",second_number,"=",multiplication)
print(first_number,"/",second_number,"=",division) 