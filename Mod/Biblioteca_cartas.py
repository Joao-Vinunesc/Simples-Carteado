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
    
    
    def montar_biblioteca(limite_deck):  

        for carta in range(limite_deck):
            nomes=["Cavaleiro ", "Duque ", "Menestrel ", "Heroi", "Bandido", "Paladino", "Justiceiro", "Lorde", "Guarda", "Arqueiro", "Rei"]
            nomesii=["do Abismo", "do vale dourado", "Celestial", "Abissal", "de Novanoite", "de Centiluz", "das Nove Fogueiras"]
            efeitos=["Destroi 1", "compra 1", "da 1 poder aliado", "da 2 de vida aliado", "reduz 1 poder inimigo", "reduz 2 poder inimigo", "Normal", "Normal", "Normal"]
            inome=random.choice(nomes)
            iinome=random.choice(nomesii)
            nome = f"{inome} {iinome}"
            poder=random.choice(range(5))
            vida=random.choice(range(1,6))            
            arte="arte"
            efeito=random.choice(efeitos)
            carta =Carta(nome, poder, vida, efeito, arte) 

    def montar_deck():
        deck_p1=[]
        deck_p2=[]
        for i in range(20):
            selecao=random.choice(biblioteca_cartas)
            deck_p1.append(selecao)

            selecao=random.choice(biblioteca_cartas)
            deck_p2.append(selecao)
        return deck_p1, deck_p2
