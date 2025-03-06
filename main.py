'''
Quais serão os elementos de batalha?
    -> Mãos de 3 cartas
    -> decks com 20 cartas
    -> cartas podem ter efeitos

Quais mecanicas vão ser usadas?    
    -> Poder abate valor de vida
    -> caso a carta venha a 0 de vida ela é enviada para o descarte
    -> Cada jogador deve ter entre 10 à 20 de vida

Condições de Vitoria:
    -> o primeiro jogador que chegar a 0 ou menos de vida é considerado perdedor
    -> o primeiro jogador que chegar a 0 cartas é considerado perdedor

Há algum fator de repetição(replay)?
    ->Cartas Serão geradas aleatoriamente
    -> A cada vitoria o jogador receberar uma quantidade de gemas que poderar usar para gerar novas cartas.



'''
import random
import os
from Mod import Batalha
from Mod import Biblioteca_cartas
from Mod import Jogador




        

def exibir_campo(campo):
    print(f'-----------CAMPO------------')
    print(''.join(f'[{carta.nome}]-' for carta in campo))
    print(f'----------------------------\n')

def exibir_ataque(ataque):
    print(f'----------ATAQUE------------')
    print(''.join(f'[{carta.nome}]-' for carta in ataque))
    print(f'----------------------------\n')

def exibir_mao(mao):
    print(f'-----------MAO--------------')
    print(''.join(f'[{carta.nome}]-' for carta in mao))
    print(f'----------------------------\n')

def limpar_tela():
    # Verifica o sistema operacional e executa o comando correspondente
   
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')


#CRIAÇÃO DA BASE DE CARTAS ALEATORIAS#
Biblioteca_cartas.Carta.montar_biblioteca(10)
deck_p1, deck_p2 = Biblioteca_cartas.Carta.montar_deck()
#------------------------------------#

#----------TESTE DE BATALHA----------#

i=True

while i ==True:   
    jogador_1=Jogador.Jogador(deck_p1) 
    jogador_2=Jogador.Jogador(deck_p2)

    print(jogador_1)
    
    1
    i = False


    #for carta in batalha.mao_p1:
    #    print(f'{carta.nome} \n| {carta.poder} | {carta.vida} | {carta.efeito}\n')
    #batalha.fase_jogar(batalha.mao_p1)
    
   
   



 

