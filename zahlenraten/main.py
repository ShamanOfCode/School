# Zahlenraten mit rekursion  ohne try/except
# 2 methoden wobei die 2. methode die rekursive ist und start und end eingrenzt
# 1 Methode die die 2 aufruft und die zahl generiert

import random

def zahlenraten_rekursiv(start, end):
    if start > end:
        print("Die Zahl wurde nicht gefunden.")
        return
    mitte = (start + end) // 2
    print(f"Ist deine Zahl {mitte}? (Antwort: 'ja', 'größer', 'kleiner')")
    antwort = input().strip().lower()
    if antwort == "ja":
        print(f"Glückwunsch! Die Zahl ist {mitte}.")
    elif antwort == "größer":
        zahlenraten_rekursiv(mitte + 1, end)
    elif antwort == "kleiner":
        zahlenraten_rekursiv(start, mitte - 1)
    else:
        print("Ungültige Eingabe. Bitte antworte mit 'ja', 'größer' oder 'kleiner'.")
        zahlenraten_rekursiv(start, end)

def zahlenraten_start():
    start = 1
    end = 100
    print("Denke dir eine Zahl zwischen 1 und 100. Ich versuche sie zu erraten!")
    zahlenraten_rekursiv(start, end)

if __name__ == "__main__":
    zahlenraten_start()
