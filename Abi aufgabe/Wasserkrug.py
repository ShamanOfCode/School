#Das Dreikrügeproblem ist eine klassische Denksportaufgabe, bei der man drei Wasserkrüge mit
#8 Litern, 5 Litern und 3 Litern Fassungsvermögen zur Verfügung hat. Man darf das Wasser eines
#Kruges in einen anderen umfüllen. Da die Krüge keine Messstriche haben, kann man beim Umfüllen
#entweder den Krug komplett leeren oder einen anderen Krug ganz voll machen. Gesucht ist eine Folge
#v Umfüllungen, durch welche die 8 Liter Wasser im großen Krug auf zwei Krüge mit je 4 Liter
#Wasser aufgeteilt werden.
#In der Aufgabe geht es um die Modellierung und Implementierung eines Programms, das eine
#möglichst kurze Folge v Füllzuständen der Krüge als Liste v Zuständen ausgibt.
#Eine Lösung sieht so aus: [(8,0,0), (3,5,0), (3,2,3), (6,2,0), (6,0,2), (1,5,2), (1,4,3), (4,4,0)]
#Ausgehend vom Startzustand (8,0,0) wird der gewünschte Endzustand (4,4,0) durch sieben
#Umfüllungen erreicht.
# G = Gross (8 Liter)
# M = Mittel (5 Liter)
# K = Klein (3 Liter)

def fuellen(krug1, krug2, krug3, v, n):
    if v == 'G' and n == 'M':
        menge = min(krug1, 5 - krug2)
        krug1 -= menge
        krug2 += menge
    elif v == 'G' and n == 'K':
        menge = min(krug1, 3 - krug3)
        krug1 -= menge
        krug3 += menge
    elif v == 'M' and n == 'G':
        menge = min(krug2, 8 - krug1)
        krug2 -= menge
        krug1 += menge
    elif v == 'M' and n == 'K':
        menge = min(krug2, 3 - krug3)
        krug2 -= menge
        krug3 += menge
    elif v == 'K' and n == 'G':
        menge = min(krug3, 8 - krug1)
        krug3 -= menge
        krug1 += menge
    elif v == 'K' and n == 'M':
        menge = min(krug3, 5 - krug2)
        krug3 -= menge
        krug2 += menge
    return (krug1, krug2, krug3)
def loesung():
    start = (8, 0, 0)
    ziel = (4, 4, 0)
    con = start
    besuchte_zustaende = set()
    besuchte_zustaende.add(con)
    pfad = [con]
    while con != ziel:
        for v in ['G', 'M', 'K']:
            for n in ['G', 'M', 'K']:
                if v != n:
                    new = fuellen(con[0], con[1], con[2], v, n)
                    if new not in besuchte_zustaende:
                        besuchte_zustaende.add(new)
                        pfad.append(new)
                        con = new
                        break
            else:
                continue
            break
    return pfad
print(loesung())
