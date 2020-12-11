import sys
import AnalisadorLexico as AL
import AnalisadorSintatico as AS

def itsInt(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False

def itsFloat(s):
    try:
        x = float(s)
        return True
    except ValueError:
        return False

