import tkinter as tk
import be

SKALA = 20
BARVA_STENE = '#003'
BARVA_PAKMANA = '#EE0'
BARVA_DUHCA = '#00E'
KORAK_MS = 30

VELIKOST_CEKINA = SKALA * be.polmer_kovancka * 2
BARVA_CEKINA = "#00A"

VELIKOST_BOMBONA = SKALA * be.polmer_bonbona * 2
BARVA_BOMBONA = "#FF0"

class PrikazIgre:
  def __init__(self, okno, ime_povrsine):
    self.okno = okno
    self.igra = be.Igra(ime_povrsine)
    self.platno = tk.Canvas(
        width=SKALA * self.igra.sirina,
        height=SKALA * self.igra.visina
    )
    self.okno.bind('<Key>', self.obdelaj_tipko)
    self.platno.pack()
    self.narisi()
    self.okno.after(KORAK_MS, self.korak)

  def koncaj(self, sporocilo):
    self.okno.destroy()
    koncno_okno = tk.Tk()
    sporocilo = tk.Label(koncno_okno, text="{}! Vaš rezultat: {}".format(sporocilo, self.igra.rezultat))
    sporocilo.pack()
    koncno_okno.mainloop()
    return

  def korak(self):
    self.igra.korak()
    self.narisi()
    self.okno.after(KORAK_MS, self.korak)
    

  def obdelaj_tipko(self, event):
    return
    #if event.keysym == 'Right':
    #    self.igra.spremeni_smer(be.DESNO)
    #elif event.keysym == 'Left':
    #    self.igra.spremeni_smer(model.LEVO)
    #elif event.keysym == 'Up':
    #    self.igra.spremeni_smer(model.GOR)
    #elif event.keysym == 'Down':
    #    self.igra.spremeni_smer(model.DOL)
    #self.narisi()

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

    for bombon in self.igra.plosca.bomboni:
      x_bombona, y_bombona = bombon
      self.platno.create_rectangle(
        x_bombona * SKALA + (SKALA - VELIKOST_BOMBONA) / 2,
        y_bombona * SKALA + (SKALA - VELIKOST_BOMBONA) / 2,
        (x_bombona + 1) * SKALA - (SKALA - VELIKOST_BOMBONA) / 2,
        (y_bombona + 1) * SKALA - (SKALA - VELIKOST_BOMBONA) / 2,
        fill = BARVA_BOMBONA,
        outline = BARVA_BOMBONA
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
    self.platno.create_oval(
      pakman_x * SKALA,
      pakman_y * SKALA,
      (pakman_x + 1) * SKALA,
      (pakman_y + 1) * SKALA,
        fill = BARVA_PAKMANA,
        outline = BARVA_PAKMANA
    )

okno = tk.Tk()
moj_program = PrikazIgre(okno, 'povrsina/povrsina.txt')
okno.mainloop()