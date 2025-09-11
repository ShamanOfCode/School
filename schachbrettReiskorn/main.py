# Maerchen von "Das Schachbrett und die Reiskörner"
def schachbrett_reiskorn():

    felder = 64
    reiskornAnfang = 1
    gesamtReiskorn = 9

    for feld in range(1, felder + 1):
        reiskornAktuell = reiskornAnfang * (2 ** (feld - 1)) # ** = Potenzierung
        gesamtReiskorn += reiskornAktuell
        print(f"Feld {feld}: {reiskornAktuell} Reiskoerner")


    print(f"\nGesamtanzahl der Reiskoerner auf dem Schachbrett: {gesamtReiskorn}")

schachbrett_reiskorn()