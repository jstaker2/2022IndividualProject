import PySimpleGUI as sg
from harryPotter import harryPotter

startLayout = [[sg.Text("Trivia game")], [sg.Button("Start")]]


# Create the window
window = sg.Window("Trivia Game", startLayout,margins=(500, 300))

event, values = window.read()
# End program if user closes window or
# presses the OK button
if event == "Start":
    modeLayout = [[sg.B("Harry Potter")], [sg.B("Pokémon")], [sg.B("Clash Royale")], [sg.B("Math")]]
    modeEvent, modeValues = sg.Window("Choose your trivia mode", modeLayout, keep_on_top=True).read()
    if modeEvent == "Harry Potter":
        hp = harryPotter()
        for i, question in enumerate(hp.getQuestions()):
            hpLayout = [[sg.Text(hp.getQuestions()[i])]] + [[sg.Radio(possAns, "RADIO1")] for possAns in hp.getPossibleAnswers()[i]] +[[sg.Button("Submit")]]
            hpWindow = sg.Window("Harry Potter", hpLayout,margins=(500, 300))
            hpEvent, hpValues = hpWindow.read()
            correctAnswer = hp.correctAnswers()[i]
            correctInd = hp.possibleAnswers()[i].index(correctAnswer)
            if hpEvent == "Submit" and hpValues[correctInd] == True:
                sg.theme_background_color('green')
                hpWindow.close()
window.close()