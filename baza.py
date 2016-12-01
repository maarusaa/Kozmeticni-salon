import sqlite3
con = sqlite3.connect("kozmeticni_salon.sqlite")

"""def racun(idRacuna):
    "Sesteje znesek plačila"
    vsota = 0
    for racunIzdelek in con.execute('''
		SELECT st_racuna
		FROM racun_izdelek  
		WHERE racunIzdelek == idRacuna
    ''')"""
	
def vnesiRacun(dat, oseba, izdelki, storitve):
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

	
	

