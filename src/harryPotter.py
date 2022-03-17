from triviaMode import Trivia

class harryPotter(Trivia):
    def __init__(self):
        questions = [
            "Which is a horcrux?", 
            "Which wood is Harry's wand made out of?",
            "What did Humphrey Belcher decide the time was ripe for?"
        ]
        possibleAnswers = [
            ["The Portkey Shoe", "The Triwizard Cup", "The Locket", "Quidditch Through The Ages"],
            ["Oak", "Holly", "Elder", "Spruce"],
            ["Spiked Felix Felicis", "Self Aware Pigmy Puff", "WWE Level Punching Telescope", "A Cheese Cauldron"]
        ]
        correctAnswers = [
            "The Locket",
            "Holly",
            "A Cheese Cauldron"
        ]
        super().__init__(questions, possibleAnswers, correctAnswers)