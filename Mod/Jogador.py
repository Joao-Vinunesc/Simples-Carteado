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
            if not self.deck:
                print("deck vazio")
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
        if not self.campo:
            print('não há cartas no campo')
        else:
            grupo_ataque=[]
            for carta in self.campo:
                input(f'Colocar {carta.nome}|{carta.poder}|{carta.vida} no grupo de ataque?')
                #--Colocar futuramente uma condicional aqui para selecionar quais cartas serão adicionadas
                grupo_ataque.append(carta)
                
        return(grupo_ataque)
    
    def selecionar_defesa(self):
        grupo_defesa = []
        if not self.campo: #caso não tenha defesa o ataque é direto ao pv do jogador
            print('não há cartas para defesa')
        else: #futuramente colocar opção do defensor escolher quem vai defender.
            for carta in self.campo:
                grupo_defesa.append(carta)    
        return grupo_defesa
        


    #--Mostra as cartas de um grupo, Nescessario passar o grupo ex: mao_p1|
    def mostrar_cartas(self,local):
        i=1
        for carta in local:
            print(f'{i}- {carta.nome} \n|{carta.poder}||{carta.vida}||{carta.efeito}|\n')
            i+=1


