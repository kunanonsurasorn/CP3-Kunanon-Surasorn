import tkinter as tk
from forex_python.converter import CurrencyRates
from datetime import datetime,timedelta

currency_list = ["THB","USD","EUR","GBP","CNY","JPY"]
currency_rates = CurrencyRates()
today = datetime.today()
today_str = today.strftime("%d/%m/%Y")

def convert_button_click():
    try:
        money_amount_input = float(input_money_entry.get())
    except ValueError:
        converted_money_output.configure(text="Invalid number")
        return
    
    original_currency = original_currency_var.get()
    converted_currency = converted_currency_var.get()

    if original_currency == converted_currency:
        converted_money_output.configure(text="Same Currency")
        return

    rate = currency_rates.get_rate(original_currency, converted_currency, datetime.today())
    money_value_output = money_amount_input*rate
    money_value_output = round(money_value_output,2)

    converted_money_output.configure(text=money_value_output)

def currency_history(original_currency,converted_currency,days=4):
    rate_history = []
    today = datetime.today().date()

    for i in range(days):
        current_date = today - timedelta(days=i)
        try:
            rate = currency_rates.get_rate(original_currency, converted_currency, current_date)
            rate = round(rate, 2)
            rate_history.append((current_date, rate))
        except Exception as e:
            print("History Error:",e)
            continue
    return list(reversed(rate_history))

def compare_button_click():
    try:
        original_currency = original_currency_var.get()
        converted_currency = converted_currency_var.get()

        history = currency_history(original_currency, converted_currency)   

        if len(history) < 4:
            today_output.configure(text="Not enough data")
            return
        
        today_rate = history[-1][1]
        yesterday_rate = history[-2][1]
        two_days_rate = history[-3][1]
        three_days_rate = history[-4][1]

        today_output.configure(text=f"{today_rate}")
        yesterday_output.configure(text=f"{yesterday_rate}")
        two_days_ago_output.configure(text=f"{two_days_rate}")
        three_days_ago_output.configure(text=f"{three_days_rate}")

        rates = [rate for date,rate in history]
        average = round(sum(rates)/len(rates),2)
        maximum = max(rates)
        minimum = min(rates)
        range_max_min = round(max(rates)-min(rates),2)

        average_value_output.configure(text=average)
        max_value_output.configure(text=maximum)
        min_value_output.configure(text=minimum)
        range_max_min_output.configure(text=range_max_min)
    
    except Exception as e:
        print("Compare Error:",e)
        today_output.configure(text="Error")
     
main_window = tk.Tk()
main_window.geometry("600x500")
main_window.resizable(False,False)

title_label = tk.Label(main_window, text = "Foreign Exchange Currency",font=("Segoe UI",15))
title_label.grid(row = 0, column = 0,columnspan=5,padx=10,pady=10)

input_currency_label = tk.Label(main_window, text = "Input Original Currency",font=("Segoe UI",10))
input_currency_label.grid(row = 1, column = 0,padx=5,pady=5)

original_currency_var = tk.StringVar()
original_currency_var.set("USD")
input_currency_selection = tk.OptionMenu(main_window,original_currency_var,*currency_list)
input_currency_selection.grid(row = 1, column = 1,padx=10,pady=10)

output_currency_label = tk.Label(main_window, text = "Input Converted Currency",font=("Segoe UI",10))
output_currency_label.grid(row = 2, column = 0,padx=5,pady=5)

converted_currency_var = tk.StringVar()
converted_currency_var.set("THB")
output_currency_selection = tk.OptionMenu(main_window,converted_currency_var,*currency_list)
output_currency_selection.grid(row = 2, column = 1,padx=10,pady=10)

input_money_label = tk.Label(main_window, text = "Input Money",font=("Segoe UI",10))
input_money_label.grid(row = 1, column = 2,padx=10,pady=10)

input_money_entry = tk.Entry(main_window)
input_money_entry.grid(row = 1, column = 3,padx=10,pady=10)

converted_money_label = tk.Label(main_window, text = "Converted Money",font=("Segoe UI",10))
converted_money_label.grid(row = 2, column = 2,padx=10,pady=10)

converted_money_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
converted_money_output.grid(row = 2, column = 3,padx=10,pady=10)

sub_title_label = tk.Label(main_window, text = "Currency Converter and Analysis",font=("Segoe UI",15))
sub_title_label.grid(row = 5, column = 0,columnspan=5,padx=10,pady=10)

date_label = tk.Label(main_window, text = "Date",font=("Segoe UI",15))
date_label.grid(row = 6, column = 0,padx=10,pady=10)

date_output = tk.Label(main_window, text = today_str,font=("Segoe UI",15))
date_output.grid(row = 6, column = 1,padx=10,pady=10)

convert_currency_button = tk.Button(main_window,text="Convert Currency",command=convert_button_click)
convert_currency_button.grid(row=3, column=1,padx=5,pady=5)

difference_statistics_button = tk.Button(main_window,text="Difference and Statistics",command=compare_button_click)
difference_statistics_button.grid(row=6, column=3,padx=5,pady=5)

today_label = tk.Label(main_window, text = "Today",font=("Segoe UI",10))
today_label.grid(row = 7, column = 0,padx=10,pady=10)

today_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
today_output.grid(row = 8, column = 0,padx=10,pady=10)

yesterday_label = tk.Label(main_window, text = "Yesterday",font=("Segoe UI",10))
yesterday_label.grid(row = 7, column = 1,padx=10,pady=10)

yesterday_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
yesterday_output.grid(row = 8, column = 1,padx=10,pady=10)

two_days_ago_label = tk.Label(main_window, text = "2 Days ago",font=("Segoe UI",10))
two_days_ago_label.grid(row = 7, column = 2,padx=10,pady=10)

two_days_ago_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
two_days_ago_output.grid(row = 8, column = 2,padx=10,pady=10)

three_days_ago_label = tk.Label(main_window, text = "3 Days ago",font=("Segoe UI",10))
three_days_ago_label.grid(row = 7, column = 3,padx=10,pady=10)

three_days_ago_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
three_days_ago_output.grid(row = 8, column = 3,padx=10,pady=10)

min_value_label = tk.Label(main_window, text = "Min",font=("Segoe UI",10))
min_value_label.grid(row = 9, column = 0,padx=10,pady=10)

min_value_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
min_value_output.grid(row = 10, column = 0,padx=10,pady=10)

max_value_label = tk.Label(main_window, text = "Max",font=("Segoe UI",10))
max_value_label.grid(row = 9, column = 1,padx=10,pady=10)

max_value_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
max_value_output.grid(row = 10, column = 1,padx=10,pady=10)

average_value_label = tk.Label(main_window, text = "Average",font=("Segoe UI",10))
average_value_label.grid(row = 9, column = 2,padx=10,pady=10)

average_value_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
average_value_output.grid(row = 10, column = 2,padx=10,pady=10)

range_max_min_label = tk.Label(main_window, text = "Range",font=("Segoe UI",10))
range_max_min_label.grid(row = 9, column = 3,padx=10,pady=10)

range_max_min_output = tk.Label(main_window, text = "-",font=("Segoe UI",10))
range_max_min_output.grid(row = 10, column = 3,padx=10,pady=10)

main_window.mainloop()