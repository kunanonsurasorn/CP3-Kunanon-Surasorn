from forex_python.converter import CurrencyRates
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tkinter as tk

currency_rates = CurrencyRates()
today = datetime.today()
today_str = today.strftime("%d/%m/%Y")
currency_list = ["THB","USD","EUR","GBP","CNY","JPY"]

def convert_button_click():
    try:
        money_amount_input = float(money_input.get())
    except ValueError:
        converted_currency_result.configure(text="Invalid number")
        return
    
    original_currency = original_currency_var.get()
    converted_currency = converted_currency_var.get()

    rate = currency_rates.get_rate(original_currency, converted_currency, today)
    money_value_output = money_amount_input*rate
    money_value_output = round(money_value_output,2)

    original_currency_label.configure(text=original_currency)
    original_currency_result.configure(text=money_amount_input)
    converted_currency_label.configure(text=converted_currency)
    converted_currency_result.configure(text=money_value_output)

def currency_history(original_currency,converted_currency,days=7):
    rate_history = []

    for i in range(days):
        current_date = today - timedelta(days=i)
        current_date = current_date.date()
        rate = currency_rates.get_rate(original_currency, converted_currency, current_date)
        rate = round(rate, 2)
        rate_history.append((current_date, rate))

    return list(reversed(rate_history))
    
def currency_graph(rate_history,original_currency,converted_currency):
    x = [item[0] for item in rate_history]
    y = [item[1] for item in rate_history]
    
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
    one_day_ago = len(history) - 2
    seven_days_ago = len(history) - 8
    thirty_days_ago = 0

    date_before_1day_difference_output.configure(text=f"{diff_from_index(one_day_ago)} %")
    date_before_7day_difference_output.configure(text=f"{diff_from_index(seven_days_ago)} %")
    date_before_30day_difference_output.configure(text=f"{diff_from_index(thirty_days_ago)} %")
    
    currency_graph(history, original_currency, converted_currency)

main_window = tk.Tk()

title_label = tk.Label(main_window, text = "Foreign Exchange Currency")
title_label.grid(row = 0, column = 1)

original_currency_title_label = tk.Label(main_window, text = "Original Currency")
original_currency_title_label.grid(row = 1, column = 0)

original_currency_var = tk.StringVar()
converted_currency_var = tk.StringVar()

original_currency_var.set("USD")
converted_currency_var.set("THB")

original_currency_menu = tk.OptionMenu(main_window,original_currency_var,*currency_list)
original_currency_menu.grid(row=1, column=1)

converted_currency_menu = tk.OptionMenu(main_window,converted_currency_var,*currency_list)
converted_currency_menu.grid(row=2, column=1)

converted_currency_title_label = tk.Label(main_window, text = "Converted Currency")
converted_currency_title_label.grid(row = 2, column = 0)

money_input_label = tk.Label(main_window, text = "Input Money")
money_input_label.grid(row = 3, column = 0)

money_input = (tk.Entry(main_window))
money_input.grid(row = 3, column = 1)

convert_button = tk.Button(main_window,text="Convert Currency",command=convert_button_click)
convert_button.grid(row=5, column=0)

compare_button = tk.Button(main_window,text="Compare & Graph",command=compare_button_click)
compare_button.grid(row=5, column=1)

original_currency_label = tk.Label(main_window, text = "Original Currency")
original_currency_label.grid(row = 6, column = 0)

original_currency_result = tk.Label(main_window, text = "Original Currency Output")
original_currency_result.grid(row = 6, column = 1)

converted_currency_label = tk.Label(main_window, text = "Converted Currency")
converted_currency_label.grid(row = 7, column = 0)

converted_currency_result = tk.Label(main_window, text = "Converted Currency Output")
converted_currency_result.grid(row = 7, column = 1)

date_label = tk.Label(main_window, text = "Date")
date_label.grid(row = 4, column = 0)

today_output = tk.Label(main_window, text = f"{today_str}")
today_output.grid(row = 4, column = 1)

difference_label = tk.Label(main_window, text = "Difference")
difference_label.grid(row = 1, column = 2)

date_before_1day = today - timedelta(days=1)
date_before_1day = date_before_1day.date()
date_before_1day_format = date_before_1day.strftime("%d/%m/%Y")
date_before_1day_output = tk.Label(main_window, text = f"{date_before_1day_format}")
date_before_1day_output.grid(row = 2, column = 2)

date_before_1day_difference_output = tk.Label(main_window, text = 0)
date_before_1day_difference_output.grid(row = 3, column = 2)

date_before_7days = today - timedelta(days=7)
date_before_7days = date_before_7days.date()
date_before_7days_format = date_before_7days.strftime("%d/%m/%Y")
date_before_7days_output = tk.Label(main_window, text = f"{date_before_7days_format}")
date_before_7days_output.grid(row = 4, column = 2)

date_before_7day_difference_output = tk.Label(main_window, text = 0)
date_before_7day_difference_output.grid(row = 5, column = 2)

date_before_30days = today - timedelta(days=30)
date_before_30days = date_before_30days.date()
date_before_30days_format = date_before_30days.strftime("%d/%m/%Y")
date_before_30days_output = tk.Label(main_window, text = f"{date_before_30days_format}")
date_before_30days_output.grid(row = 6, column = 2)

date_before_30day_difference_output = tk.Label(main_window, text = 0)
date_before_30day_difference_output.grid(row = 7, column = 2)

main_window.mainloop()