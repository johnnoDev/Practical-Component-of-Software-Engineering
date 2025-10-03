import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("600x600")
window.title("Comparador de Valores")

label_one = tk.Label(window, text="Ingresa el primer número")
label_one.pack()

entry_one = tk.Entry(window)
entry_one.pack()

label_two = tk.Label(window, text="Ingresa el segundo número")
label_two.pack()

entry_two = tk.Entry(window)
entry_two.pack()

# Etiqueta vacia para la respuesta
response = tk.Label(window, text="", font=("Arial", 14, "bold"))
response.pack()

def compare():
    try:
        value_one = float(entry_one.get())
        value_two = float(entry_two.get())
            # .config() cambia propiedades del widget Label en tiempo real
        if value_one > value_two:
            response.config(text=f'{value_one} es mayor que {value_two}')
        elif value_one < value_two:
            response.config(text=f'{value_one} es menor que {value_two}')
        else:
            response.config(text=f'{value_one} es igual a {value_two}')
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")
        
button = tk.Button(window, text="Comparar", command=compare)
button.pack()

window.mainloop()