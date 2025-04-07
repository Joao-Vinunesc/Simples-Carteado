import random
import Jogador as J, Biblioteca_cartas


Biblioteca_cartas.Carta.montar_biblioteca(60)    
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

def atacante_par_defensor(grupo_ataque, grupo_defesa):
    #Lista com jogador1+grupo de ataque | jogador2+grupo de defesa
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
                remover_j1.append(atacante)
            if defensor.vida <=0:
                print(f'{defensor.nome} foi destruido')                
                remover_j2.append(defensor)

            for eliminado in remover_j1:
                grupo_ataque[0].remove(eliminado)
            for eliminado in remover_j2:
                grupo_defesa[0].remove(eliminado)
                
            jogador1_resultado =[grupo_ataque, remover_j1]
            jogador2_resultado =[grupo_defesa, remover_j2]
            return jogador1_resultado, jogador2_resultado

#Lista com jogador1+grupo de ataque | jogador2+grupo de defesa
def calculo_batalha(grupo_ataque,grupo_defesa ):

    #quando não há defesas
    if not grupo_defesa[0]:
        print('não tem cartas no grupo de defesa') 
        #caso vazio - dano direto a vida do jogador
        for atacante in grupo_ataque[0]:
            print(f'Vida restante:{grupo_defesa[1].vida}')
            grupo_defesa[1].vida -=atacante.poder 

            print(f'Sem defesas! {atacante.nome} causa {atacante.poder} de dano a vida do Jogador2')
            print(f'Vida restante:{grupo_defesa[1].vida}')

    #quando há mais atacantes que defensores
    if len(grupo_ataque[0]) > len(grupo_defesa[0]):
        print('dispar atacante/defensor')
        atacante_par_defensor(grupo_ataque, grupo_defesa)
        for atacante in grupo_ataque[0][len(grupo_defesa[0]):]:
            print(f'Vida restante:{grupo_defesa[1].vida}')
            grupo_defesa[1].vida -=atacante.poder 

            print(f'Sem defesas! {atacante.nome} causa {atacante.poder} de dano a vida do Jogador2')
            print(f'Vida restante:{grupo_defesa[1].vida}')

        
    
    else:
        # - Caso o numero de atacantes e defensores seja igual:
        atacante_par_defensor(grupo_ataque, grupo_defesa)

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
            jogador2.campo=J.Jogador.mao_inicial(jogador2,1)
       
        #--inicia o turno com o jogador 1
        jogador1.mostrar_cartas(jogador1.mao)        
        J.Jogador.fase_compra(jogador1)
        jogador1.mostrar_cartas(jogador1.mao)
        fase_invocar(jogador1)
        fase_ataque(jogador1, jogador2)

        #--Turno do jogador 2
        jogador2.mostrar_cartas(jogador2.mao)
        J.Jogador.fase_compra(jogador2)
        jogador2.mostrar_cartas(jogador2.mao)
        fase_invocar(jogador2)
        fase_ataque(jogador2,jogador1)
        
        
        #-- jogar carta da mao para o campo -?
        if jogador1.vida == 0:
            print(f'{jogador2} Venceu!')
            fim_jogo=True
        elif jogador2.vida ==0:
            print(f'{jogador1} Venceu')
            fim_jogo=True
    2


    
#---ZONA DE TESTE---#
#grupo_atk=J.Jogador.mao_inicial(jogador1,3)
#grupo_def=J.Jogador.mao_inicial(jogador2,3)
#grupo_ataque, grupo_defesa, remover_j1, remover_j2= calculo_batalha(grupo_atk,grupo_def)


print(len(deck1))
turno(jogador1, jogador2)