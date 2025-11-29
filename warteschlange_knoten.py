# UML: Buch -titel - autor -prioritaet c __init(titel:Str, autor:str, prioritaet:int) +information_ausgeben()
# Knoten -nachfolger: Knoten -daten: Buch c__init(buch:Buch)  +nachfolger_setzen(knoten:Knoten) +nachfolger_geben(): Knoten +datenelement_geben():Buch
# Warteschlange -anfang: Knoten -ende: Knoten c__init__() +einfuegen(buch:Buch)  +loeschen() +bestimmtes_loeeschen(prioritaet) +ausgeben():int

class Buch:
    def __init__(self, titel: str, autor: str, prioritaet: int):
        self.titel = titel
        self.autor = autor
        self.prioritaet = prioritaet

    def information_ausgeben(self):
        return f'Titel: {self.titel}, Autor: {self.autor}, Priorität: {self.prioritaet}'
class Knoten:
    def __init__(self, buch: Buch):
        self.nachfolger = None
        self.daten = buch

    def nachfolger_setzen(self, knoten: 'Knoten'):
        self.nachfolger = knoten
    def nachfolger_geben(self) -> 'Knoten':
        return self.nachfolger
    def datenelement_geben(self) -> Buch:
        return self.daten
class Warteschlange:
    def __init__(self):
        self.anfang = None
        self.ende = None
    def einfuegen(self, buch: Buch):
        neuer_knoten = Knoten(buch)
        if self.anfang is None:
            self.anfang = neuer_knoten
            self.ende = neuer_knoten
        else:
            self.ende.nachfolger_setzen(neuer_knoten)
            self.ende = neuer_knoten
    def loeschen(self):
        if self.anfang is None:
            return None
        geloeschtes_buch = self.anfang.datenelement_geben()
        self.anfang = self.anfang.nachfolger_geben()
        if self.anfang is None:
            self.ende = None
        return geloeschtes_buch
    def bestimmtes_loeeschen(self, prioritaet: int):
        aktueller_knoten = self.anfang
        vorheriger_knoten = None
        while aktueller_knoten is not None:
            if aktueller_knoten.datenelement_geben().prioritaet == prioritaet:
                if vorheriger_knoten is None:
                    self.anfang = aktueller_knoten.nachfolger_geben()
                    if self.anfang is None:
                        self.ende = None
                else:
                    vorheriger_knoten.nachfolger_setzen(aktueller_knoten.nachfolger_geben())
                    if aktueller_knoten == self.ende:
                        self.ende = vorheriger_knoten
                return aktueller_knoten.datenelement_geben()
            vorheriger_knoten = aktueller_knoten
            aktueller_knoten = aktueller_knoten.nachfolger_geben()
        return None
    def ausgeben(self) -> int:
        aktueller_knoten = self.anfang
        count = 0
        while aktueller_knoten is not None:
            print(aktueller_knoten.datenelement_geben().information_ausgeben())
            aktueller_knoten = aktueller_knoten.nachfolger_geben()
            count += 1
        return count
    #sort priority
    def bubble_sort(self):
        if self.anfang is None:
            return
        end = None
        while end != self.anfang:
            aktueller_knoten = self.anfang
            while aktueller_knoten.nachfolger_geben() != end:
                naechster_knoten = aktueller_knoten.nachfolger_geben()
                if aktueller_knoten.datenelement_geben().prioritaet > naechster_knoten.datenelement_geben().prioritaet:
                    aktueller_knoten.daten, naechster_knoten.daten = naechster_knoten.daten, aktueller_knoten.daten
                aktueller_knoten = naechster_knoten
            end = aktueller_knoten

if __name__ == "__main__":
    warteschlange = Warteschlange()
    buch1 = Buch("Bob Story 1", "Bob1", 1)
    buch2 = Buch("Bob Story 2", "Bob2", 2)
    buch3 = Buch("Bob Story 3", "Bob3", 3)

    warteschlange.einfuegen(buch1)
    warteschlange.einfuegen(buch2)
    warteschlange.einfuegen(buch3)

    print("Warteschlange nach dem Einfügen:")
    warteschlange.ausgeben()

    print("Warteschlange vor dem Sortieren:")
    warteschlange.ausgeben()

    warteschlange.bubble_sort()

    # show the queue after sorting
    print("\nWarteschlange nach dem Sortieren (nach Priorität):")
    warteschlange.ausgeben()

    geloeschtes_buch = warteschlange.loeschen()
    print(f"\nGelöschtes Buch: {geloeschtes_buch.information_ausgeben()}")

    print("\nWarteschlange nach dem Löschen:")
    warteschlange.ausgeben()

    bestimmtes_geloeschtes_buch = warteschlange.bestimmtes_loeeschen(1)
    if bestimmtes_geloeschtes_buch:
        print(f"\nBestimmt gelöschtes Buch mit Priorität 1: {bestimmtes_geloeschtes_buch.information_ausgeben()}")
    else:
        print("\nKein Buch mit der angegebenen Priorität gefunden.")

    print("\nWarteschlange nach dem bestimmten Löschen:")
    warteschlange.ausgeben()
