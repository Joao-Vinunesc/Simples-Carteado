import random

class Batalha():
    def __init__(self):
        pass

 
    def mao_inicial(deck, inicio):
        selecao=[] 
            
        for iten in range(inicio):
            carta=random.choice(deck)
            selecao.append(carta)            
            deck.remove(carta)
        mao=[]
        mao.extend(selecao)
        return mao

    def fase_compra(deck, mao):
        carta = random.choice(deck)
        mao.append(carta)
        deck.remove(carta)
        return carta

    def fase_invocar(self, mao, campo):
        
        print("--FASE DE INVOCAÇÃO--")
        i=True        
        while i==True:
            #enquanto houver cartas para jogar:
            if len(mao) > 0:   

                escolha=input('Deseja jogar alguma carta para o campo?\n1-SIM\n2-NÃO - encerrar turno')
                if escolha == "1":
                    selecao=int(input('jogue uma carta:\n'))
                    carta=mao[selecao-1]
                    mao.remove(carta)
                    campo.append(carta)

                else:
                    print("Encerrando fase de invocação, continuando o jogo...")
                    i=False   
            else:
                print('não há cartas para jogar') 
                i=False

    def fase_ataque(self, campo):
        ataque=[]
        
        if len(campo) > 0:           

            while True:


                if len(campo) == 0: 
                    print('não há cartas no campo para jogar')
                    break

                selecao=int(input(f'\nselecione uma carta do CAMPO para atacar:\n'))
                carta=campo[selecao-1]
                campo.remove(carta)
                ataque.append(carta)


                escolha=input("confirmar o ataque?\n1-SIM\n2-NÃO")
                if escolha==2:
                    break
                else:
                    return ataque

    def calculo_dano(self, ataques, defesas):
        
        if defesas is None:
            print("não há cartas para Defesa")

        for carta_atk, carta_def in zip(ataques, defesas):
            carta_def.vida =- carta_atk.poder 
            if carta_def.vida <= 0:
                Batalha.descarte_p2.extend(carta_def)
                defesas.remove(carta_def)
                

                
                    
        else:
            print('não há cartas para jogar')
      
    def ataque_carta():
        pass    
    
    def rodada(deck):
        pass
    
    def mostrar_cartas(self,local):
        i=1
        for carta in local:
            print(f'{i}- {carta.nome} \n|{carta.poder}||{carta.vida}||{carta.efeito}|\n')
            i+=1
