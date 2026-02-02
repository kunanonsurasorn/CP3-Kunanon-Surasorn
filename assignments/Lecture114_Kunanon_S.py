from forex_python.converter import CurrencyRates
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tkinter import * 

currency_rates = CurrencyRates()
present_day = datetime.today()
present_day_format = present_day.strftime("%d/%m/%Y")
list_currency = ["THB","USD","EUR","GBP","CNY","JPY"]

def convert_button_click():
    try:
        money_amount_input = float(money_input.get())
    except ValueError:
        label_result4.configure(text="Invalid number")
        return
    original_currency = original_currency_var.get()
    converted_currency = converted_currency_var.get()
    rate = currency_rates.get_rate(original_currency, converted_currency, present_day)
    money_value_output = money_amount_input*rate
    money_value_output = round(money_value_output,2)
    label_result1.configure(text=original_currency)
    label_result2.configure(text=money_amount_input)
    label_result3.configure(text=converted_currency)
    label_result4.configure(text=money_value_output)

def currency_history(original_currency,converted_currency,days=7):
    date_currency_value = []
    for i in range(days):
        date = present_day - timedelta(days=i)
        date = date.date()
        rate = currency_rates.get_rate(original_currency, converted_currency, date)
        rate = round(rate, 2)
        date_currency_value.append((date, rate))
    return list(reversed(date_currency_value))
    
def currency_graph(date_currency_value,original_currency,converted_currency):
    x = [item[0] for item in date_currency_value]
    y = [item[1] for item in date_currency_value]
    
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.title(f"{original_currency} to {converted_currency} Exchange Rate")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
    plt.gcf().autofmt_xdate()
    plt.show()

def compare_button_click():
    original_currency = original_currency_var.get()
    converted_currency = converted_currency_var.get()

    history = currency_history(original_currency, converted_currency, days=30)
    rate_today = history[-1][1]

    def diff_from_index(idx):
        past_rate = history[idx][1]
        return round(((rate_today - past_rate) / past_rate) * 100, 2)
    
    #present day sequence is -1.
    one_day_ago = -2
    seven_days_ago = -8
    thirty_days_ago = 0

    label_result6.configure(text=f"{diff_from_index(one_day_ago)} %")
    label_result7.configure(text=f"{diff_from_index(seven_days_ago)} %")
    label_result8.configure(text=f"{diff_from_index(thirty_days_ago)} %")
    
    currency_graph(history, original_currency, converted_currency)

main_window = Tk()

title_label = Label(main_window, text = "Foreign Exchange Currency")
title_label.grid(row = 0, column = 1)

original_currency_label = Label(main_window, text = "Original Currency")
original_currency_label.grid(row = 1, column = 0)

original_currency_var = StringVar()
converted_currency_var = StringVar()

original_currency_var.set("USD")
converted_currency_var.set("THB")

original_currency_menu = OptionMenu(main_window,original_currency_var,*list_currency)
original_currency_menu.grid(row=1, column=1)

converted_currency_menu = OptionMenu(main_window,converted_currency_var,*list_currency)
converted_currency_menu.grid(row=2, column=1)

converted_currency_label = Label(main_window, text = "Converted Currency")
converted_currency_label.grid(row = 2, column = 0)

money_input_label = Label(main_window, text = "Input Money")
money_input_label.grid(row = 3, column = 0)

money_input = (Entry(main_window))
money_input.grid(row = 3, column = 1)

convert_button = Button(main_window,text="Convert Currency",command=convert_button_click)
convert_button.grid(row=5, column=0)

compare_button = Button(main_window,text="Compare & Graph",command=compare_button_click)
compare_button.grid(row=5, column=1)

label_result1 = Label(main_window, text = "Original Currency")
label_result1.grid(row = 6, column = 0)

label_result2 = Label(main_window, text = "Original Currency Output")
label_result2.grid(row = 6, column = 1)

label_result3 = Label(main_window, text = "Converted Currency")
label_result3.grid(row = 7, column = 0)

label_result4 = Label(main_window, text = "Converted Currency Output")
label_result4.grid(row = 7, column = 1)

date_label = Label(main_window, text = "Date")
date_label.grid(row = 4, column = 0)

date_output0 = Label(main_window, text = f"{present_day_format}")
date_output0.grid(row = 4, column = 1)

label_result5 = Label(main_window, text = "Difference")
label_result5.grid(row = 1, column = 2)

date_before_oneday = present_day - timedelta(days=1)
date_before_oneday = date_before_oneday.date()
date_before_oneday_format = date_before_oneday.strftime("%d/%m/%Y")
date_output1 = Label(main_window, text = f"{date_before_oneday_format}")
date_output1.grid(row = 2, column = 2)

label_result6 = Label(main_window, text = 0)
label_result6.grid(row = 3, column = 2)

date_before_twodays = present_day - timedelta(days=7)
date_before_twodays = date_before_twodays.date()
date_before_twodays_format = date_before_twodays.strftime("%d/%m/%Y")
date_output2 = Label(main_window, text = f"{date_before_twodays_format}")
date_output2.grid(row = 4, column = 2)

label_result7 = Label(main_window, text = 0)
label_result7.grid(row = 5, column = 2)

date_before_threedays = present_day - timedelta(days=30)
date_before_threedays = date_before_threedays.date()
date_before_threedays_format = date_before_threedays.strftime("%d/%m/%Y")
date_output3 = Label(main_window, text = f"{date_before_threedays_format}")
date_output3.grid(row = 6, column = 2)

label_result8 = Label(main_window, text = 0)
label_result8.grid(row = 7, column = 2)

main_window.mainloop()
