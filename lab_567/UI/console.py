from copy import deepcopy

from lab_567.Logic.CRUD import adauga_obiect, stergere_obiect, modifica_obiect, modificare_locatie, string_descriere, get_locatii, pret_maxim_locatie, lista_ordonata,suma_locatie
from lab_567.Domain.obiect import to_string

def print_menu():
    print("1. adaugare obiect")
    print("2. stergere obiect")
    print("3. modificare obiect")
    print("4. string cu toate descrierile obiectelor care au pretul mai mare ca o valaore data")
    print("5. modificare locatie oiecte")
    print("6. pretul maxim din fiecare locatie")
    print("7. ordonare obiecte dupa pret crescator")
    print("8. afisare suma preturilor din fiecare locatie")
    print("9. undo ")
    print("10. redo")
    print("a. afisare toate obiecte")
    print("x. iesire")
    print("0. Consola 2")
def ui_adaugare_obiect(inventar):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input("Dati pretul: "))
        locatie = input("Dati locatie: ")
        return adauga_obiect(id, nume, descriere, pret, locatie, inventar)
    except ValueError as ve:
        print("Operiatia nu a fost reusita: {}".format(ve))
    return inventar


def ui_stergere_obiect(inventar):
    id = input("dati id-ul obiectului pe care doriti sa il stergeti din inventar")
    return stergere_obiect(id,inventar)

def ui_modificare_obiect(invetar):
    try:
        id = input("Dati id-ul obiectului pecare doriti sa il modificati: ")
        nume = input("Dati numele nou: ")
        descriere = input("Dati descrierea noua: ")
        pret = float(input("Dati pretul nou: "))
        locatie = input("Dati locatie noua: ")
        return modifica_obiect(id, nume,descriere, pret, locatie, invetar)
    except ValueError as ve:
        print("Operiatia nu a fost reusita: {}".format(ve))
    return invetar

def show_all(inventar):
    for obiect in inventar:
        print(to_string(obiect))

def ui_modificare_locatie(inventar):
    locatie= input("Dati locatia locatie unde mutati obiectele: ")
    return modificare_locatie(locatie,inventar)

def ui_descriere(inventar):
    x = " "
    pret=input("dati pretul")
    for obiect in inventar:
            if str(string_descriere(obiect,pret)) != "None":
                x = x + str(string_descriere(obiect,pret)) + " "
    print(x)

def ui_pret_maxim_per_locatie(inventar):
    locatii=get_locatii(inventar)
    for locatie in locatii:
        print("Pretul maxim in",str(locatie),"este",str(pret_maxim_locatie(locatie,inventar)))

def ui_suma_pret_per_locatie(inventar):
    locatii = get_locatii(inventar)
    for locatie in locatii:
        print("suma preturilor din ", str(locatie), " este ", str(suma_locatie(locatie, inventar)))




