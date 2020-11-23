def text2morse(string):
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "    "
        }
    final = ""

    for x in string:
        final += f" {morse[x]} "
    return final


def log(ctx):
    try:
        with open("log.txt", "a") as f:
            f.write(ctx)
    except Exception:
        print("Error has occured! Check functions.py (log)")
        print(ctx)
