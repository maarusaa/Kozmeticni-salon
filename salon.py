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

##@route('/storitev/<storitev>/kozmeticni_salon')
##def urnik_letnika(letnik):
##    return template(
##        'storitve',
##        srecanja=modeli.urnik_letnika(letnik)
##    )
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
