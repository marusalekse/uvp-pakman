import random

LEVO, DESNO, GOR, DOL = (-1,0), (1,0), (0,-1), (0,1)
polmer_pakmana = 0.5
polmer_duhca = 0.5
polmer_kovancka = 0.1
polmer_bonbona = 0.2
dolzina_premika = 0.1

#preveri, ce so koordinate cela stevila
def celostevilske_koordinate(koordinate):
  x, y = koordinate
  return round(x, 2) == int(round(x, 2)) and round(y, 2) == int(round(y,2))

class Pakman:
  def __init__(self, zacetni_polozaj):
    self.polozaj = zacetni_polozaj
    self.zacetni_polozaj = zacetni_polozaj
    self.aktiviranost = 0
    self.trenutna_smer = LEVO
    self.naslednja_smer = LEVO

class IgralnaPlosca:
  def __init__(self, ime_datoteke_s_poljem):
    self.polje = []
    self.zacetni_polozaj_pakmana = (0,0)
    self.zacetni_polozaji_duhcev = []
    self.portali = {}
    self.cekini = []
    self.bonboni = []

    #polje bomo naredili kot tabelo vseh polj, vrednosti na njih povejo kaj je na njemu
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
            self.bonboni.append((x, y))
          # Duhec
          elif znak == 'd':
            self.polje[y].append(0)
            self.zacetni_polozaji_duhcev.append((x, y))
          #Pakman
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
    self.rezultat = 0
    self.koraki_aktiviranost = 0
    self.igra_poteka = True
    self.visina = len(self.plosca.polje)
    self.sirina = len(self.plosca.polje[0])
    for duhec in self.plosca.zacetni_polozaji_duhcev:
      self.duhci.append(Pakman(duhec))

  #preveri, ce se duhec in pakman dotikata
  def zabijanje(self):
    for duhec in self.duhci:
        a, b = duhec.polozaj
        x, y = self.pakman.polozaj
        if (a-x)**2 + (b-y)**2 <= (polmer_pakmana + polmer_duhca)**2:
          if self.pakman.aktiviranost <= 0:
            return False
          else:
            duhec.polozaj = duhec.zacetni_polozaj
            self.rezultat += 50
    return True

  #premakne pakmana, ce se da
  def premik_pakmana(self, osebek):
    x, y = osebek.polozaj
    if celostevilske_koordinate(osebek.polozaj):
      for portal in self.plosca.portali:
        for lokacija in self.plosca.portali[portal]:
          a, b = lokacija
          if (int(round(x)), int(round(y))) == lokacija:
            #nastavimo koordinate na drug del portala
            osebek.polozaj = self.plosca.portali[portal][0 ** self.plosca.portali[portal].index(lokacija)]
            nov_x, nov_y = osebek.polozaj
            if nov_x == 0:
              osebek.trenutna_smer = osebek.naslednja_smer = DESNO
            elif nov_x == self.sirina - 1:
              osebek.trenutna_smer = osebek.naslednja_smer = LEVO
            elif nov_y == 0:
              osebek.trenutna_smer = osebek.naslednja_smer = DOL
            elif nov_y == self.visina - 1:
              osebek.trenutna_smer = osebek.naslednja_smer = GOR
            break
    x, y = osebek.polozaj
    if celostevilske_koordinate(osebek.polozaj):
      naslednja_smer_x, naslednja_smer_y = osebek.naslednja_smer
      # Preveri, ce je polje prosto
      if self.plosca.polje[naslednja_smer_y + int(round(y))][naslednja_smer_x + int(round(x))] != "1":
        osebek.trenutna_smer = osebek.naslednja_smer
    smer_x, smer_y = osebek.trenutna_smer
    if celostevilske_koordinate(osebek.polozaj) and self.plosca.polje[smer_y + int(round(y))][smer_x + int(round(x))] == "1":
      return 
    osebek.polozaj = x + dolzina_premika * smer_x, y + dolzina_premika * smer_y

  def sprememba_smeri(self, smer):
    self.pakman.naslednja_smer = smer

  #premakne duhca
  def premik_duhca(self, duhec):
    x, y = duhec.polozaj
    if celostevilske_koordinate(duhec.polozaj):
      veljavne_smeri = []

      sm_x, sm_y = duhec.trenutna_smer
      naslednji_x, naslednji_y = (sm_x + int(round(x)), sm_y + int(round(y)))
      odloci = True
      if 0 < naslednji_x < self.sirina - 1 and 0 < naslednji_y < self.visina - 1 and self.plosca.polje[naslednji_y][naslednji_x] != "1":
        odloci = False or random.randint(0, 10) == 2

      if odloci:
        for smer in [LEVO, DESNO, GOR, DOL]:
          sm_x, sm_y = smer
          naslednji_x, naslednji_y = (sm_x + int(round(x)), sm_y + int(round(y)))
          if 0 < naslednji_x < self.sirina - 1 and 0 < naslednji_y < self.visina - 1 and self.plosca.polje[naslednji_y][naslednji_x] != "1":
            veljavne_smeri.append(smer)
        duhec.trenutna_smer = random.choice(veljavne_smeri)
    smer_x, smer_y = duhec.trenutna_smer
    duhec.polozaj = (x + smer_x * dolzina_premika, y + smer_y * dolzina_premika)

  # ce je na istem mestu kot cekin ga poje, doda tocke k rezultatu
  def preveri_pojej_cekin(self):
    for cekin in self.plosca.cekini:
      a, b = cekin
      x, y = self.pakman.polozaj
      if (a-x)**2 + (b-y)**2 < (polmer_pakmana + polmer_kovancka)**2:
        self.plosca.cekini.remove(cekin)
        self.rezultat += 5

  # preveri ce je pakman na bonbonu, in aktivira pakmana
  def preveri_pojej_bonbon(self):
    for bonbon in self.plosca.bonboni:
      a, b = bonbon
      x, y = self.pakman.polozaj
      if (a-x)**2 + (b-y)**2 < (polmer_pakmana + polmer_bonbona)**2:
        self.plosca.bonboni.remove(bonbon)
        self.rezultat += 25
        # 10 korakov na polje, 50 polj
        self.pakman.aktiviranost = 10 * 20 

  #vse, kar se zgodi v enem koraku
  def korak(self):
    konec = not self.zabijanje()
    if konec:
      return False
    self.premik_pakmana(self.pakman)
    for duhec in self.duhci:
      self.premik_duhca(duhec)
    self.preveri_pojej_cekin()
    self.preveri_pojej_bonbon()
    self.pakman.aktiviranost -= 1
    return True

    




  

  
