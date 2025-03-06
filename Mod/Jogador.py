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