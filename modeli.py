<<<<<<< HEAD
import baza
import sqlite3

conn = sqlite3.connect('olimpijske-igre.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

def poisci_olimpijske(letoPodano):
    """
    Funkcija, ki vrne kljuc
    >>> poisci_olimpijske('1948')
    11
    """
    poizvedba = """
        SELECT kljuc
        FROM olimpijske_igre
        WHERE letoPodano = leto
    """
    return conn.execute(poizvedba, letoPodano)



def podatki_olimpijske(kljucPodan):
    """
    Funkcija, ki vrne začetek, konec, kraj OI in stevilo drzav
    >>> poisci_olimpijske('11')
    [29.7., 14.8., London, 44]
    """
    poizvedba = """
        SELECT zacetek, konec, mesto, st_drzav
        FROM olimpijske_igre
        WHERE kljuc == kljucPodan
    """
    return conn.execute(poizvedba, kljucPodan)



def poisci_osebe(niz):
    """
    Funkcija, ki vrne IDje vseh oseb, katerih ime vsebuje dani niz.
    >>> poisci_osebe('elia')
    [8, 42, 457, 497]
    """
    poizvedba = """
        SELECT id
        FROM osebe
        WHERE ime LIKE ?
        ORDER BY ime
    """
    idji_oseb = []
    for (id_osebe,) in conn.execute(poizvedba, ['%' + niz + '%']):
        idji_oseb.append(id_osebe)
    return idji_oseb


def podatki_oseb(id_oseb):
    """
    Vrne osnovne podatke vseh oseb z danimi IDji.
    >>> podatki_oseb([8, 42, 457, 497])
    [(8, 'Belia Verduin'), (42, 'Othelia Scullion'), (457, 'Delia Louden'), (497, 'Rafaelia Lambot')]
    """
    poizvedba = """
        SELECT id, ime, priimek
        FROM osebe
        WHERE id IN ({})
    """.format(','.join('?' for _ in range(len(id_oseb))))
    return conn.execute(poizvedba, id_oseb).fetchall()

def podatki_osebe(id_osebe):
    """
    Vrne podatke o osebi z danim IDjem.
    >>> podatki_osebe(8)
    ('Belia Verduin', )
    """
    poizvedba = """
        SELECT ime FROM osebe WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_osebe])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        ime,priimek = osnovni_podatki
        poizvedba_za_podatke = """
            SELECT discipline.disciplina, uvrstitve.mesto
            FROM uvrstitve
                 JOIN osebe ON uvrstitve.id_osebe = osebe.id
                 JOIN discipline ON discipline.id = uvrstitve.id_discipline
            WHERE osebe.id = ?
            ORDER BY uvrstitve.mesto
        """
        disciplina, mesto = conn.execute(poizvedba_za_podatke, [id_osebe]).fetchall()
    return ime, priimek, disciplina, mesto
=======
import baza
import sqlite3

conn = sqlite3.connect('olimpijske-igre.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

def poisci_olimpijske(letoPodano):
    """
    Funkcija, ki vrne kljuc
    >>> poisci_olimpijske('1948')
    11
    """
    poizvedba = """
        SELECT kljuc
        FROM olimpijske_igre
        WHERE letoPodano == leto
    """
    return conn.execute(poizvedba, letoPodano)



def podatki_olimpijske(kljucPodan):
    """
    Funkcija, ki vrne začetek, konec, kraj OI in stevilo drzav
    >>> poisci_olimpijske('11')
    [29.7., 14.8., London]
    """
    poizvedba = """
        SELECT zacetek, konec, mesto, st_drzav
        FROM olimpijske_igre
        WHERE kljuc == kljucPodan
    """
    return conn.execute(poizvedba, kljucPodan)



def poisci_osebe(niz):
    """
    Funkcija, ki vrne IDje vseh oseb, katerih ime vsebuje dani niz.
    >>> poisci_osebe('elia')
    [8, 42, 457, 497]
    """
    poizvedba = """
        SELECT id
        FROM osebe
        WHERE ime LIKE ?
        ORDER BY ime
    """
    idji_oseb = []
    for (id_osebe,) in conn.execute(poizvedba, ['%' + niz + '%']):
        idji_oseb.append(id_osebe)
    return idji_oseb


def podatki_oseb(id_oseb):
    """
    Vrne osnovne podatke vseh oseb z danimi IDji.
    >>> podatki_oseb([8, 42, 457, 497])
    [(8, 'Belia Verduin'), (42, 'Othelia Scullion'), (457, 'Delia Louden'), (497, 'Rafaelia Lambot')]
    """
    poizvedba = """
        SELECT id, ime, priimek
        FROM osebe
        WHERE id IN ({})
    """.format(','.join('?' for _ in range(len(id_oseb))))
    return conn.execute(poizvedba, id_oseb).fetchall()

def podatki_osebe(id_osebe):
    """
    Vrne podatke o osebi z danim IDjem.
    >>> podatki_osebe(8)
    ('Belia Verduin', )
    """
    poizvedba = """
        SELECT ime FROM osebe WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_osebe])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        ime, = osnovni_podatki
        poizvedba_za_podatke = """
            SELECT uvrstitve.disciplina, uvrstitve.mesto
            FROM uvrstitve
                 JOIN osebe ON uvrstitve.id_osebe = osebe.id
            ORDER BY uvrstitve.mesto
        """
        #??????????????????????????
        disciplina, mesto = conn.execute(poizvedba_za_podatke, [id_osebe]).fetchall()
    return ime, disciplina, mesto
>>>>>>> 34d3739fe850e4d8056f38c77f6a0ae6619b9361
