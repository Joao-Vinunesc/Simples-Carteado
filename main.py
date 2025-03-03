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

biblioteca_cartas = []

class Carta():
    def __init__(self, nome, poder, vida, efeito, arte):
        self.nome   = nome
        self.poder  = poder
        self.vida   = vida
        self.arte   = arte
        self.efeito = efeito
        biblioteca_cartas.append(self)

    def __str__(self):
        return f'\nCarta {self.nome} \nPoder:{self.poder}\nVida:{self.vida}\nEfeito:\n"{self.efeito}"'
    
class Jogador():
    def __init__(self, gemas):
        self.gemas = gemas
        self.deck=[]

class Batalha():
    def __init__(self, deck_p1, deck_p2):

        self.vida_p1 = 10        
        self.deck_p1 = deck_p1
        self.mao_p1  = Batalha.mao_inicial(deck_p1, 3)
        self.descarte_p1 =[]
        self.campo_p1=[]
        
        self.vida_p2 = 10
        self.deck_p2 = deck_p2
        self.mao_p2 = Batalha.mao_inicial(deck_p2, 3)
        self.descarte_p2 =[]
        self.campo_p2=[]

  
    def mao_inicial(deck, inicio):
        selecao=[] 
            
        for iten in range(inicio):
            carta=random.choice(deck)
            selecao.append(carta)            
            deck.remove(carta)
        mao=[]
        mao.extend(selecao)
        return mao

    def fase_compra(self, deck, mao):
        carta = random.choice(deck)
        mao.append(carta)
        deck.remove(carta)
        return carta

    def fase_invocar(self, mao, campo):
        i=True
        
        while i==True:
            #enquanto houver cartas para jogar:
            if len(mao) > 0:   
                escolha=input('Jogar carta no campo?\n 1-SIM\n2-NÃO - encerrar turno')
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
                break

            
                      


                

    def fase_ataque(self, campo):
        atacou=[]
        
        if len(campo) > 0:           

            while True:
                if len(campo) == 0: 
                    print('não há cartas no campo para jogar')
                    break
                print('CAMPO')
                batalha.mostrar_cartas(campo)
                print('ATAQUE:')
                batalha.mostrar_cartas(atacou)
                selecao=int(input(f'selecione uma carta do CAMPO para atacar:\n'))
                carta=campo[selecao-1]
                campo.remove(carta)
                atacou.append(carta)
                escolha=input("Confinuar o ataque?\n1-SIM\n2-NÃO")
                if escolha==2:
                    break
                else:
                    continue
                



        else:
            print('não há cartas para jogar')
    def rodada(deck):
        pass
    
    def mostrar_cartas(self,local):
        i=1
        for carta in local:
            print(f'{i}- {carta.nome} \n|{carta.poder}||{carta.vida}||{carta.efeito}|\n')
            i+=1

def montar_biblioteca(limite_deck):    
    for carta in range(limite_deck):
        nomes=["Cavaleiro ", "Duque ", "Menestrel ", "Heroi", "Bandido", "Paladino", "Justiceiro", "Lorde", "Guarda", "Arqueiro", "Rei"]
        nomesii=["do Abismo", "do vale dourado", "Celestial", "Abissal", "de Novanoite", "de Centiluz", "das Nove Fogueiras"]
        efeitos=["Destroi 1", "compra 1", "da 1 poder aliado", "da 2 de vida aliado", "reduz 1 poder inimigo", "reduz 2 poder inimigo", "Normal", "Normal", "Normal"]
        inome=random.choice(nomes)
        iinome=random.choice(nomesii)
        nome = f"{inome} {iinome}"
        poder=random.choice(range(5))
        vida=random.choice(range(6))
        arte="arte"
        efeito=random.choice(efeitos)
        carta =Carta(nome, poder, vida, efeito, arte) 

def montar_deck():
    deck_p1=[]
    deck_p2=[]
    for i in range(5):
        selecao=random.choice(biblioteca_cartas)
        deck_p1.append(selecao)

        selecao=random.choice(biblioteca_cartas)
        deck_p2.append(selecao)
    return deck_p1, deck_p2
       
montar_biblioteca(10)
deck_p1, deck_p2 = montar_deck()


#print(biblioteca_cartas)


i=True
batalha=Batalha(deck_p1, deck_p2)
while i ==True:    
    print(batalha.vida_p1)
    print(batalha.vida_p2)
    batalha.fase_compra(batalha.deck_p1, batalha.mao_p1)
    batalha.mostrar_cartas(batalha.mao_p1)
    batalha.fase_invocar(batalha.mao_p1, batalha.campo_p1)
    batalha.mostrar_cartas(batalha.campo_p1)
    batalha.fase_ataque(batalha.campo_p1)


    #for carta in batalha.mao_p1:
    #    print(f'{carta.nome} \n| {carta.poder} | {carta.vida} | {carta.efeito}\n')
    #batalha.fase_jogar(batalha.mao_p1)
    
   
   



    i = False

