import bottle
from bottle import get, post, run, template, request, redirect
import modeli
import hashlib

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
    podatki = modeli.podatki_disciplina(id_discipline)
    return template(
        'rezultati_iskanja_discipline',
        niz=niz,
        podatki = podatki,
)

run(reloader=True, debug=True)