from bottle import *
import baza


@route('/')
def domaca_stran():
    return template(
        'zacetna_stran'
        )

@route('/termini/')
def termini():
    return template(
        'termini'
        )

@get('/narocanje/<leto:int>/<mesec:int>/<dan:int>/')
def narocanje(leto, mesec, dan):
    return template('narocanje', {
        'dan': dan,
        'mesec': mesec,
        'leto': leto,
        'termini': baza.prosti_termini(leto, mesec, dan)
    })

@get('/narocanje/<leto:int>/<mesec:int>/<dan:int>/<ura:int>/<id_zaposlenega:int>/')
def izvajalec(leto, mesec, dan, ura, id_zaposlenega):
    return template('izvajalec',
                    {
                'dan': dan,
                'mesec': mesec,
                'leto': leto,
                 'ura':ura,
                'id_zaposlenega': id_zaposlenega},
            storitve = baza.storitveZaposlenega(id_zaposlenega))

@post('/narocanje/<leto:int>/<mesec:int>/<dan:int>/<ura:int>/<id_zaposlenega:int>/')
def izvajalec(leto, mesec, dan, ura, id_zaposlenega):
    
    ime = request.forms.ime
    priimek = request.forms.priimek
    idOsebe = baza.idOsebe(ime, priimek)
    baza.rezerviraj(leto, mesec, dan, ura, id_zaposlenega, idOsebe)
    redirect('/')
    

@route('/izdelki/')
def seznam_izdelkov():
    return template('izdelki',
        kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@route('/izdelki/dodajIzdelek/')
def dodajIzdelek():
    return template('dodajIzdelek', ime = "", cena = "", zaloga = "")


@route('/izdelki/dodajIzdelek/', method = 'POST' )
def dodajIzdelek():
    ime = request.forms.ime
    cena = request.forms.cena
    zaloga = request.forms.zaloga
    baza.dodajIzdelek(ime, cena, zaloga)
    redirect('/')

@route('/storitve/dodajStoritev/')
def dodajStoritev():
    return template('dodajStoritev', ime = "", cena = "", cas = "", izvajalci = baza.seznamIzvajalcev())

@route('/storitve/dodajStoritev/', method = 'POST' )
def dodajStoritev():
    ime = request.forms.ime
    cena = request.forms.cena
    cas = request.forms.cas
    izvajalci = request.forms.izvajalec
    baza.dodajStoritev(ime, cena, cas)
    zaposleni = int(izvajalci)
    storitev = baza.idStoritve(ime)
    baza.dodajIzvajalca(storitev, zaposleni)
    redirect('/')

@route('/izdelki/spremeniCeno/', method = 'GET')
def spremeniCeno():
    return template('spremeniCeno',
                    kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@route('/izdelki/spremeniCeno/', method = 'POST' )
def spremeniCeno():
    id_izdelka = int(request.forms.izdelek)
    cena = request.forms.cena
    baza.spremeniCeno(cena, id_izdelka)
    redirect('/')

@route('/izdelki/izbrisiIzdelek/', method = 'GET')
def izbrisiIzdelek():
    return template('izbrisiIzdelek',
                    kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@route('/izdelki/izbrisiIzdelek/', method = 'POST')
def izbrisiIzdelek():
    id_izdelka = int(request.forms.izdelek)
    baza.izbrisiIzdelek(id_izdelka)
    redirect('/')
       
@route('/storitve/odstraniStoritev/', method = 'GET')
def odstraniStoritev():
    return template('odstraniStoritev',
                    kozmeticne_storitve = baza.seznamStoritev()
                    )

@route('/storitve/odstraniStoritev/', method = 'POST')
def odstraniStoritev():
    id_storitve = int(request.forms.storitev)
    baza.odstraniStoritev(id_storitve)
    baza.odstraniIzvajalca(id_storitve)
    redirect('/')


@route('/storitve/spremeniCenoS/', method = 'GET')
def spremeniCenoS():
    return template('spremeniCenoS',
                    kozmeticne_storitve = baza.seznamStoritev()
                    )

@route('/storitve/spremeniCenoS/', method = 'POST' )
def spremeniCenoS():
    cena = request.forms.cena
    id_storitve = request.forms.storitev
    baza.spremeniCenoS(cena, id_storitve)
    redirect('/')



@route('/izdelki/spremeniZalogo/', method = 'GET')
def spremeniZalogo():
    return template('spremeniZalogo',
                    kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@route('/izdelki/spremeniZalogo/', method = 'POST' )
def spremeniZalogo():
    id_izdelka = int(request.forms.izdelek)
    zaloga = request.forms.zaloga
    baza.spremeniZalogo(zaloga, id_izdelka)
    redirect('/')


@route('/storitve/spremeniIzvajalca/', method = 'GET')
def spremeniIzvajalca():
    return template('spremeniIzvajalca',
                    kozmeticne_storitve = baza.seznamStoritev(),
                    izvajalci = baza.idZaposlenega()
                    )


@route('/storitve/spremeniIzvajalca/', method = 'POST' )
def spremeniIzvajalca():
    id_storitve = request.forms.storitev
    id_izvajalca = request.forms.izvajalec
    baza.spremeniIzvajalca(id_storitve, id_izvajalca)
    redirect('/')


@route('/storitve/')
def seznam_storitev():
    return template('storitve',
        kozmeticne_storitve = baza.seznamStoritev()
                    )

@route('/racun/')
def racun():
    return template('racun',
        kozmeticne_storitve = baza.seznamStoritev(),
        kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@post('/racun/')
def racun_post():
    ime = request.forms.ime
    priimek = request.forms.priimek
    dat = request.forms.datum
    storitve = request.forms.getall('storitve')
    izdelki = request.forms.getall('izdelki')

    oseba = baza.idOsebe(ime, priimek)
    racun = baza.vnesiRacun(dat, oseba, izdelki, storitve)

    redirect('/znesek/{}/'.format(racun))

@route('/znesek/<racun:int>/')
def znesek(racun):
    return template('znesek',
                    storitve = baza.izbraneStoritve(racun),
                    izdelki = baza.izbraniIzdelki(racun),
                    oseba = baza.izpisImena(racun),
                    datum = baza.izpisDatuma(racun),
                    znesek = baza.znesek(racun)
                )
                    
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='static')


run(debug=True)
