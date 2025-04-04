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

def texto_combate(atacante,defensor, dano_ao_atk, dano_ao_def):
    print(f'{atacante.nome}|{atacante.poder}|{atacante.vida} ataca {defensor.nome}|{defensor.poder}|{defensor.vida}')
    print(f'{atacante.nome}|{atacante.poder}|{atacante.vida} sofreu {dano_ao_atk} de dano')
    print(f'{defensor.nome}|{defensor.poder}|{defensor.vida} sofreu {dano_ao_def} de dano\n')

    if dano_ao_atk >= 1:
        print(f'{atacante.nome} recebeu {dano_ao_atk}dano')
    if dano_ao_def >= 1:
        print(f'{defensor.nome} recebeu {dano_ao_def}dano\n')

#Lista com jogador+grupo de ataque | jogador2+grupo de defesa
def calculo_batalha(grupo_ataque,grupo_defesa ):
    """ problemas:.
        as cartas removidas não são removidas de fato do campo do jogador
        a função é enorme e precisa ser refatorada"""
    if not grupo_defesa[0]:
        print('não tem cartas no grupo de defesa') 
        #caso vazio - dano direto a vida do jogador
        
        for atacante in grupo_ataque[0]:
            print(f'Vida restante:{grupo_defesa[1].vida}')
            grupo_defesa[1].vida -=atacante.poder 

            print(f'Sem defesas! {atacante.nome} causa {atacante.poder} de dano a vida do Jogador2')
            print(f'Vida restante:{grupo_defesa[1].vida}')
            
    else:
        # - Caso o numero de atacantes e defensores seja igual:
        for atacante, defensor in zip(grupo_ataque[0], grupo_defesa[0]):            
            dano_ao_def= atacante.poder          
            dano_ao_atk= defensor.poder 

            texto_combate(atacante, defensor, dano_ao_atk, dano_ao_def)
            
            defensor.vida =defensor.vida-dano_ao_def
            atacante.vida =atacante.vida-dano_ao_atk

            remover_j1=[]
            remover_j2=[]
            if atacante.vida <= 0:
                print(f'{atacante.nome} foi destruido')
                grupo_ataque.remove(atacante)
                remover_j1.append(atacante)
            if defensor.vida <=0:
                print(f'{defensor.nome} foi destruido')
                grupo_defesa.remove(defensor)
                remover_j2.append(defensor)
            jogador1_resultado =[grupo_ataque, remover_j1]
            jogador2_resultado =[grupo_defesa, remover_j2]

        return jogador1_resultado, jogador2_resultado

def resolucao_batalha(jogador1,jogador1_resultado, jogador2, jogador2_resultado):
    for carta in jogador1_resultado[0]:
        jogador1.campo.append(carta)

def fase_ataque(jogador_atk, jogador_def):
    carta=int(input('escolha uma carta do campo para atacar'))    
    J.Jogador.mostrar_cartas(jogador_atk, jogador_atk.campo)

    grupo_ataque=[J.Jogador.selecionar_ataque(jogador_atk),jogador_atk]
    
    grupo_defesa=[J.Jogador.selecionar_defesa(jogador_def), jogador_def]

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
#grupo_atk=J.Jogador.mao_inicial(jogador1,3)
#grupo_def=J.Jogador.mao_inicial(jogador2,3)
#grupo_ataque, grupo_defesa, remover_j1, remover_j2= calculo_batalha(grupo_atk,grupo_def)



turno(jogador1, jogador2)