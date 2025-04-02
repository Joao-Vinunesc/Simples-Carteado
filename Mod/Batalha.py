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

def calculo_batalha(grupo_ataque,grupo_defesa ):
    """ problemas:
        em dados momentos o calculo não é feito de maneira correta gerando interações
        onde as cartas ganham vida ao inves de perder.
        as cartas removidas não são removidas de fato do campo do jogador
        a função é enorme e precisa ser refatorada"""
    if not grupo_defesa:
        print('não tem cartas no grupo de defesa') 
    else:
        for atacante, defensor in zip(grupo_ataque, grupo_defesa):
            #-- a ideia é que tanto o defensor quanto o atacante troquem danos.
            dano_ao_def= atacante.poder - defensor.poder
            # 4|5 - 1|1
            dano_ao_atk= defensor.poder - atacante.poder

            if dano_ao_atk <= 0:
                dano_ao_atk == 0
            elif dano_ao_def <= 0:
                dano_ao_def==0   
            
            defensor.vida =-dano_ao_def
            print(f'{atacante.nome}|{atacante.poder}|{atacante.vida} ataca {defensor.nome}|{defensor.poder}|{defensor.vida}')
            print(f'{atacante.nome}|{atacante.poder}|{atacante.vida} sofreu {dano_ao_atk} de dano')
            print(f'{defensor.nome}|{defensor.poder}|{defensor.vida} sofreu {dano_ao_def} de dano')
            atacante.vida= atacante.vida -dano_ao_atk
            print(f'{atacante.nome} agr possui {atacante.vida}!')
            print(f'{defensor.nome} agr possui {atacante.vida}!')

            if atacante.vida <= 0:
                print(f'{atacante.nome} foi destruido')
                grupo_ataque.remove(atacante)
            elif defensor.vida <=0:
                print(f'{defensor.nome} foi destruido')
                grupo_defesa.remove(defensor)
                   
    J.Jogador.mostrar_cartas(grupo_ataque,grupo_ataque)
    J.Jogador.mostrar_cartas(grupo_defesa,grupo_defesa)
    print('f')

def fase_ataque(jogador_atk, jogador_def):
    carta=int(input('escolha uma carta do campo para atacar'))    
    J.Jogador.mostrar_cartas(jogador_atk, jogador_atk.campo)

    grupo_ataque=J.Jogador.selecionar_ataque(jogador_atk)
    
    grupo_defesa=J.Jogador.selecionar_defesa(jogador_def)

    calculo_batalha(grupo_ataque, grupo_defesa)

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
        fase_ataque(jogador1, jogador2)
        
        #-- jogar carta da mao para o campo -?

        fim_jogo=True

    turno_do = jogador1

    
#---ZONA DE TESTE---#
grupo_atk=J.Jogador.mao_inicial(jogador1,3)
grupo_def=J.Jogador.mao_inicial(jogador2,3)
calculo_batalha(grupo_atk,grupo_def)
#turno(jogador1, jogador2)