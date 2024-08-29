import tkinter as tk
from tkinter import messagebox
import math

# Função para calcular a expressão
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Função para calcular a raiz quadrada
def calcular_raiz_quadrada():
    try:
        resultado = math.sqrt(float(entrada.get()))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para inserir valores no campo de entrada
def clicar_botao(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + valor)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.geometry("420x600")
root.resizable(False, False)  # Impede de redimensionar a janela

# Campo de texto para a entrada da expressão
entrada = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Lista com os botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1)  # Botões de limpar (C) e raiz quadrada (√)
]

# Cria os botões na interface
for (texto, linha, coluna) in botoes:
    if texto == '=':
        action = calcular
    elif texto == 'C':
        action = limpar
    elif texto == '√':
        action = calcular_raiz_quadrada
    else:
        action = lambda x=texto: clicar_botao(x)
    tk.Button(root, text=texto, width=5, height=3, command=action, font=('Arial', 18)).grid(row=linha, column=coluna, padx=5, pady=5)

# Rodar o loop principal da aplicação
root.mainloop()
