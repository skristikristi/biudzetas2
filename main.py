import sqlalchemy
import pandas



class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papild_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papild_info = papild_info

class IslaiduIrasas(Irasas):
    def __init__(self,suma, atsiskaitymo_budas,isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Zurnalas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamas(self, suma, siuntejas, papild_info):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papild_info)
        self.zurnalas.append(pajamu_irasas)

    def prideti_islaidas(self, suma, atsiskaitymo_budas,isigyta_preke_paslauga):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas,isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas)


    def gauti_biudzeto_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas) :
                suma -= irasas.suma
        return suma

    def parodyti_ataskaitą(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papild_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga}")


visas_biudzetas = Zurnalas()

while True:
    veiksmas = int(input("1- Įvesti pajamas, \n2- Įvesti išlaidas, \n3- gauti balansą, \n4- parodyti ataskaitą, \n5- uždaryti programą"))
    if veiksmas == 1:
        print("Įveskite pajamas: ")
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Siuntėjas: ")
        papild_info = input("Papildoma informacija: ")
        visas_biudzetas.prideti_pajamas(suma, siuntejas, papild_info)
        print("Pajamos įvestos sėkmingai!")
    if veiksmas == 2:
        print("Įveskite išlaidas: ")
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė ar paslauga: ")
        visas_biudzetas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        print("Išlaidos įvestos sėkmingai!")
    if veiksmas == 3:
        print(f"Balansas: {visas_biudzetas.gauti_biudzeto_balansa()}")
    if veiksmas == 4:
        visas_biudzetas.parodyti_ataskaitą()
    if veiksmas == 5:
        print("Geros dienos!")
        break