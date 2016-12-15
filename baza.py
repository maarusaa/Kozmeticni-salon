import sqlite3
con = sqlite3.connect("kozmeticni_salon.sqlite")

#original :D 
def vnesiRacun(dat, oseba, izdelki, storitve):
"""Izdelki in storitve -> slovar, kljuc je ime izdelka/storitve, vrednost je pa količina"""
	cur = con.execute('''insert into racuni (datum, stranka) values (?, ?)''', [dat, oseba])
	racun = cur.lastrowid
	for izdelek in izdelki:
		cur.execute('''insert into racun_izdelek (st_racuna, izdelek, kolicina) VALUES (?, ?, ?)''', [racun, izdelek, izdelki[izdelek]])
	for storitev in storitve:
		cur.execute('''insert into racun_storitve (st_racuna, storitev, kolicina) VALUES (?, ?, ?)''', [racun, storitev, storitve[storitev]])
	cur.execute('''
	UPDATE racuni SET znesek =
	(SELECT sum(cena) FROM racun_izdelek JOIN kozmeticni_izdelki ON racun_izdelek.izdelek = id WHERE st_racuna = ?) +
	(SELECT sum(cena) FROM racun_storitve JOIN kozmeticne_storitve ON racun_storitve.storitev = id WHERE st_racuna = ?)''', [racun, racun])
	con.commit()
	
def idIzdelka(izdelek):
	'''funkcija vrne id izdelka.'''
	return  con.execute('''select id from kozmeticni_izdelki where izdelek = ?''', [izdelek])
	
def idStoritve(storitev):
	'''funkcija vrne id storitve'''
	return  con.execute('''select id from kozmeticne_storitve where storitev = ?''', [storitev])
	
def vstaviOsebo(ime, priimek):
	'''vstavi novo osebo v tabelo stranke'''
	try:
		con.execute('''insert into stranke (ime, priimek) VALUES (?, ?)''', [ime, priimek])
	except:
		# že obstaja
	

def idOsebe ( ime, priimek):
	'''funkcija vrne id osebe'''
	return con.execute('''select id from stranke where ime = ? and priimek = ?''', [ime, priimek])
	

def prosti_termini(storitev, dan, teden):
        #kaj ti to naredi? seznam, slovar wtf? :D 
        vsi_mozni_izvajalci_storitve = con.execute('''select id from zaposleni''')
        na_voljo = {
          'ponedeljek': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         },
          'torek': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         },
          'sreda': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         },
          'četrtek': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         },
          'petek': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         },
          'sobota': {
                         8: set(vsi_mozni_izvajalci_storitve),
                         9: set(vsi_mozni_izvajalci_storitve),
                         10: set(vsi_mozni_izvajalci_storitve),
                         11: set(vsi_mozni_izvajalci_storitve),
                         12: set(vsi_mozni_izvajalci_storitve),
                         13: set(vsi_mozni_izvajalci_storitve),
                         14: set(vsi_mozni_izvajalci_storitve),
                         15: set(vsi_mozni_izvajalci_storitve),
                         16: set(vsi_mozni_izvajalci_storitve),
                         17: set(vsi_mozni_izvajalci_storitve),
                         18: set(vsi_mozni_izvajalci_storitve),
                         19: set(vsi_mozni_izvajalci_storitve),
                         20: set(vsi_mozni_izvajalci_storitve)
                         }
          }
     
        for termin in ze_zasedeni_termini_v_tem_tednu:
                na_voljo[dan].remove(termin)
                
                #pobrisi termin iz na_voljo
        



	

	
	

	
	

