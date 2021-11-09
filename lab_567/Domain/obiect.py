def creeaza_obiect(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce retine un obiect
    :param id: id-ul obiectului -string
    :param nume: numele obiectului-string
    :param descriere:descrierea obiectului-string
    :param pret: pretul obiectului-float
    :param locatie: locatia obiectuui-string
    :return: un dictionar ce retine un obiect din inventar
    """
    return{
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie
    }
def get_Id(obiect):
    """
    da id-ul unui obiect
    :param obiect:un dictionar de tip obiect
    :return: id-ul obiectului - string
    """
    return obiect["id"]

def get_nume(obiect):
    return obiect["nume"]

def get_descriere(obiect):
    return obiect["descriere"]

def get_pret(obiect):
    return obiect["pret"]

def get_locatie(obiect):
    return obiect["locatie"]

def to_string(obiect):
    return "id:{}, nume:{}, descriere:{}, pret:{}, locatie:{}".format(
        get_Id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )
