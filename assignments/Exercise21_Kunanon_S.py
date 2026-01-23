from tkinter import *

def leftClickbutton(event):
    weight = textBoxWeight.get()
    weight = float(weight)
    height = textBoxHeight.get()
    height = float(height)
    result_number = weight/((height/100)**2)
    result_number = round(result_number, 2)
    if result_number >= 30.0:
        result_text = "อ้วนมาก"
    elif result_number >= 25:
        result_text = "อ้วน"
    elif result_number >= 23:
        result_text = "น้ำหนักเกิน"
    elif result_number >= 18.6:
        result_text = "น้ำหนักปกติ"
    else:
        result_text = "ผอมเกินไป"
    LabelResult.configure(text=result_text)

MainWindow = Tk()

#Height Input
LabelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
LabelHeight.grid(row = 0, column = 0)
textBoxHeight = (Entry(MainWindow))
textBoxHeight.grid(row = 0, column = 1)

#Weight Input
LabelWeight = Label(MainWindow, text = "น้ำหนัก (kg.)")
LabelWeight.grid(row = 1, column = 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1, column = 1)

#Calculation Process
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickbutton)
calculateButton.grid(row=2,column=0)

#BMI Output
LabelResult = Label(MainWindow, text = "ผลลัพธ์")
LabelResult.grid(row = 2, column = 1)
MainWindow.mainloop()