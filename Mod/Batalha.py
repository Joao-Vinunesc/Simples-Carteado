import random
import Jogador as J, Biblioteca_cartas

#--Realmente necessario essa classe?
class Batalha():
    def __init__(self):
        pass
Biblioteca_cartas.Carta.montar_biblioteca(20)    
deck1, deck2=Biblioteca_cartas.Carta.montar_deck()
jogador1=J.Jogador(deck1)
jogador2=J.Jogador(deck2)

def fase_invocar(jogador):
    J.Jogador.mostrar_cartas(jogador,jogador.mao)
    carta=int(input(f'escolha uma carta para jogar ao campo\n'))
    J.Jogador.invocar_no_campo(jogador, jogador.mao[carta-1])
    J.Jogador.mostrar_cartas(jogador, jogador.campo)

def fase_ataque(jogador):
    if not jogador.campo:
        print('não há cartas no campo')
    carta=int(input('escolha uma carta do campo para atacar'))
    J.Jogador.selecionar_ataque(jogador)
    J.Jogador.mostrar_cartas(jogador, jogador.campo)



def turno(jogador1, jogador2):
    contador=1
    fim_jogo =False
    while fim_jogo == False:
        if contador == 1: #se primeiro turno: puxar a mão inicial
            jogador1.mao=J.Jogador.mao_inicial(jogador1,3)
            jogador2.mao=J.Jogador.mao_inicial(jogador2,3)
       
        #--inicia o turno com o jogador 1
        jogador1.mostrar_cartas(jogador1.mao)
        J.Jogador.fase_compra(jogador1)
        jogador1.mostrar_cartas(jogador1.mao)
        fase_invocar(jogador1)
        fase_ataque(jogador1)
        
        #-- jogar carta da mao para o campo -?

        fim_jogo=True

    turno_do = jogador1

    

turno(jogador1, jogador2)