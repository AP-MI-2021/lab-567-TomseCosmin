from lab_567.Domain.obiect import *
from lab_567.Logic.CRUD import adauga_obiect, stergere_obiect, get_by_Id, modificare_locatie


def test_adauga_obiect():
    inventar = adauga_obiect("id1", "nume1", "descriere1", "pret1", "locatie1", [])
    inventar = adauga_obiect("id2", "nume2", "descriere2", "pret2", "locatie2", inventar)
    assert get_Id(inventar[0])=="id1"
    assert get_nume(inventar[0]) == "nume1"
    assert get_descriere(inventar[0]) == "descriere1"
    assert get_pret(inventar[0]) == "pret1"
    assert get_locatie(inventar[0]) == "locatie1"
    assert get_Id(inventar[1]) == "id2"
    assert get_nume(inventar[1]) == "nume2"
    assert get_descriere(inventar[1]) == "descriere2"
    assert get_pret(inventar[1]) == "pret2"
    assert get_locatie(inventar[1]) == "locatie2"

def test_sterge_obiect():
    inventar = adauga_obiect("id1", "nume1", "descriere1", "pret1", "locatie1", [])
    inventar = adauga_obiect("id2", "nume2", "descriere2", "pret2", "locatie2", inventar)
    assert get_by_Id("id1", inventar) == inventar[0]
    inventar = stergere_obiect("id1",inventar)

    assert get_Id(inventar[0]) == "id2"
    assert get_nume(inventar[0]) == "nume2"
    assert get_descriere(inventar[0]) == "descriere2"
    assert get_pret(inventar[0]) == "pret2"
    assert get_locatie(inventar[0]) == "locatie2"
    assert get_by_Id("id1",inventar) is None

def test_modificare_locatie():
    inventar = adauga_obiect("id1", "nume1", "descriere1", "pret1", "locatie1", [])
    inventar = adauga_obiect("id2", "nume2", "descriere2", "pret2", "locatie2", inventar)
    inventar = modificare_locatie("locatie3",inventar)
    assert get_locatie(inventar[0]) == "locatie3"

test_modificare_locatie()

