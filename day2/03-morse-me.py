from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

code_dict = {
    'A':'.- ',
    'B':'-... ',
    'C':'-.-. ',
    'D':'-.. ',
    'E':'. ',
    'F':'..-. ',
    'G':'--. ',
    'H':'.... ',
    'I':'.. ',
    'J':'.--- ',
    'K':'-.- ',
    'L':'.-.. ',
    'M':'-- ',
    'N':'-. ',
    'O':'--- ',
    'P':'.--. ',
    'Q':'--.- ',
    'R':'.-. ',
    'S':'... ',
    'T':'- ',
    'U':'..- ',
    'V':'...- ',
    'W':'.-- ',
    'X':'-..- ',
    'Y':'-.-- ',
    'Z':'--.. ',
    '1':'.---- ',
    '2':'..--- ',
    '3':'...-- ',
    '4':'....- ',
    '5':'..... ',
    '6':'-.... ',
    '7':'--... ',
    '8':'---.. ',
    '9':'----. ',
    '0':'----- ',
    ',':'--..-- ',
    '.':'.-.-.- ',
    '?':'..--.. ',
    '/':'-..-. ',
    '-':'-....- ',
    '(':'-.--. ',
    ')':'-.--.- '
    }

def dotOnOff():
    red.value(1)
    amber.value(1)
    green.value(1)
    time.sleep(1)
    red.value(0)
    amber.value(0)
    green.value(0)

def dashOnOff():
    red.value(1)
    amber.value(1)
    green.value(1)
    time.sleep(2)
    red.value(0)
    amber.value(0)
    green.value(0)
    
def pause(milsec):
    time.sleep(milsec)

def textToCipher(str):
    cipher = ''
    for letter in str:
        if letter != ' ':
            cipher += code_dict[letter]
        else:
            cipher += ' '
 
    return cipher

def cipherToLights():
    message = input().upper()
    print(textToCipher(message))
    cipher = textToCipher(message)
    for bit in cipher:
        if bit == '.':
            dotOnOff()
            pause(0.5)
        elif bit == '-':
            dashOnOff()
            pause(0.5)
        elif bit == ' ':
            pause(1)
        
    return None

cipherToLights()