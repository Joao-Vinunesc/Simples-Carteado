import tkinter as tk
def botao():
    lista=[1,2,3,4]
    for item in lista:
        item=tk.Tk()

tela =tk.Tk()
tela.title("teste")
tela.geometry("650x650")
def campop1():
    """
       0 [ ]-[ ]-[ ]-[ ]-[ ]
       1 [ ]-[ ]-[ ]-[ ]-[ ]
       2
       3 [x]-[x]-[x]-[x]-[x]
       4 [ ]-[ ]-[ ]-[ ]-[ ]
          0   1   2   3   4
    """
    slot_campo1=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo1.grid(row=3, column=0, padx=5)

    slot_campo2=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo2.grid(row=3, column=1, padx=5)

    slot_campo3=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo3.grid(row=3, column=2, padx=5)

    slot_campo4=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo4.grid(row=3, column=3, padx=5)

    slot_campo5=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo5.grid(row=3, column=4, padx=5)

def maop1():
    """
       0 [ ]-[ ]-[ ]-[ ]-[ ]
       1 [ ]-[ ]-[ ]-[ ]-[ ]
       2
       3 [ ]-[ ]-[ ]-[ ]-[ ]
       4 [x]-[x]-[x]-[x]-[x]
          0   1   2   3   4
    """
    push_button =  tk.Button(tela, text="cartas", command= botao)
    push_button.grid(row=0, column=0, padx=5, pady=10)

    slot_mao1=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao1.grid(row=4, column=0, padx=5, pady=10)

    slot_mao2=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao2.grid(row=4, column=1, padx=5, pady=10)

    slot_mao3=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao3.grid(row=4, column=2, padx=5, pady=10)

    slot_mao4=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao4.grid(row=4, column=3, padx=5, pady=10)

    slot_mao5=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao5.grid(row=4, column=4, padx=5, pady=10)

def meio():
    slot_meio1=tk.Frame(tela, width=100, height=100)
    slot_meio1.grid(row=5, column=0, padx=5, pady=10)

    slot_meio2=tk.Frame(tela, width=100, height=100)
    slot_meio2.grid(row=5, column=1, padx=5, pady=10)

    slot_meio3=tk.Frame(tela, width=100, height=100)
    slot_meio3.grid(row=5, column=2, padx=5, pady=10)

    slot_meio4=tk.Frame(tela, width=100, height=100)
    slot_meio4.grid(row=5, column=3, padx=5, pady=10)

    slot_meio5=tk.Frame(tela, width=100, height=100)
    slot_meio5.grid(row=5, column=4, padx=5, pady=10)

def campop2():

    slot_campo_p21=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo_p21.grid(row=7, column=0, padx=5)

    slot_campo_p22=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo_p22.grid(row=7, column=1, padx=5)

    slot_campo_p23=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo_p23.grid(row=7, column=2, padx=5)

    slot_campo_p24=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo_p24.grid(row=7, column=3, padx=5)

    slot_campo_p25=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_campo_p25.grid(row=7, column=4, padx=5)


def maop2():
    slot_mao_p21=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao_p21.grid(row=8, column=0, padx=5, pady=10)

    slot_mao_p22=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao_p22.grid(row=8, column=1, padx=5, pady=10)

    slot_mao_p23=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao_p23.grid(row=8, column=2, padx=5, pady=10)

    slot_mao_p24=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao_p24.grid(row=8, column=3, padx=5, pady=10)

    slot_mao_p25=tk.Frame(tela, width=100, height=100, bg="grey")
    slot_mao_p25.grid(row=8, column=4, padx=5, pady=10)

campop1()
maop1()
meio()
campop2()
maop2()
tela.mainloop()

""" Para o caso de esquecer como label e grid funcionam:
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Exemplo de Grid")

    # Adicionando widgets ao grid
    label1 = tk.Label(janela, text="Nome:")
    label1.grid(row=0, column=0, padx=10, pady=5)  # Linha 0, Coluna 0

    entry1 = tk.Entry(janela)
    entry1.grid(row=0, column=1, padx=10, pady=5)  # Linha 0, Coluna 1

    label2 = tk.Label(janela, text="Senha:")
    label2.grid(row=1, column=0, padx=10, pady=5)  # Linha 1, Coluna 0

    entry2 = tk.Entry(janela, show="*")
    entry2.grid(row=1, column=1, padx=10, pady=5)  # Linha 1, Coluna 1

    botao = tk.Button(janela, text="Entrar", command=lambda: print("Botão clicado!"))
    botao.grid(row=2, column=0, columnspan=2, pady=10)  # Ocupa duas colunas

    # Executando a interface gráfica
    janela.mainloop()"

"""