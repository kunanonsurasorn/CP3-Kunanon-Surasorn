#กำหนดตัวแปรสำหรับการคำนวณอัตราเร็วประกอบด้วย ระยะทาง (distance) และ เวลา (time)
distance = int(input("Enter the distance : "))
time = int(input("Enter the time : "))

#คำนวณอัตราเร็วจากการหารตัวแปร distance และ time
velocity = distance/time #ค่าที่ได้จากการหารเป็นข้อมูลประเภท float
velocity = int(velocity) #แปลงชนิดข้อมูลจาก float เป็น int

#แสดงผลทางจอของตัวแปร velocity
print(velocity,"km/h")