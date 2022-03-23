from triviaMode import Trivia

class triviaMath(Trivia):
    def __init__(self):
        questions = [
            "138 / 2", 
            "7 * 60",
            "12 + 7",
            "36 - 14"
        ]
        possibleAnswers = [
            ["68", "69", "70", "71"],
            ["340", "420", "270", "ur mum"],
            ["19", "21", "24", "5"],
            ["50", "12", "27", "22"]
        ]
        correctAnswers = [
            "69",
            "420",
            "19",
            "22"
        ]
        super().__init__(questions, possibleAnswers, correctAnswers)