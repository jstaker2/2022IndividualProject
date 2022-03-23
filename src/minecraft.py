from triviaMode import Trivia

class minecraft(Trivia):
    def __init__(self):
        questions = [
            "What does the piercing enchantment do?", 
            "Which of the following can be found in a bastion chest?",
            "What is the rarest color of axolotl?",
            "What do you name a sheep to make it a rainbow sheep?"
        ]
        possibleAnswers = [
            ["Makes a bow more durable", "Makes arrow give more knockback", "Deals more damage to mobs that spawn in water", "Lets the an arrow pass through multiple mobs"],
            ["Iron Ingots", "Lodestone", "Sponge", "Splash potion of speed"],
            ["Brown", "Blue", "Yellow", "White"],
            ["jeb_", "dinnerbone", "Notch", "ᓭ⍑ᒷᒷ!¡"]
        ]
        correctAnswers = [
            "Lets the an arrow pass through multiple mobs",
            "Lodestone",
            "Blue",
            "jeb_"
        ]
        super().__init__(questions, possibleAnswers, correctAnswers)