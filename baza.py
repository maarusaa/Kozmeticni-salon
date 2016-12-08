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
	
	

	
###poskus 2 :D
##def vnesiRacun(dat, ime, priimek, izdelki, storitve):
##    """Izdelki in storitve -> slovar, kljuc je ime izdelka/storitve, vrednost je pa količina"""
##    #for x in con.execute('''SELECT ime,priimek FROM stranke WHERE ime = ? AND priimek = ?''', (ime, priimek)):print(x)
##    if ime,priimek not in con.execute('''SELECT ime,priimek FROM stranke WHERE ime = ? AND priimek = ?''', [ime, priimek]):
##            con.execute('''insert into stranke (ime, priimek) VALUES (?, ?)''', [ime, priimek])
##    
##    oseba = con.execute('''SELECT id FROM stranke where ime = ? AND priimek = ?''', [ime,priimek])
##    print(oseba)
##    cur = con.execute('''insert into racuni (datum, stranka) values (?, ?)''', [dat, oseba])
##    racun = cur.lastrowid
##    for izdelek in izdelki:
##            cur.execute('''insert into racun_izdelek (st_racuna, izdelek, kolicina) VALUES (?, ?, ?)''', [racun, izdelek, izdelki[izdelek]])
##    for storitev in storitve:
##            cur.execute('''insert into racun_storitve (st_racuna, storitev, kolicina) VALUES (?, ?, ?)''', [racun, storitev, storitve[storitev]])
##    cur.execute('''
##    UPDATE racuni SET znesek =
##    (SELECT sum(cena) FROM racun_izdelek JOIN kozmeticni_izdelki ON racun_izdelek.izdelek = id WHERE st_racuna = ?) +
##    (SELECT sum(cena) FROM racun_storitve JOIN kozmeticne_storitve ON racun_storitve.storitev = id WHERE st_racuna = ?)''', [racun, racun])
##    con.commit()

	

	
	

	
	

