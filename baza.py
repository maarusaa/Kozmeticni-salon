import sqlite3
con = sqlite3.connect("kozmeticni_salon.sqlite")
con.row_factory = sqlite3.Row

def vnesiRacun(dat, oseba, izdelki, storitve):
        '''Izdelki in storitve -> seznam'''
        cur = con.execute('''insert into racuni (datum, stranka) values (?, ?)''', [dat, oseba])
        racun = cur.lastrowid
        for izdelek in izdelki:
                cur.execute('''insert into racun_izdelek (st_racuna, izdelek) VALUES (?, ?)''', [racun, izdelek])
        for storitev in storitve:
                cur.execute('''insert into racun_storitve (st_racuna, storitev) VALUES (?, ?)''', [racun, storitev])
        cur.execute('''
        UPDATE racuni SET znesek =
        (SELECT sum(cena) FROM racun_izdelek JOIN kozmeticni_izdelki ON racun_izdelek.izdelek = id WHERE st_racuna = ?) +
        (SELECT sum(cena) FROM racun_storitve JOIN kozmeticne_storitve ON racun_storitve.storitev = id WHERE st_racuna = ?)
        WHERE id = ?''', [racun, racun, racun])
        con.commit()
        return racun
        
def idIzdelka(izdelek):
        '''funkcija vrne id izdelka.'''
        id_izdelka = con.execute('''select id from kozmeticni_izdelki where izdelek = ?''', [izdelek]).fetchone()
        return id_izdelka['id']
        
def idStoritve(storitev):
        '''funkcija vrne id storitve'''
        id_storitve =  con.execute('''select id from kozmeticne_storitve where storitev = ?''', [storitev]).fetchone()
        return id_storitve['id']
        
def idOsebe(ime, priimek):
        '''vstavi novo osebo v tabelo stranke in vrne id'''
        oseba = con.execute('''select id from stranke where ime = ? and priimek = ?''', [ime, priimek]).fetchone()#nam vrne osebo ali None, ce ga se ni v bazi
        if oseba is not None:
                return oseba['id']
        else:
                cur = con.execute('''insert into stranke (ime, priimek) VALUES (?, ?)''', [ime, priimek])
                con.commit()
                return cur.lastrowid


def idZaposlenega():
        return list(con.execute('''select id, ime, priimek from zaposleni'''))

	
def seznamIzdelkov():
	return list(con.execute('''select id, cena, izdelek, zaloga from kozmeticni_izdelki'''))

def seznamStoritev():
	return list(con.execute('''select id, cena, storitev, cas from kozmeticne_storitve'''))
        

def seznamIzvajalcev():
        return list(con.execute('''select id, ime, priimek from zaposleni'''))

def dodajIzdelek(ime, cena, zaloga):
        con.execute('''insert into kozmeticni_izdelki (izdelek, cena, zaloga) VALUES (?,?,?)''', [ime, cena, zaloga])
        con.commit()

def dodajStoritev(ime, cena, cas):
        con.execute('''insert into kozmeticne_storitve (storitev, cena, cas) VALUES (?,?,?)''', [ime, cena, cas])
        con.commit()

def dodajIzvajalca(storitev, izvajalec):
        con.execute('''insert into izvaja (storitev, zaposleni) VALUES (?,?)''', [storitev, izvajalec])
        con.commit()


def izbrisiIzdelek(id_izdelka):
        con.execute('''delete from kozmeticni_izdelki where id = ?''', [id_izdelka])

def odstraniStoritev(id_storitve):
        con.execute('''delete from kozmeticne_storitve where id = ?''', [id_storitve])
        
def odstraniIzvajalca(id_storitve):
        con.execute('''delete from izvaja where storitev = ?''', [id_storitve])


def spremeniCeno(cena, id_izdelka):
        return con.execute('''update kozmeticni_izdelki set cena = ? where id = ?''',[cena, id_izdelka])
        con.commit()

def spremeniCenoS(cena, id_storitve):
        return con.execute('''update kozmeticne_storitve set cena = ? where id = ?''',[cena, id_storitve])
        con.commit()

def spremeniZalogo(zaloga, id_izdelka):
        con.execute('''update kozmeticni_izdelki set zaloga = ? where id = ?''',[zaloga, id_izdelka])
        con.commit()

def spremeniIzvajalca(id_storitve, id_izvajalca):
        con.execute('''update izvaja set zaposleni = ? where storitev = ?''',[id_izvajalca, id_storitve])
        con.commit()


def izbraneStoritve(racun):
        return list(con.execute('''select kozmeticne_storitve.storitev, kozmeticne_storitve.cena
                                        from racun_storitve join kozmeticne_storitve on kozmeticne_storitve.id = racun_storitve.storitev
                                        where st_racuna = ?''', [racun]))

def izbraniIzdelki(racun):
        return list(con.execute('''select kozmeticni_izdelki.izdelek, kozmeticni_izdelki.cena
                                        from racun_izdelek join kozmeticni_izdelki on kozmeticni_izdelki.id = racun_izdelek.izdelek
                                        where st_racuna = ?''', [racun]))

def znesek(racun):
        return list(con.execute('''select racuni.znesek from racuni where id = ?''', [racun]))

        
def izpisImena(racun):
        return con.execute('''select ime, priimek from racuni join stranke on racuni.stranka = stranke.id where racuni.id = ? ''', [racun])

def izpisDatuma(racun):
        return con.execute('''select datum from racuni where id = ?''', [racun])
        
def zasedeni(leto, mesec, dan):
        return con.execute('''select ura, izvajalec from termin where leto = ? and mesec = ? and dan = ?''', [leto, mesec, dan])

def storitveZaposlenega(id_zaposlenega):
        storitve =  list(con.execute('''select kozmeticne_storitve.storitev from kozmeticne_storitve join izvaja on izvaja.storitev = kozmeticne_storitve.id where izvaja.zaposleni = ?''', [id_zaposlenega]))
        return storitve

def imenaStoritev(id_storitve):
        for i in range(len(id_storitve)):
                return list(con.execute('''select storitev from kozmeticne_storitve where id = ?''', [id_storitve[i]]))


def prosti_termini(leto, mesec, dan):
    vsi_mozni_izvajalci_storitve = list(con.execute('''select id, ime, priimek from zaposleni'''))
    zaseden = zasedeni(leto, mesec, dan)
    ze_zasedeni= {}
    for ura, izvajalec in zaseden:
            if ura not in ze_zasedeni.keys():
                    ze_zasedeni[ura]= [izvajalec]
            else:
                    ze_zasedeni[ura].append(izvajalec)
    na_voljo = {}
    for ura in range(8, 20):
            prosti = []
            for izvajalec in vsi_mozni_izvajalci_storitve:
                    if izvajalec['id'] not in ze_zasedeni.get(ura, []):
                            prosti.append(izvajalec)
            na_voljo[ura] = prosti
    return na_voljo

def rezerviraj(leto, mesec, dan, ura, id_zaposlenega, idOsebe):
        con.execute('''insert into termin (leto, mesec, dan, ura, izvajalec, stranka) VALUES (?,?,?,?,?,?)''', [leto, mesec, dan, ura, id_zaposlenega, idOsebe])
        con.commit()






        
        

        
        

