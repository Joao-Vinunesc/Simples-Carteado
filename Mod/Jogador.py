import random
class Jogador():
    def __init__(self,  deck):
        self.gemas = 0
        self.deck= deck
        self.vida = 10 
        self.mao  = []
        self.descarte =[]
        self.campo=[]

    def __str__(self):
        deck=[]
        for carta in self.deck:
            deck.append(carta.nome)

        return f'Vida{self.vida},\n Mão:{self.mao}\n deck:{deck}'

    
    def mao_inicial(self, inicio):
        mao=[]
        for item in range(inicio):
            carta=random.choice(self.deck)
            mao.append(carta)            
            self.deck.remove(carta)
        return mao

    def fase_compra(self):
        carta = random.choice(self.deck)
        self.mao.append(carta)
        self.deck.remove(carta)
    
    #--Necessario iniciar a função com a entrada da carta escolhida da mão!
    def invocar_no_campo(self,carta):
        self.mao.remove(carta)
        self.campo.append(carta)
    
    #--Seleciona as carta dentro do CAMPO para o ataque | Retorna lista com as cartas para o ataque
    def selecionar_ataque(self):
        grupo_ataque=[]
        for carta in self.campo:
            input(f'Colocar {carta.nome}|{carta.poder}|{carta.vida} no grupo de ataque?')
            #--Colocar futuramente uma condicional aqui para selecionar quais cartas serão adicionadas
            grupo_ataque.append(carta)
        return(grupo_ataque)




