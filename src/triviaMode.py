class Trivia:

    def __init__(self, questions:list[str], possibleAnswers:list[list[str]], correctAnswers:list[str]):
        self.questions = questions
        self.possibleAnswers = possibleAnswers
        self.correctAnswers = correctAnswers

    def getQuestions(self):
        return self.questions

    def getPossibleAnswers(self):
        return self.possibleAnswers

    def getCorrectAnswers(self):
        return self.correctAnswers