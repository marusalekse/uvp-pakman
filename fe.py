import tkinter as tk
import be

SKALA = 20
BARVA_STENE = '#003'
BARVA_PAKMANA = '#EE0'
OBRATNA_BARVA_PAKMANA = '#11F'

BARVA_DUHCA = '#00E'
ZACETNA_HITROST = 30

VELIKOST_CEKINA = SKALA * be.polmer_kovancka * 2
BARVA_CEKINA = "#00A"

VELIKOST_bonbona = SKALA * be.polmer_bonbona * 2
BARVA_bonbona = "#FF0"
# tocke bomo belezili tu, ker se v be pobrisejo
REZULTAT = 0

class PrikazIgre:
  def __init__(self, okno, ime_povrsine, hitrost, level):
    self.okno = okno
    self.hitrost = hitrost
    self.igra = be.Igra(ime_povrsine)
    self.platno = tk.Canvas(
        width=SKALA * self.igra.sirina,
        height=SKALA * self.igra.visina
    )
    self.level = level
    self.okno.bind('<Key>', self.obdelaj_tipko)
    self.platno.pack()
    self.narisi()
    self.okno.after(self.hitrost, self.korak)

  #pokaze, da je pakman umrl
  def koncaj(self, sporocilo):
    global REZULTAT
    REZULTAT += self.igra.rezultat
    self.okno.destroy()
    koncno_okno = tk.Tk()
    sporocilo = tk.Label(koncno_okno, text="{}! Vaš rezultat: {}".format(sporocilo, REZULTAT))
    sporocilo.pack()
    koncno_okno.mainloop()
    return

  # pokaze, da gre pakman v naslednji level
  def levelWin(self):
    global REZULTAT
    REZULTAT += self.igra.rezultat
    self.okno.destroy()
    self.novo_okno = tk.Tk()
    sporocilo = tk.Label(self.novo_okno, text="Level UP!!!")
    sporocilo.pack()
    self.novo_okno.after(3000, self.levelup)
    self.novo_okno.mainloop()

  #pakman gre v naslednji level
  def levelup(self):
    #PONOVNI ZAGON
    print("Level UP! SCORE:", self.igra.rezultat)
    self.novo_okno.destroy()
    okno = tk.Tk()
    moj_program = PrikazIgre(okno, 'povrsina/povrsina.txt', int(round(self.hitrost * 0.75)), self.level + 1)
    okno.mainloop()

  def korak(self):
    konec = not self.igra.korak()
    if konec:
      self.koncaj('Konec igre')
    elif len(self.igra.plosca.cekini) == 0:
      self.levelWin()
    else:
      self.narisi()
      self.okno.after(self.hitrost, self.korak)
    
  def obdelaj_tipko(self, event):
    if event.keysym == 'Right':
        self.igra.sprememba_smeri(be.DESNO)
    elif event.keysym == 'Left':
        self.igra.sprememba_smeri(be.LEVO)
    elif event.keysym == 'Up':
        self.igra.sprememba_smeri(be.GOR)
    elif event.keysym == 'Down':
        self.igra.sprememba_smeri(be.DOL)

  #narise vse stvari v oknu
  def narisi(self):
    self.platno.delete('all')
    for y, vrstica in enumerate(self.igra.plosca.polje):
      for x, znak in enumerate(vrstica):
        if (znak == '1'):
          self.platno.create_rectangle(
            x * SKALA,
            y * SKALA,
            (x + 1) * SKALA,
            (y + 1) * SKALA,
            fill = BARVA_STENE,
            outline = BARVA_STENE
          )
    for cekin in self.igra.plosca.cekini:
      x_cekina, y_cekina = cekin
      self.platno.create_rectangle(
        x_cekina * SKALA + (SKALA - VELIKOST_CEKINA) / 2,
        y_cekina * SKALA + (SKALA - VELIKOST_CEKINA) / 2,
        (x_cekina + 1) * SKALA - (SKALA - VELIKOST_CEKINA) / 2,
        (y_cekina + 1) * SKALA - (SKALA - VELIKOST_CEKINA) / 2,
        fill = BARVA_CEKINA,
        outline = BARVA_CEKINA
      )

    for bonbon in self.igra.plosca.bonboni:
      x_bonbona, y_bonbona = bonbon
      self.platno.create_rectangle(
        x_bonbona * SKALA + (SKALA - VELIKOST_bonbona) / 2,
        y_bonbona * SKALA + (SKALA - VELIKOST_bonbona) / 2,
        (x_bonbona + 1) * SKALA - (SKALA - VELIKOST_bonbona) / 2,
        (y_bonbona + 1) * SKALA - (SKALA - VELIKOST_bonbona) / 2,
        fill = BARVA_bonbona,
        outline = BARVA_bonbona
      )

    for duhec in self.igra.duhci:
      duh_x, duh_y = duhec.polozaj
      self.platno.create_oval(
        duh_x * SKALA,
        duh_y * SKALA,
        (duh_x + 1) * SKALA,
        (duh_y + 1) * SKALA,
          fill = BARVA_DUHCA,
          outline = BARVA_DUHCA
      )


    pakman_x, pakman_y = self.igra.pakman.polozaj
    if self.igra.pakman.aktiviranost <= 0 or 0 <= self.igra.pakman.aktiviranost % 10 < 5:
      pak_barva = BARVA_PAKMANA
    else:
      pak_barva = OBRATNA_BARVA_PAKMANA
    self.platno.create_oval(
      pakman_x * SKALA,
      pakman_y * SKALA,
      (pakman_x + 1) * SKALA,
      (pakman_y + 1) * SKALA,
        fill = pak_barva,
        outline = pak_barva
    )

okno = tk.Tk()
moj_program = PrikazIgre(okno, 'povrsina/povrsina.txt', ZACETNA_HITROST, 1)
okno.mainloop()