from bottle import *
import baza


@route('/')
def domaca_stran():
    return template(
        'zacetna_stran'
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
    baza.vnesiRacun(dat, oseba, izdelki, storitve)

    redirect('/')
                    
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='/path/to/image/files', mimetype='image/png')


run(debug=True)
