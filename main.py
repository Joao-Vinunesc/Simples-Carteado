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

#espada=Carta('espada', 2, 0, 'ataca', 'arte.png')

def montar_deck(deck):
    
    for carta in range(deck):
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



class Jogador():
    def __init__(self, gemas):
        self.gemas = gemas
    

        


montar_deck(5)
for carta in biblioteca_cartas:
    print(carta)


