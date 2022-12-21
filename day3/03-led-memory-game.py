from machine import Pin
import time
import random
import sys

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
greenButton = Pin(13, Pin.IN, Pin.PULL_DOWN)
amberButton = Pin(8, Pin.IN, Pin.PULL_DOWN)
redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
greenLed = Pin(18, Pin.OUT)
amberLed = Pin(19, Pin.OUT)
redLed = Pin(20, Pin.OUT)

level = {
    'e': 4,
    'n': 6,
    'h': 8
}

led = {
    'green': greenLed,
    'amber': amberLed,
    'red': redLed
}

def chooseDifficulty():
    difficulty = input('Choose a difficulty, easy, normal, hard: (e,n,h) ')
    while difficulty not in ('e', 'n', 'h'):
        difficulty = input('You can only choose e,n,h: ')
    
    return difficulty

def generatePattern(difficulty):
    choices = ['green', 'amber', 'red']
    pattern = []

    for n in range(level[difficulty]):
        pattern.append(random.choice(choices))
        
    print(pattern)
    return pattern

def toggleLed(light):
    led[light].toggle()
    time.sleep(1)
    led[light].toggle()
    time.sleep(0.5)

def showPattern(pattern):
    for x in pattern:
        toggleLed(x)
        
def lose():
    for i in range(3):
        redLed.toggle()
        amberLed.toggle()
        greenLed.toggle()
        time.sleep(0.5)
        redLed.toggle()
        amberLed.toggle()
        greenLed.toggle()
        time.sleep(0.5)
    
def win():
    for i in range(20):
        redLed.value(1)
        time.sleep(0.1)
        redLed.value(0)
        amberLed.value(1)
        time.sleep(0.1)
        amberLed.value(0)
        greenLed.value(1)
        time.sleep(0.1)
        greenLed.value(0)
        time.sleep(0.1)
        amberLed.value(1)
        time.sleep(0.1)
        amberLed.value(0)  

def checkGuess(playerGuess, light, loopNum, pattern):
    if pattern[loopNum] != light:
        lose()
        sys.exit()
    elif playerGuess == pattern:
        win()
        sys.exit()

def playGame():
    guess = []
    i = 0
   
    difficulty = chooseDifficulty()
    patternToGuess = generatePattern(difficulty)
    showPattern(patternToGuess)

    while True:
        time.sleep(0.5) # Short delay
                
        if greenButton.value() == 1:
            toggleLed('green')
            guess.append('green')
            checkGuess(guess, 'green', i, patternToGuess)
            i += 1

        elif amberButton.value() == 1:
            toggleLed('amber')
            guess.append('amber')
            checkGuess(guess, 'amber', i, patternToGuess)
            i += 1

        elif redButton.value() == 1:
            toggleLed('red')
            guess.append('red')
            checkGuess(guess, 'red', i, patternToGuess)
            i += 1

playGame()
