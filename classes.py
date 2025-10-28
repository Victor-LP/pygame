#definindo as classes do jogo
class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 5
        self.mana = 50
        self.velocidade = 5
    def atacar(self,Inimigo):
        Inimigo.vida -= self.ataque

class Zumbi:
    def __init__(self,nivel):
        self.nivel = nivel
        #os atributos são proporcionais ao nível
        self.vida = round(15*(1+(nivel*3/10)))
        self.ataque = round(5*(1+(nivel*3/10)))
        self.velocidade = round(2*(1+(nivel*2/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Esqueleto:
    def __init__(self,nivel):
        self.nivel = nivel
        self.vida = round(10*(1+(nivel*2/10)))
        self.ataque = round(5*(1+(nivel*3/10)))
        self.velocidade = round(3*(1+(nivel*3/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Morcego:
    def __init__(self,nivel):
        self.nivel = nivel
        self.vida = round(3*(1+(nivel*2/10)))
        self.ataque = round(3*(1+(nivel*2/10)))
        self.velocidade = round(5*(1+(nivel*4/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Chefao:
    def __init__(self,nivel):
        self.nivel = nivel
        self.vida = 100 + nivel * 20
        self.ataque = 15 + nivel * 5
        self.velocidade = 4 + nivel
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque