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
    def __init__(self,name : str, deck: list, winner: bool, hand: list):
        self.name = name
        self.deck = deck
        self.hand = hand 
        self.winner = winner
        self.cartas_tomadas = 0

class table():
    def __init__(self, table_x: list, table_y: list, player_quantity: int):
        self.table_x = table_x
        self.table_y = table_y
        self.player_quantity = player_quantity

        