LEVO, DESNO, GOR, DOL = "levo", "desno", "gor", "dol"


class Pakman:
  def __init__(self, zacetni_polozaj):
    self.polozaj = zacetni_polozaj
    self.aktiviranost = FALSE
    self.trenutna_smer = LEVO
    self.naslednja_smer = LEVO

  #vrnila bo naslednji polozaj
  #def premik():
  #najprej bom mogla klicat spremembo smeri
  #klicala jo bom ob pritisku gumba, pogleda, e lahko spremeni smer, cene jo nastavi za naslednjo
  #def sprememba_smeri():

  #duhec bo classa Pakman, samo nioli ga ne bom aktivirala ali klicala funkcije sprememba smeri.

class IgralnaPlosca:
  def __init__(self, ime_datoteke_s_poljem):
    self.polje = []
    self.zacetni_polozaji_duhcev = {}
    self.portali = {}
    #polje bomo naredili kot tabelo vseh polij, vrednosti na njih povejo kaj je na njemu
    with open(ime_datoteke_s_poljem) as f:
      i = 0
      for vrstica in f:
        self.polje.append([])
        j  =  0
        for znak in vrstica.strip:
          self.polje[i].append(znak)
          if znak == "d":
            self.portali.add( (j,i) )
          #podobno moram narediti se za slovar portalov
          j += 1
        i+=1
  #ta funkcija bo neuna, klicala jo bom na pravem polozaju
  def pojej_kovancek(polozaj):
    a, b = polozaj
    self.polje[a][b] = "0"

#class Igra

  
