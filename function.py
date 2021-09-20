from os import system

def vz():
    print("")

def l():
    print("\033[33m=x=\033[m"*11)

def nome():
    print("\033[1;96m _  __    _       _")
    print("| |/ /_ _(_)_ __ | |_ ___  _ __")
    print("|   /| ´_| | ´_ \| __/ _ \| ´_ \ ")
    print("| . \| | | | |_) | || (_) | | | |")
    print("|_|\_\_| |_| .__/ \__\___/|_| |_|")
    print("           |_|\033[m")
    print("")

def cle():
    system("clear")

def cript(frase):
    cript = ""
    for letra in frase:
        if letra in "AaáÁàÀãÃâÂ": cript += "x"
        elif letra in "Bb": cript += "U"
        elif letra in "CcÇç": cript += "u"
        elif letra in "Dd": cript += "C"
        elif letra in "EeéÉèÈÊê": cript += "a"
        elif letra in "Ff": cript += "L"
        elif letra in "Gg": cript += "W"
        elif letra in "Hh": cript += "Z"
        elif letra in "IiíÍìÌîÎ": cript += "v"
        elif letra in "Jj": cript += "z"
        elif letra in "Kk": cript += "d"
        elif letra in "Ll": cript += "V"
        elif letra in "Mm": cript += "R"
        elif letra in "Nn": cript += "H"
        elif letra in "OoóÓòÒõÕÔô": cript += "g"
        elif letra in "Pp": cript += "h"
        elif letra in "Qq": cript += "X"
        elif letra in "Rr": cript += "c"
        elif letra in "Ss": cript += "w"
        elif letra in "Tt": cript += "A"
        elif letra in "UuúÙùÚûÛ": cript += "l"
        elif letra in "Vv": cript += "D"
        elif letra in "Ww": cript += "r"
        elif letra in "Xx": cript += "Q"
        elif letra in "Yy": cript += "G"
        elif letra in "Zz": cript += "q"
        elif letra in " ,.": cript += "s"
        elif letra in "!": cript += "i"
        elif letra in "?": cript += "I"
        elif letra  in "+": cript += "K"
        elif letra in "-": cript += "k"
        else: cript += letra
    return cript

def decript(frase):
    decript = ""
    for letra in frase:
        if letra in "x": decript += "a"
        elif letra in "U": decript += "b"
        elif letra in "u": decript += "c"
        elif letra in "C": decript += "d"
        elif letra in "a": decript += "e"
        elif letra in "L": decript += "f"
        elif letra in "W": decript += "g"
        elif letra in "Z": decript += "h"
        elif letra in "v": decript += "i"
        elif letra in "z": decript += "j"
        elif letra in "d": decript += "k"
        elif letra in "V": decript += "l"
        elif letra in "R": decript += "m"
        elif letra in "H": decript += "n"
        elif letra in "g": decript += "o"
        elif letra in "h": decript += "p"
        elif letra in "X": decript += "q"
        elif letra in "c": decript += "r"
        elif letra in "w": decript += "s"
        elif letra in "A": decript += "t"
        elif letra in "l": decript += "u"
        elif letra in "D": decript += "v"
        elif letra in "r": decript += "w"
        elif letra in "Q": decript += "x"
        elif letra in "G": decript += "y"
        elif letra in "q": decript += "z"
        elif letra in "s": decript += " "
        elif letra in "i": decript += "!"
        elif letra in "I": decript += "?"
        elif letra  in "K": decript += "+"
        elif letra in "k": decript += "-"
        else: decript += letra
    return decript
