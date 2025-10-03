import tkinter as tk
from tkinter import messagebox

def compare():
    try:
        value_one = float(entry_one.get())
        value_two = float(entry_two.get())
        if value_one > value_two:
            response.config(text=f'{value_one} es mayor que {value_two}', bg="green")
        elif value_one < value_two:
            response.config(text=f'{value_one} es menor que {value_two}', bg="red")
        else:
            response.config(text=f'{value_one} es igual a {value_two}', bg="blue")
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo valores númericos")

window = tk.Tk()
window.geometry("400x350")
window.title("Comparador de Valores")
window.resizable(False, False)

window.configure(bg='DodgerBlue2')

# Styles
label_style = {"bg": "light cyan", "fg": "#333", "font": ('Arial', 12, 'bold')}
entry_style = {"bg":"white", "fg":"blue", "font": ('Arial', 12, 'bold')}
button_style = {"bg":"SpringGreen2", "fg":"white", "font": ('Arial', 12, 'bold')}

label_one = tk.Label(window, text="Ingresa el primer número", **label_style)
label_one.pack(pady=5)

entry_one = tk.Entry(window, **entry_style)
entry_one.pack(pady=5)

label_two = tk.Label(window, text="Ingresa el segundo número", **label_style)
label_two.pack(pady=5)

entry_two = tk.Entry(window, **entry_style)
entry_two.pack(pady=5)

button = tk.Button(window, text="Comparar", command=compare, **button_style)
button.pack(pady=10)

# Etiqueta vacia para la respuesta
response = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="DodgerBlue2")
response.pack(pady=15)

window.mainloop()