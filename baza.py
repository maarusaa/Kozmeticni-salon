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
        (SELECT sum(cena) FROM racun_storitve JOIN kozmeticne_storitve ON racun_storitve.storitev = id WHERE st_racuna = ?)''', [racun, racun])
        con.commit()
        
def idIzdelka(izdelek):
        '''funkcija vrne id izdelka.'''
        return  con.execute('''select id from kozmeticni_izdelki where izdelek = ?''', [izdelek])
        
def idStoritve(storitev):
        '''funkcija vrne id storitve'''
        return  con.execute('''select id from kozmeticne_storitve where storitev = ?''', [storitev])
        
def idOsebe(ime, priimek):
        '''vstavi novo osebo v tabelo stranke in vrne id'''
        oseba = con.execute('''select id from stranke where ime = ? and priimek = ?''', [ime, priimek]).fetchone()#nam vrne osebo ali None, ce ga se ni v bazi
        if oseba is not None:
                return oseba['id']
        else:
                cur = con.execute('''insert into stranke (ime, priimek) VALUES (?, ?)''', [ime, priimek])
                con.commit()
                return cur.lastrowid

		
	
def seznamIzdelkov():
	return list(con.execute('''select id, cena, izdelek from kozmeticni_izdelki'''))

def seznamStoritev():
	return list(con.execute('''select id, cena, storitev, cas from kozmeticne_storitve'''))
        

def prosti_termini(storitev, dan, teden):
        '''funkcija vrne slovar slovarjev.''' 
        vsi_mozni_izvajalci_storitve = con.execute('''select id from zaposleni''')
        na_voljo = {dan:{ura: set(vsi_mozni_izvajalci_storitve) for ura in range(8,21)} for dan in ['ponedeljek', 'torek', 'sreda', 'cetrtek', 'petek']}

        for termin in ze_zasedeni_termini_v_tem_tednu:
                na_voljo[dan].remove(termin)
                
                #pobrisi termin iz na_voljo


        

        
        

        
        

