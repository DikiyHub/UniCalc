import tkinter as tk
from tkinter import messagebox, ttk

# Galvenā aprēķinu loģika
# Funkcijas apraksts
def convert():
    try:
# Pārbauda, vai vērtība ir pozitīva
        if value <= 0:
            messagebox.showwarning('Brīdinājums', 'Lūdzu, ievadiet skaitli, kas lielāks par 0!')
            return

        category = combo_units.get()
        result = 0
        symbol = ''

        # Veikt konvertēšanu, pamatojoties uz izvēli
        if category == 'EUR uz USD':
            result = value * 1.08
            symbol = '$'
        elif category == 'USD uz EUR':
            result = value * 0.92
            symbol = '€'
        elif category == 'Metri uz Kilometriem':
            result = value / 1000
            symbol = 'km'
        elif category == 'Celsius uz Fahrenheit':
            result = (value * 9/5) + 32
            symbol = '°F'
        
        # Atjaunināt izvadi
        result_label.config(text=f'Rezultāts: {result:.2f} {symbol}')
        
    except ValueError:
        # Kļūdu apstrāde
        messagebox.showerror('Kļūda', 'Lūdzu, ievadiet derīgu skaitli!')

# Grafiskā interfeisa dizains
root = tk.Tk()
root.title('UniCalc v1.0')
root.geometry('350x450')
root.configure(bg='#f5f5f5')

# UI elementi
tk.Label(root, text='UniCalc', font=('Arial', 18, 'bold'), bg='#f5f5f5').pack(pady=20)

tk.Label(root, text='Ievadiet vērtību:', bg='#f5f5f5').pack()
entry_input = tk.Entry(root, font=('Arial', 12), justify='center')
entry_input.pack(pady=10)

tk.Label(root, text='Izvēlieties kategoriju:', bg='#f5f5f5').pack()
options = ['EUR uz USD', 'USD uz EUR', 'Metri uz Kilometriem', 'Celsius uz Fahrenheit']
combo_units = ttk.Combobox(root, values=options, state='readonly')
combo_units.pack(pady=10)
combo_units.current(0)

btn_convert = tk.Button(root, text='KONVERTĒT', command=convert, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
btn_convert.pack(pady=30)

result_label = tk.Label(root, text='Rezultāts: ', font=('Arial', 12), bg='#f5f5f5')
result_label.pack()

# Sākt pieteikšanos
if __name__ == '__main__':
    root.mainloop()
