import bottle
from bottle import get, post, run, template, request, redirect
import modeli
import hashlib
import random

SKRIVNOST = 'moja skrivnost'

def prijavljen_uporabnik():
    return request.get_cookie('prijavljen', secret=SKRIVNOST) == 'da'

def url_leto(id):
    return '/leto/{}/'.format(id)


@get('/')
def glavna_stran():
    leto = [
        (leto, '/olimpijske_igre/{}/'.format(leto))
        for leto in modeli.mozna_leta()
    ]
    return template(
        'glavna_stran',
        leto = leto,
        prijavljen=prijavljen_uporabnik()
    )

@get('/olimpijske_igre/<leto:int>/')
def podatki_olimpijskih_iger(leto):
    indeks = modeli.poisci_olimpijske(leto)
    zacetek, konec, mesto, st_drzav = modeli.podatki_olimpijske(indeks)
    return template(
        'podatki_olimpijskih_iger',
        leto = leto,
        zacetek = zacetek,
        konec = konec,
        mesto = mesto,
        st_drzav = st_drzav
)

@get('/iskanjeTekmovalcev/')
def iskanjeTekmovalcev():
    niz = request.query.tekmovalec
    idji_oseb = modeli.poisci_osebe(niz)
    #podatki = modeli.podatki_osebe(idji_oseb)
    podatki = [modeli.podatki_osebe(id_osebe) for id_osebe in idji_oseb]
    return template(
        'rezultati_iskanja_tekmovalcev',
        niz=niz,
        podatki = podatki,
)

@get('/iskanjeDiscipline/')
def iskanjeDisciplin():
    niz = request.query.disciplina
    id_discipline = modeli.poisci_discipline(niz) 
    if id_discipline is None:
        return template(
            'disciplina_ne_obstaja',
            niz = niz
        )
    id_discipline, = id_discipline
    podatki = modeli.podatki_disciplina(id_discipline)
    if len(podatki) == 0:
        return template(
            'rezultati_ni_prvouvrscenih',
            niz = niz,
        )
    else:
        return template(
            'rezultati_iskanja_discipline',
            niz=niz,
            podatki = podatki,
        )

@get('/dodaj_OI/')
def dodaj_OI():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template('dodaj_OI',
                    leto="",
                    mesto="",
                    zacetek="",
                    konec="",
                    st_drzav="",
                    napaka=False)


@post('/dodaj_OI/')
def dodajanje_OI():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    try:
        id = modeli.dodaj_OI(leto=request.forms.leto,
                            mesto=request.forms.mesto,
                            zacetek=request.forms.zacetek,
                            konec=request.forms.konec,
                            st_drzav=request.forms.st_drzav)
    except:
        return template('dodaj_OI',
                        leto=request.forms.leto,
                        mesto=request.forms.mesto,
                        zacetek=request.forms.zacetek,
                        konec=request.forms.konec,
                        st_drzav=request.forms.st_drzav,
                        napaka=True)
    redirect('/olimpijske_igre/{}/'.format(request.forms.leto))

@post('/prijava/')
def prijava():
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    if modeli.preveri_geslo(uporabnisko_ime, geslo):
        bottle.response.set_cookie(
            'prijavljen', 'da', secret=SKRIVNOST, path='/')
        redirect('/')
    else:
        raise bottle.HTTPError(403, "BOOM!")

@get('/odjava/')
def odjava():
    bottle.response.set_cookie('prijavljen', '', path='/')
    redirect('/')

@post('/registracija/')
def registracija():
    uporabnisko_ime = request.forms.uporabnisko_ime
    geslo = request.forms.geslo
    if modeli.ustvari_uporabnika(uporabnisko_ime, geslo):
        bottle.response.set_cookie(
            'prijavljen', 'da', secret=SKRIVNOST, path='/')
        redirect('/')
    else:
        raise bottle.HTTPError(
            403, "Uporabnik s tem uporabniškim imenom že obstaja!")

run(reloader=True, debug=True)