from lab_567.Domain.obiect import creeaza_obiect, get_Id, get_nume, get_pret, get_descriere, get_locatie


def adauga_obiect(id, nume, descriere, pret, locatie, inventar):
    """
    adauga un obiect in inventar (in lista)
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :return: o lista continand lista veche plus noul obiect
    """
    ok = 1
    for obiect in inventar:
        if get_Id(obiect) == id:
            print(
                "Obiectul nu a putut fii adaugat, aveti deja un obiect cu acest id in inventar (operatia nu va fii luata in calcul)")
            ok = 0
    if ok == 1:
        obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
        return inventar + [obiect]
    else:
        return inventar


def get_by_Id(id, inventar):
    """
    ia obiectul cu id-ul dat din inventar (dintr-olista)
    :param id:string
    :param inventar: lista de obiecte
    :return: obiectul cu id-ul dat sau None daca nu exista nici un obiect cu id-ul dat
    """
    for obiect in inventar:
        if get_Id(obiect) == id:
            return obiect
    return None


def stergere_obiect(id, inventar):
    """
    sterge un obiect din inventar
    :param id: string
    :param inventar: lista de obiecte
    :return: inventarul fara obiectulcu id-ul dat (o lista)
    """
    return [obiect for obiect in inventar if get_Id(obiect) != id]


def modifica_obiect(id, nume, descriere, pret, locatie, inventar):
    """
    modifica un obiect din inventar cu id-ul din parametru
    :param id: modifica obiectul cu acest id (string)
    :param nume: nume nou pt obiect id (string)
    :param descriere:
    :param pret:
    :param locatie: locatie noua pt obiect id (string)
    :param inventar:
    :return: inventar cu obiect cu id din parametru modificat (lista)
    """
    inventar_nou = []
    for obiect in inventar:
        if get_Id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            inventar_nou.append(obiect_nou)
        else:
            inventar_nou.append(obiect)
    return (inventar_nou)


def modificare_locatie(locatie, inventar):
    """
    modifica locatia tuturor obiectelor din lista
    :param locatie: string
    :param inventar: lista
    :return: lista noua
    """
    inventar_nou = []
    for obiect in inventar:
        id1 = get_Id(obiect)
        nume1 = get_nume(obiect)
        descriere1 = get_descriere(obiect)
        pret1 = get_pret(obiect)
        obiect_nou = creeaza_obiect(id1, nume1, descriere1, pret1, locatie)
        inventar_nou.append(obiect_nou)
    return (inventar_nou)


def string_descriere(obiect, pret):
    """
    returneazaa descrierea unui obiect daca acesta are prtul maiamre decat o valaore data
    :param obiect:
    :param pret: numar care o sa devina float
    :return: string
    """
    if get_pret(obiect) > float(pret):
        return str(get_descriere(obiect))


def get_locatii(inventar):
    """

    :param inventar: lista
    :return: lista cu locatiile obiectelor din inventar
    """
    locatii = []
    for obiect in inventar:
        ok = 1
        for locatie in locatii:
            if get_locatie(obiect) == locatie:
                ok = 0
        if ok == 1:
            locatii.append(get_locatie(obiect))
    return locatii


def pret_maxim_locatie(locatie, inventar):
    """
    gaseste pretul maxim a obiectelordintr-o locatie
    :param locatie: string
    :param inventar: lista
    :return: flaot
    """
    maxim = 0
    for obiect in inventar:
        if get_locatie(obiect) == locatie:
            if get_pret(obiect) > maxim:
                maxim = get_pret(obiect)
    return maxim


def pret_minim(inventar):
    mimin = get_pret(inventar[0])
    for obiect in inventar:
        if get_pret(obiect) < mimin:
            mimin = get_pret(obiect)
    return mimin


def lista_ordonata(inventar):
    inventar_sortat = []
    while inventar != []:
        for obiect in inventar:
            if get_pret(obiect) == pret_minim(inventar):
                inventar_sortat.append(obiect)
                inventar.remove(obiect)
    return inventar_sortat


def suma_locatie(locatie, inventar):
    s = 0
    for obiect in inventar:
        if get_locatie(obiect) == locatie:
            s = s + get_pret(obiect)
    return s
