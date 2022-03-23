from triviaMode import Trivia
from clashCards import cards
import random

class clash(Trivia):

    def __init__(self):

        knight = cards(3, "Common", "Troop", "Knight")
        bowler = cards(5, "Epic", "Troop", "Bowler")
        zap = cards(2, "Common", "Spell", "Zap")
        log = cards(2, "Legendary", "Spell", "Log")
        tesla = cards(4, "Common", "Building", "Tesla")

        cardList = [
            knight,
            bowler,
            zap,
            log,
            tesla
        ]

        card1 = random.sample(cardList, 1)[0]
        card2 = random.sample(cardList, 1)[0]
        card3 = random.sample(cardList, 1)[0]

        questions = [
            "What is the elixir cost of "+ str(card1.getName()), 
            "What is the rarity of "+ str(card2.getName()),
            "What card type is "+ str(card3.getName())
        ]
        possibleAnswers = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["Common", "Rare", "Epic", "Legendary"],
            ["Troop", "Spell", "Building"]
        ]
        correctAnswers = [
            str(card1.elixir),
            str(card2.rarity),
            str(card3.cardType)
        ]
        super().__init__(questions, possibleAnswers, correctAnswers)