def run_menu(inventar):
    undo_list=[]
    redo = []
    while True:
        print_menu()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            undo_list.append(inventar)
            fakeinventar=[]
            fakeinventar = deepcopy(inventar)
            inventar = ui_adaugare_obiect(inventar)
            if inventar == fakeinventar:
                inventar = undo_list.pop()
        elif optiune == "2":
            undo_list.append(inventar)
            fakeinventar=[]
            fakeinventar = deepcopy(inventar)
            inventar = ui_stergere_obiect(inventar)
            if inventar == fakeinventar:
                inventar = undo_list.pop()
                print("nu ati putut sterge obiectul deoarece obiectulcu id-ul dat nu exista (operatia nu va fii luata in calcul)")
        elif optiune == "3":
            undo_list.append(inventar)
            fakeinventar = []
            fakeinventar = deepcopy(inventar)
            inventar = ui_modificare_obiect(inventar)
            if inventar == fakeinventar:
                inventar = undo_list.pop()
                print("nu ati putut modifica obiectul cu id-ul dat deoarece acesta nu exista sau in urma modificari obiectul a rams la fel (operatia nu va fii luata in calcul)")
        elif optiune == "4":
            ui_descriere(inventar)
        elif optiune == "5":
            undo_list.append(inventar)
            fakeinventar = []
            fakeinventar = deepcopy(inventar)
            inventar = ui_modificare_locatie(inventar)
            if inventar == fakeinventar:
                inventar = undo_list.pop()
                print("ati ales ca locatie noua a obiectelor locatia actuala (operatia nu va fii luata in calcul)")
        elif optiune == "6":
            ui_pret_maxim_per_locatie(inventar)
        elif optiune == "7":
            inventar=lista_ordonata(inventar)

        elif optiune == "8":
            ui_suma_pret_per_locatie(inventar)
        elif optiune == "9":
            if len(undo_list) > 0:

                redo.append(inventar)
                inventar = undo_list.pop()

            else:
                print("Nu se poate face undo")
        elif optiune == "10":
            if len(redo) > 0:
                undo_list.append(inventar)
                inventar = redo.pop()
            else:
                print("Nu se paote face redo")
        elif optiune == "a":
            show_all(inventar)
        elif optiune == "0":
            inventar = run_menu_2(inventar)
        elif optiune == "x":
            break
        else:
            print("Optiunea data nu exista, incercati din nou")


def run_add(params, inventar):
    try:
        inventar = adauga_obiect(params[0], params[1], params[2], float(params[3]), params[4], inventar)
        return inventar
    except ValueError as ve:
        print("Operiatia nu a fost reusita: {}".format(ve))
    return inventar


def run_delete(id, inventar):
    inventar = stergere_obiect(id, inventar)
    return inventar


def run_update(params, inventar):
    try:
        inventar = modifica_obiect(params[0], params[1], params[2], float(params[3]), params[4], inventar)
        return inventar
    except ValueError as ve:
        print("Operiatia nu a fost reusita: {}".format(ve))
    return inventar

def print_usage():
    usage = """
Instructiuni:    
    Adaugare: add,[id],[nume],[descriere],[pret],[locatie]
    Stergere: delete,[id]
    Modificare: update,[id],[nume],[descriere],[pret],[locatie]
    Afisare: showall
    Meniu: help
    Consola 1: exit
    Undo:U
    Redo:R
!!! a se pune doar ";" intre instructiuni

"""
    print(usage)


def run_menu_2(inventar):
    undo_list=[]
    redo = []
    print_usage()
    should_run = True

    while should_run:
        optiuni = input("input: ")
        optiuni = optiuni.split(";")
        for optiune in optiuni:
                optiune = optiune.split(",")

                if optiune[0] == "exit":
                    should_run = False
                    break
                elif optiune[0] == "help":
                    print_usage()
                elif optiune[0] == "showall":
                    show_all(inventar)

                elif optiune[0] == "add":
                    undo_list.append(inventar)
                    fakeinventar = []
                    fakeinventar = deepcopy(inventar)
                    inventar = run_add(optiune[1:], inventar)
                    if inventar == fakeinventar:
                        inventar = undo_list.pop()
                elif optiune[0] == "delete":
                    inventar = run_delete(optiune[1], inventar)
                elif optiune[0] == "update":
                    undo_list.append(inventar)
                    fakeinventar = []
                    fakeinventar = deepcopy(inventar)
                    inventar = run_update(optiune[1:], inventar)
                    if inventar == fakeinventar:
                        inventar = undo_list.pop()
                elif optiune[0] == "U":
                    if len(undo_list) > 0:

                        redo.append(inventar)
                        inventar = undo_list.pop()

                    else:
                        print("Nu se poate face undo")
                elif optiune[0] == "R":
                    if len(redo) > 0:
                        undo_list.append(inventar)
                        inventar = redo.pop()
                    else:
                        print("Nu se paote face redo")

                else:
                    print("Optiune inexistenta")
    return inventar

