from copy import deepcopy

from lab_567.Logic.CRUD import adauga_obiect, stergere_obiect, modifica_obiect, modificare_locatie, string_descriere, get_locatii, pret_maxim_locatie, lista_ordonata,suma_locatie
from lab_567.Domain.obiect import to_string

def print_menu():
    print("1. adaugare obiect")
    print("2. stergere obiect")
    print("3. modificare obiect")
    print("4. string cu toate descrierile obiectelor care au pretul mai mare ca o valaore data")
    print("5 modificare locatie oiecte")
    print("6. pretul maxim din fiecare locatie")
    print("7. ordonare obiecte dupa pret crescator")
    print("8. afisare sumapreturilor din fiecare locatie")
    print("9. undo la ultima actiune de modificare a inventarului")
    print("10. redo")
    print("a. afisare toate obiecte")
    print("x. iesire")

def ui_adaugare_obiect(inventar):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul: "))
    locatie = input("Dati locatie: ")
    return adauga_obiect(id,nume,descriere,pret,locatie,inventar)

def ui_stergere_obiect(inventar):
    id = input("dati id-ul obiectului pe care doriti sa il stergeti din inventar")
    return stergere_obiect(id,inventar)

def ui_modificare_obiect(invetar):
    id = input("Dati id-ul obiectului pecare doriti sa il modificati: ")
    nume = input("Dati numele nou: ")
    descriere = input("Dati descrierea noua: ")
    pret = float(input("Dati pretul nou: "))
    locatie = input("Dati locatie noua: ")
    return modifica_obiect(id, nume,descriere, pret, locatie, invetar)

def show_all(inventar):
    for obiect in inventar:
        print(to_string(obiect))

def ui_modificare_locatie(inventar):
    locatie= input("Dati locatia locatie unde mutati obiectele")
    return modificare_locatie(locatie,inventar)

def ui_descriere(inventar):
    x = " "
    pret=input("dati pretul")
    for obiect in inventar:
        x = x + str(string_descriere(obiect,pret))
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
            undo_list.append(inventar)
            inventar = redo.pop()

        elif optiune == "a":
            show_all(inventar)
        elif optiune == "x":
            break
        else:
            print("Optiunea data nu exista, incercati din nou")


