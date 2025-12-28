

class Flugzeug:
    def __init__(self, flugnummer, geplante_ankunftszeit, tatsaechliche_ankunftszeit, ausnahmegenehmigung=False):
        self.flugnummer = flugnummer
        self.geplante_ankunftszeit = geplante_ankunftszeit
        self.tatsaechliche_ankunftszeit = tatsaechliche_ankunftszeit
        self.ausnahmegenehmigung = ausnahmegenehmigung
        self.landeerlaubnis = False
    def darf_landen(self):
        if self.ausnahmegenehmigung:
            self.landeerlaubnis = True
        elif 23 <= self.tatsaechliche_ankunftszeit < 24:
            if self.geplante_ankunftszeit < 23:
                self.landeerlaubnis = True
        else:
            self.landeerlaubnis = False
        return self.landeerlaubnis

flug1 = Flugzeug("AB123", 22, 23)
flug2 = Flugzeug("CD456", 21, 1)
flug3 = Flugzeug("EF789", 20, 0, ausnahmegenehmigung=True)
print(f"{flug1.flugnummer} darf landen: {flug1.darf_landen()}")
print(f"{flug2.flugnummer} darf landen: {flug2.darf_landen()}")
print(f"{flug3.flugnummer} darf landen: {flug3.darf_landen()}")
