from bottle import *
import baza


@route('/')
def domaca_stran():
    return template(
        'zacetna_stran',
##        storitve=baza.kozmeticne_storitve(),
##        izdelki=baza.kozmeticni_izdelki(),
##        zaposleni=baza.zaposleni(),
##        termini = baza.termin()
    )

@route('/izdelki/')
def seznam_izdelkov():
    return template('izdelki',
        kozmeticni_izdelki = baza.seznamIzdelkov()
                    )

@route('/storitve/')
def seznam_storitev():
    return template('storitve',
        kozmeticne_storitve = baza.seznamStoritev()
                    )

@route('/termini/')
def termini():
    return template('termini')

@route('/racun/')
def termini():
    return template('racun',
        kozmeticne_storitve = baza.seznamStoritev(),
        kozmeticni_izdelki = baza.seznamIzdelkov()
                    )
                    
##
##
##@route('/izdelki/<izdelki>/kozmeticni_salon')
##def urnik_osebe(oseba):
##    return template(
##        'izdelki',
##        srecanja=modeli.urnik_osebe(oseba)
##    )
##
##
##@route('/termini/<termini>/kozmeticni_salon')
##def urnik_ucilnice(ucilnica):
##    return template(
##        'termini',
##        srecanja=modeli.urnik_ucilnice(ucilnica)
##    )


run(debug=True)
