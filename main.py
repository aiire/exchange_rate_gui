import tkinter as tk
import os
import requests

def convert():
    api_key = "2bbe2b492e78ad7bdebc4b20"
    # api_key = os.environ['exchange_rates_api_key']
    message = None
    try:
        base_currency_code = base_entry.get().upper().strip()
        converting_currency_code = convert_entry.get().upper().strip()

        print(base_currency_code, converting_currency_code)

        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency_code}'

        response = requests.get(url)
        data = response.json()

        exchange_rate = float(data['conversion_rates'][converting_currency_code])

        currency_value = float(amount_entry.get())
        converted_currency_value = currency_value * exchange_rate

        message = f'{currency_value} {base_currency_code} = {converted_currency_value} {converting_currency_code}'
    except Exception as e:
        message = f'ERROR: {e}'

    output_label.config(text=message)
    print(message)

root = tk.Tk()

root.title("Exchange Rate Conversion")

root.geometry("300x400")

base_currency_prompt = tk.Label(root, text="Enter the base currency")
base_currency_prompt.pack()

base_entry = tk.Entry(root)
base_entry.pack()

converting_currency_prompt = tk.Label(root, text="Enter the converting currency")
converting_currency_prompt.pack()

convert_entry = tk.Entry(root)
convert_entry.pack()

base_currency_label_output = tk.Label(root, text="")
base_currency_label_output.pack()

output_label = tk.Label(root, text="")
output_label.pack()

amount_prompt = tk.Label(root, text="Enter the amount of money to convert")
amount_prompt.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

button = tk.Button(root, text="Convert", command=convert)
button.pack()

root.mainloop()
