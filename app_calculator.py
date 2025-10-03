import tkinter as tk
from tkinter import messagebox

def suma():
    try:
        n1, n2 = float(entry_one.get()), float(entry_two.get())
        response.config(text=f'La suma de {n1} y {n2} es: {n1 + n2}')
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")

def rest():
    try:
        n1, n2 = float(entry_one.get()), float(entry_two.get())
        response.config(text=f'La resta de {n1} y {n2} es: {n1 - n2}')
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")

def multp():
    try:
        n1, n2 = float(entry_one.get()), float(entry_two.get())
        response.config(text=f'La multiplicacion de {n1} y {n2} es: {n1 * n2}')
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")

def div():
    try:
        n1, n2 = float(entry_one.get()), float(entry_two.get())
        response.config(text=f'La division de {n1} y {n2} es: {(n1 /n2):.2f}')
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir para Cero")


window = tk.Tk()
window.geometry("400x300")
window.resizable(False, False)

label_one = tk.Label(window, text="Ingresa un primer número: ")
label_one.pack(pady=5)

entry_one = tk.Entry(window)
entry_one.pack(pady=5)


label_two = tk.Label(window, text="Ingresa un segundo número: ")
label_two.pack(pady=5)

entry_two = tk.Entry(window)
entry_two.pack(pady=5)

button_sum = tk.Button(text="+", command=suma)
button_sum.pack()

button_rest = tk.Button(text="-", command=rest)
button_rest.pack()

button_multp = tk.Button(text="*", command=multp)
button_multp.pack()

button_div = tk.Button(text="/", command=div)
button_div.pack()

response = tk.Label(window, text="")
response.pack()


window.mainloop()