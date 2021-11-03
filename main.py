from lab_567.Logic.CRUD import adauga_obiect
from lab_567.Tests.testall import run_all_tests
from lab_567.UI.console import run_menu


def main():
    run_all_tests()
    invetar = []
    invetar = adauga_obiect("1","telefon","samsung",1000,"altex",invetar)
    run_menu([])

main()