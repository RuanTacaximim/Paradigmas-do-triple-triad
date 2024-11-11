class carta():
    def __init__(self, name : str, classes: str, cima:int ,baixo:int ,esquerda:int ,direita:int , owner:str):
        
        self.name = name
        self.classes = classes
        self.cima = cima
        self.baixo = baixo
        self.esquerda = esquerda
        self.direita = direita
        self.owner = owner
       
    
class player():
    def __init__(self,name : str, deck: list, winner: bool, hand: list):
        self.name = name
        self.deck = deck
        self.hand = hand 
        self.winner = winner
        self.cartas_tomadas = 0

class table():
    def __init__(self, table_h: list, table_v: list, player_quantity: int):
        self.table_x = table_h
        self.table_y = table_v
        self.player_quantity = player_quantity

        