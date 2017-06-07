LEVO, DESNO, GOR, DOL = (-1,0), (1,0), (0,1), (0,-1)
polmer_pakmana = 0.5
polmer_duhca = 0.5
polmer_kovancka = 0.1
polmer_bonbona = 0.2
dolzina_premika = 0.1

def celostevilske_koordinate(koordinate):
  x, y = koordinate
  return round(x, 2) == int(round(x, 2)) and round(y, 2) == int(round(y,2))

class Pakman:
  def __init__(self, zacetni_polozaj):
    self.polozaj = zacetni_polozaj
    self.zacetni_polozaj = zacetni_polozaj
    self.aktiviranost = False
    self.trenutna_smer = LEVO
    self.naslednja_smer = LEVO

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
    self.cekini = []
    self.bomboni = []

    #polje bomo naredili kot tabelo vseh polij, vrednosti na njih povejo kaj je na njemu
    with open(ime_datoteke_s_poljem) as f:
      y = 0
      for vrstica in f:
        self.polje.append([])
        x  =  0
        for znak in vrstica.strip():
          # Prazno ali zid
          if znak == '0' or znak == '1':
            self.polje[y].append(znak)
          # Portali
          elif znak >= 'A' and znak <= 'Z':
            self.polje[y].append(0)
            portal_par = self.portali.get(znak, [])
            portal_par.append((x, y))
            self.portali[znak] = portal_par
          # Cekini
          elif znak == 'c':
            self.polje[y].append(0)
            self.cekini.append((x, y))
          # Bombon, ki z vso svojo energijo žre duhove
          elif znak == 'b':
            self.polje[y].append(0)
            self.bomboni.append((x, y))
          # Duhec
          elif znak == 'd':
            self.polje[y].append(0)
            self.zacetni_polozaji_duhcev.append((x, y))
          elif znak == 'p':
            self.polje[y].append(0)
            self.zacetni_polozaj_pakmana = (x, y)
          x += 1
        y += 1


class Igra:
  def __init__(self, ime_datoteke_s_poljem):
    self.plosca = IgralnaPlosca(ime_datoteke_s_poljem)
    self.pakman = Pakman(self.plosca.zacetni_polozaj_pakmana)
    self.duhci = []
    self.reultat = 0
    self.igra_poteka = True
    self.visina = len(self.plosca.polje)
    self.sirina = len(self.plosca.polje[0])
    for duhec in self.plosca.zacetni_polozaji_duhcev:
      self.duhci.append(Pakman(duhec))

  #nastavi parametre na hitrejs
  # def zmaga():
  # se vedno morm dt da je konc tko da se ne preskocta
  # zdej morm se nekak klicat da se spremeni smer
  # def premik duhca():
  # 
  def zabijanje(self):
    for duhec in self.duhci:
        a, b = duhec.polozaj
        x, y = self.pakman.polozaj
        if (a-x)**2 + (b-y)**2 <= (polmer_pakmana + polmer_duhca)**2:
          if self.pakman.aktiviranost == False:
            self.igra_poteka = False
          else:
            duhec.polozaj = duhec.zacetni_polozaj

  def premik_pakmana(self, osebek):
    x, y = osebek.polozaj
    smer_x, smer_y = osebek.smer
    if celostevilske_koordinate(osebek.polozaj):
      naslednja_smer_x, naslednja_smer_y = osebek.naslednja_smer
      # Preverim, ali je polje prosto
      if self.plosca.polja[naslednja_smer_y + y][naslednja_smer_x + x] != "1":
        osebek.smer = osebek.naslednja_smer
      if self.plosca.polja[smer_y + y][smer_x + x] == "1":
        return 
    #za portal
    smer_x, smer_y = osebek.smer
    osebek.polozaj = x + dolzina_premika * smer_x, y + dolzina_premika * smer_y

  def premik_duhca(self, duhec):
    x, y = duhec.polozaj
    #if x//1 == x and y//1 == y:
  def korak(self):
    self.zabijanje()
    return

    




  

  
