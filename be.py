LEVO, DESNO, GOR, DOL = "levo", "desno", "gor", "dol"
polmer_pakmana = 0.5
polmer_duhca = 0,5
polmer_kovancka = 0,2
polmer_bonbona = 0,3


class Pakman:
  def __init__(self, zacetni_polozaj):
    self.polozaj = zacetni_polozaj
    self.zacetni_polozaj = zacetni_polozaj
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
    self.zacetni_polozaj_pakmana = (0,0)
    self.zacetni_polozaji_duhcev = []
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
            self.zacetni_polozaji_duhcev.append( (j,i) )
          #podobno moram narediti se za slovar portalov,pakmana
          j += 1
        i+=1
  #ta funkcija bo neumna, klicala jo bom na pravem polozaju
  def pojej_kovancek(polozaj):
    a, b = polozaj
    self.polje[a][b] = "0"

class Igra:
  def __init__(self, ime_datoteke_s_poljem):
    self.plosca = IgralnaPlosca(ime_datoteke_s_poljem)
    self.pakman = Pakman(self.plosca.zacetni_polozaj_pakmana)
    self.duhci = []
    self.reultat = 0
    self.igra_poteka = True
    for duhec in self.plosca.zacetni_polozaji_duhcev:
      self.duhci.append(Pakman(duhec))

  #nastavi parametre na hitrejs
  # def zmaga():
  # zdej morm se nekak klicat da se spremeni smer
  # def premik duhca():
  # 
  # 
  def zabijanje()
    for duhec in self.duhci:
        a, b = duhec.polozaj
        x, y = self.pakman.polozaj
        if (a-x)**2 + (b-y)**2 <= (polmer_pakmana + polmer_duhca)**2:
          if self.pakman.aktiviranost = FALSE:
            self.igra_poteka = FALSE
          else:
            duhec.polozaj = duhec.zacetni_polozaj

  #def premik():


  
  def korak():
    zabijanje()

    




  

  
