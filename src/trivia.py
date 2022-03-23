from typing import Text
import PySimpleGUI as sg
from harryPotter import harryPotter
from triviaMath import triviaMath
from minecraft import minecraft
from clash import clash


def mc(windowTitle, game, correct, qNum):
    for i, question in enumerate(game.getQuestions()):
        layout = [[sg.Text(game.getQuestions()[i])]] + [[sg.Radio(possAns, "RADIO1")] for possAns in game.getPossibleAnswers()[i]] +[[sg.Button("Submit")]]
        window = sg.Window(windowTitle, layout,margins=(500, 300))
        event, values = window.read()
        correctAnswer = game.correctAnswers[i]
        correctInd = game.possibleAnswers[i].index(correctAnswer)
        if event == "Submit" and values[correctInd] == True:
            sg.theme_background_color('green')
            correct += 1
            qNum += 1
            window.close()
        else:
            qNum += 1
            sg.theme_background_color('red')
    return correct, qNum

startLayout = [[sg.Text("Trivia game")], [sg.Button("Start")]]


# Create the window
window = sg.Window("Trivia Game", startLayout,margins=(500, 300))

event, values = window.read()
# End program if user closes window or
# presses the OK button
correct = 0 
qNum = 0
if event == "Start":
    modeLayout = [[sg.B("Harry Potter")], [sg.B("Minecraft")], [sg.B("Clash Royale")], [sg.B("Math")]]
    modeWindow = sg.Window("Choose your trivia mode", modeLayout, keep_on_top=True)
    modeEvent, modeValues = modeWindow.read()
    modeWindow.close()
    if modeEvent == "Harry Potter":
        hp = harryPotter()
        correct, qNum = mc("Harry Potter Trivia", hp,0,0)

    elif modeEvent == "Math":
        tm = triviaMath()
        correct, qNum = mc("Math Questions", tm,0,0)

    elif modeEvent == "Minecraft":
        minecraft = minecraft()
        correct, qNum = mc("Minecraft Trivia", minecraft,0,0)

    elif modeEvent == "Clash Royale":
        cr = clash()
        correct, qNum = mc("Clash Royale Trivia", cr,0,0)
    
    scoreLayout = [[sg.Text(str("You got: ") + str(correct) + str("/") + str(qNum))]]
    scoreWindow = sg.Window("Scores", scoreLayout, keep_on_top=True)
    scoreEvent, scoreValues = scoreWindow.read()
window.close()

