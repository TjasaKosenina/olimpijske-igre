import csv


def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS olimpijske_igre;")
    conn.execute("DROP TABLE IF EXISTS osebe;")
    conn.execute("DROP TABLE IF EXISTS sporti;")
    conn.execute("DROP TABLE IF EXISTS sporti_discipline;")
    conn.execute("DROP TABLE IF EXISTS uvrstitve;")
    conn.execute("DROP TABLE IF EXISTS discipline;")


def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    conn.execute("""
        CREATE TABLE olimpijske_igre (
            kljuc     INTEGER PRIMARY KEY,
            leto      INTEGER,
            mesto     TEXT,
            zacetek   TEXT,
            konec     TEXT,
            st_drzav  INTEGER
        );
    """)
    conn.execute("""
        CREATE TABLE osebe (
            id      INTEGER PRIMARY KEY,
            ime     TEXT,
            priimek TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE sporti (
            kljuc    INTEGER PRIMARY KEY,
            sport    TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE discipline (
            id              INTEGER PRIMARY KEY,
            disciplina      TEXT,
            id_sport           INTEGER REFERENCES sporti(kljuc)
        );
    """)
    conn.execute("""
        CREATE TABLE uvrstitve (
            mesto           INTEGER,
            id_osebe        INTEGER REFERENCES osebe(id),
            id_disciplina   INTEGER REFERENCES discipline(id),
            kljuc_leto      INTEGER REFERENCES olimpijske_igre(kljuc),
            PRIMARY KEY (id_osebe, id_discipline, kljuc_leto)
        );
    """)

def uvozi_olimpijske_igre(conn):
    """
    Uvozi podatke o olimpijskih igrah.
    """
    conn.execute("DELETE FROM olimpijske_igre;")
    with open('Podatki/olimpijske_igre.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO olimpijske_igre VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_osebe(conn):
    """
    Uvozi podatke o osebah.
    """
    conn.execute("DELETE FROM osebe;")
    with open('Podatki/osebe.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO osebe VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_sporte(conn):
    """
    Uvozi podatke o sportih.
    """
    conn.execute("DELETE FROM sporti;")
    with open('Podatki/sporti.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO sporti VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_discipline(conn):
    """
    Uvozi podatke o disciplinah.
    """
    conn.execute("DELETE FROM discipline;")
    with open('Podatki/discipline.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO discipline VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_uvrstitve(conn):
    """
    Uvozi podatke o uvrstitvah.
    """
    conn.execute("DELETE FROM uvrstitve;")
    with open('Podatki/uvrstitve.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO uvrstitve VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_olimpijske_igre(conn)
    uvozi_osebe(conn)
    uvozi_sporte(conn)
    uvozi_discipline(conn)
    uvozi_uvrstitve(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
ustvari_bazo(conn)