class carta():
    def __init__(self, name : str, clases: str, cima:int ,baixo:int ,esquerda:int ,direita:int , owner:str):
        
        self.name = name
        self.clases = clases
        self.cima = cima
        self.baixo = baixo
        self.esquerda = esquerda
        self.direita = direita
        self.owner = owner
       
    
class player():
    def __init__(self,name : str, deck: list, winner: bool):
        self.name = name
        self.deck = deck
        self.winner = winner
        self.cartas_tomadas = 0
