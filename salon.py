from bottle import *
import baza

meseci = ['Januar', 'Februar', 'Marec', 'April', 'Maj','Junij','Julij','Avgust','September','Oktober','November','December']

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
    return template('termini',
        meseci = meseci,
                    
        kozmeticne_storitve = baza.seznamStoritev(),

        
                    )

@post('/termini/')
def termini_post():
    mesec = request.forms.mesec
    izbraniDan = request.forms.dan
    storitev = request.forms.storitev
    izvajalciZaStoritev = baza.izvjalciZaStoritev(storitev)
 


    
    redirect('/')
    
    

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


@route('/znesek/')
def znesek():
    return template('znesek',
                    storitve = baza.izbraneStoritve()
                    #izdelki = baza.izbraniIzdelki(),
                    #znesek = baza.znesek()
                )


                    
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='static')


run(debug=True)
