from lab_567.Domain.obiect import creeaza_obiect, get_Id

def adauga_obiect(id, nume, descriere, pret, locatie,inventar):
    """
    adauga un obiect in inventar (in lista)
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :return: o lista continand lista veche plus noul obiect
    """
    obiect = creeaza_obiect(id,nume,descriere,pret,locatie)
    return inventar + [obiect]

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

def modifica_obiect(id, nume, descriere, pret, locatie,inventar):
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
