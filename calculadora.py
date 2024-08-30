import tkinter as tk
from tkinter import messagebox
import math

# funçao para calcular a expressao
def calculate():
    try:
        result = eval(ent.get())
        ent.delete(0, tk.END)
        ent.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "entrada invalida")

# funçao para limpar a entrada
def clean():
    ent.delete(0, tk.END)

# Funçao para calcular a raiz quadrada
def calculate_quadratic():
    try:
        result = math.sqrt(float(ent.get()))
        ent.delete(0, tk.END)
        ent.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "entrada invalida")

# funçao para inserir valores no campo de entrada
def click(val):
    atual = ent.get()
    ent.delete(0, tk.END)
    ent.insert(tk.END, atual + val)

# criar a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.geometry("420x600")
root.resizable(False, False)  # impede de redimensionar a janela

# campo de texto para a entrada da expressao
ent = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# lista com os botoes da calculadora
btns = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1) 
]

# cria os botoes na interface
for (txt, line, col) in btns:
    if txt == '=':
        action = calculate
    elif txt == 'C':
        action = clean
    elif txt == '√':
        action = calculate_quadratic
    else:
        action = lambda x=txt: click(x)
    tk.Button(root, text=txt, width=5, height=3, command=action, font=('Arial', 18)).grid(row=line, column=col, padx=5, pady=5)

#rodar o loop principal da aplicaçao
root.mainloop()
