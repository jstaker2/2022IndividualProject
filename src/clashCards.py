class cards():
    def __init__(self, elixir: int, rarity: str, cardType: str, name: str):
        self.elixir = elixir
        self.rarity = rarity
        self.cardType = cardType
        self.name = name

    def getElixir(self):
        return self.elixir

    def getRarity(self):
        return self.rarity

    def getCardType(self):
        return self.cardType

    def getName(self):
        return self.name