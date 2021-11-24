
import copy

from lab_567.Logic.CRUD import adauga_obiect


def undo_redo_test():
    inventar = []
    undo_list = []
    redo = []
    assert inventar == []
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id1", "nume1", "descriere1", float("1"), "locatie1", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id2", "nume2", "descriere2", float("2"), "locatie2", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id3", "nume3", "descriere3", float("3"), "locatie3", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    },
        {
            "id": "id3",
            "nume": "nume3",
            "descriere": "descriere3",
            "pret": float("3"),
            "locatie": "locatie3"
        }
    ]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == []
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == []
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id1", "nume1", "descriere1", float("1"), "locatie1", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id2", "nume2", "descriere2", float("2"), "locatie2", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id3", "nume3", "descriere3", float("3"), "locatie3", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    },
        {
            "id": "id3",
            "nume": "nume3",
            "descriere": "descriere3",
            "pret": float("3"),
            "locatie": "locatie3"
        }
    ]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    },
        {
            "id": "id3",
            "nume": "nume3",
            "descriere": "descriere3",
            "pret": float("3"),
            "locatie": "locatie3"
        }
    ]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    },
        {
            "id": "id3",
            "nume": "nume3",
            "descriere": "descriere3",
            "pret": float("3"),
            "locatie": "locatie3"
        }
    ]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id2",
        "nume": "nume2",
        "descriere": "descriere2",
        "pret": float("2"),
        "locatie": "locatie2"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    redo = []
    undo_list.append(inventar)
    fakeinventar = []
    fakeinventar = copy.deepcopy(inventar)
    inventar = adauga_obiect("id4", "nume4", "descriere4", float("4"), "locatie4", inventar)
    if inventar == fakeinventar:
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id4",
        "nume": "nume4",
        "descriere": "descriere4",
        "pret": float("4"),
        "locatie": "locatie4"
    }]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id4",
        "nume": "nume4",
        "descriere": "descriere4",
        "pret": float("4"),
        "locatie": "locatie4"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    if len(undo_list) > 0:
        redo.append(inventar)
        inventar = undo_list.pop()
    assert inventar == []
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id4",
        "nume": "nume4",
        "descriere": "descriere4",
        "pret": float("4"),
        "locatie": "locatie4"
    }]
    if len(redo) > 0:
        undo_list.append(inventar)
        inventar = redo.pop()
    assert inventar == [{
        "id": "id1",
        "nume": "nume1",
        "descriere": "descriere1",
        "pret": float("1"),
        "locatie": "locatie1"
    }, {
        "id": "id4",
        "nume": "nume4",
        "descriere": "descriere4",
        "pret": float("4"),
        "locatie": "locatie4"
    }]
