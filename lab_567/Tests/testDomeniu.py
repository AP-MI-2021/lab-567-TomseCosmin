from lab_567.Domain.obiect import *

def test_obiect():
    test = creeaza_obiect("id-test", "nume-test","descriere-test", 1000, "locatie-test")
    assert get_Id(test) == "id-test"
    assert get_nume(test) == "nume-test"
    assert get_descriere(test) == "descriere-test"
    assert get_pret(test) == 1000
    assert get_locatie(test) == "locatie-test"
