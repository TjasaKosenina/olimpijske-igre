import baza
import sqlite3
import random
import hashlib

conn = sqlite3.connect('olimpijske-igre.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

def mozna_leta():
    poizvedba = """
        SELECT leto 
        FROM olimpijske_igre
    """
    leta = conn.execute(poizvedba)
    return [leto for leto, in leta]

def poisci_olimpijske(letoPodano):
    """
    Funkcija, ki vrne kljuc
    >>> poisci_olimpijske('1948')
    11
    """
    poizvedba = """
        SELECT kljuc
        FROM olimpijske_igre
        WHERE leto = ?
    """
    indeks, = conn.execute(poizvedba, [letoPodano]).fetchone()
    return indeks



def podatki_olimpijske(kljucPodan):
    """
    Funkcija, ki vrne začetek, konec, kraj OI in stevilo drzav.
    >>> poisci_olimpijske('11')
    [29.7., 14.8., London, 44]
    """
    poizvedba = """
        SELECT zacetek, konec, mesto, st_drzav
        FROM olimpijske_igre
        WHERE kljuc = ?
    """
    return conn.execute(poizvedba, [kljucPodan]).fetchone()
    

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
        SELECT ime,priimek FROM osebe WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_osebe])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        ime,priimek = osnovni_podatki
        poizvedba_za_podatke = """
            SELECT sporti.sport, discipline.disciplina, uvrstitve.mesto
            FROM uvrstitve
                 JOIN osebe ON uvrstitve.id_osebe = osebe.id
                 JOIN discipline ON discipline.id = uvrstitve.id_disciplina
                 JOIN sporti ON sporti.kljuc = discipline.id_sport 
            WHERE osebe.id = ?
            ORDER BY uvrstitve.mesto
        """
        uvrstitve = conn.execute(poizvedba_za_podatke, [id_osebe]).fetchall()
    return ime, priimek, uvrstitve

def poisci_discipline(disciplina):
    """
    Funkcija, ki vrne ID discipline.
    >>> poisci_discipline('krogla')
    [9]
    """
    poizvedba = """
        SELECT id
        FROM discipline
        WHERE disciplina = ?
    """
    return conn.execute(poizvedba, [disciplina]).fetchone()

def podatki_disciplina(id_disciplina):
    """
    Vrne podatke o prvouvrščenih osebah v dani disciplini z danim IDjem.
    >>> podatki_disciplina(100m delfin)
    (Crissy Keyhoe (1976) )
    """
    poizvedba = """
        SELECT osebe.ime, osebe.priimek, olimpijske_igre.leto 
        FROM osebe 
            JOIN uvrstitve ON osebe.id = uvrstitve.id_osebe
            JOIN olimpijske_igre ON olimpijske_igre.kljuc = uvrstitve.kljuc_leto
        WHERE id_disciplina = ? AND uvrstitve.mesto == 1 
    """
    osebe = []
    for ime,priimek,leto in conn.execute(poizvedba, [id_disciplina]):
        osebe.append((ime,priimek,leto))
    return osebe

def dodaj_OI(leto, mesto, zacetek, konec, st_drzav):
    with conn:
        id = conn.execute("""
            INSERT INTO olimpijske_igre (leto, mesto, zacetek, konec, st_drzav)
                                        VALUES (?,?,?,?,?)
        """,[leto, mesto, zacetek, konec, st_drzav]).lastrowid
        return id

def zakodiraj(geslo, sol=None):
    if sol is None:
        sol = ''.join(chr(random.randint(65, 122)) for _ in range(16))
    posoljeno_geslo = geslo + '$' + sol
    zakodirano_geslo = hashlib.sha512(posoljeno_geslo.encode()).hexdigest()
    return zakodirano_geslo, sol


def preveri_geslo(uporabnisko_ime, geslo):
    poizvedba = """
        SELECT geslo, sol FROM uporabniki
        WHERE uporabnisko_ime = ?
    """
    uporabnik = conn.execute(poizvedba, [uporabnisko_ime]).fetchone()
    if uporabnik is None:
        return False
    shranjeno_geslo, sol = uporabnik
    zakodirano_geslo, _ = zakodiraj(geslo, sol)
    return shranjeno_geslo == zakodirano_geslo


def ustvari_uporabnika(uporabnisko_ime, geslo):
    poizvedba = """
        INSERT INTO uporabniki
        (uporabnisko_ime, geslo, sol)
        VALUES (?, ?, ?)
    """
    with conn:
        zakodirano_geslo, sol = zakodiraj(geslo)
        conn.execute(poizvedba, [uporabnisko_ime, zakodirano_geslo, sol]).fetchone()
        return True