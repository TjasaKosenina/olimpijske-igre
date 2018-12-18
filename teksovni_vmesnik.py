
import modeli

def izberi_moznost(moznosti):
    """
    Funkcija, ki izpiše seznam možnosti in vrne indeks izbrane možnosti.
    Če na voljo ni nobene možnosti, izpiše opozorilo in vrne None.
    Če je na voljo samo ena možnost, vrne 0.
    >>> izberi_moznost(['jabolko', 'hruška', 'stol'])
    1) jabolko
    2) hruška
    3) stol
    Vnesite izbiro > 2
    1
    >>> izberi_moznost([])
    >>> izberi_moznost(['jabolko'])
    0
    """

    if len(moznosti) == 0:
        return
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print('{}) {}'.format(i, moznost))

        st_moznosti = len(moznosti)
        while True:
            izbira = input('Vnesite izbiro > ')
            if not izbira.isdigit():
                print('NAPAKA: vnesti morate število')
            else:
                n = int(izbira)
                if 1 <= n <= st_moznosti:
                    return n - 1
                else:
                    print('NAPAKA: vnesti morate število med 1 in {}!'.format(st_moznosti))

def izberi_olimpijske():
    niz = input('Vnesite leto olimpijskih iger: ')
    kljuc_olimpijskih = modeli.poisci_olimpijske(niz)
    return None if kljuc_olimpijskih is None else kljuc_olimpijskih[0]

def prikazi_podatke_OI():
    kljuc_olimpijskih = izberi_olimpijske()
    if kljuc_olimpijskih is None:
        print ('Nobene olimpijske igre ne ustrezajo podanemu letu.')
    else:
        zacetek, konec, mesto, st_drzav = modeli.podatki_olimpijske(kljuc_olimpijskih)
        print('začetek: {}, konec: {}'.format(zacetek, konec))
        print('  mesto: {}'.format(mesto))
        print('  število sodelujočih držav: {}'.format(st_drzav))


def izberi_osebo():
    niz = input('Vnesite del imena osebe: ')
    idji_oseb = modeli.poisci_osebe(niz)
    moznosti = [
        ime for (ime,_,_) in modeli.podatki_oseb(idji_oseb)
    ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_oseb[izbira]

def prikazi_podatke_osebe():
    id_osebe = izberi_osebo()
    if id_osebe is None:
        print('Nobena oseba ne ustreza iskalnemu nizu.')
    else:
        ime,priimek, disciplina, mesto  = modeli.podatki_osebe(id_osebe)
        print('{} {}'.format(ime,priimek))
        print('uvrstitev: {}, {}'.format(disciplina, mesto))
        
def izberi_disciplino():
    niz = input('Vnesite disciplino: ')
    kljuc_disciplina = modeli.poisci_discipline(niz)
    return None if kljuc_disciplina is None else kljuc_disciplina[0]

def prikazi_prvouvrscene_v_disciplini():
    kljuc_disciplina = izberi_disciplino()
    if kljuc_disciplina is None:
        print ('Disciplina ne obstaja.')
    elif modeli.podatki_disciplina(kljuc_disciplina) == []:
        print('V tej disciplini ni prvouvrščenih.')
    else:
        ime, priimek, leto = modeli.podatki_disciplina(kljuc_disciplina)
        print('{} {} {}'.format(ime, priimek, leto))


def pokazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke olipijskih iger',
        'prikaži podatke osebe',
        'prikaži podatke o prvouvrščenih v disciplini',
        'dodaj olimpijske igre',
        'preglej najslabše in najboljše športnike v disciplini',
        'preglej najsalbše in najboljše športnike v letu',
    ])
    
    if izbira == 0:
        prikazi_podatke_OI()
    elif izbira == 1:
        prikazi_podatke_osebe()
    elif izbira == 2:
        prikazi_prvouvrscene_v_disciplini()
    elif izbira == 3:
        ()
    elif izbira == 4:
        ()
    else:
        print('Nasvidenje!')
        exit()
        


def main():
    print('Pozdravljeni v bazi olimpisjkih iger!')
    while True:
        pokazi_moznosti()


main()

                    
