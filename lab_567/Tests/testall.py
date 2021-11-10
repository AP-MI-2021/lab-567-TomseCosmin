from lab_567.Tests.testCRUD import test_adauga_obiect, test_sterge_obiect
from lab_567.Tests.testDomeniu import test_obiect
from lab_567.Tests.test_undo_redo import undo_redo_test


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    undo_redo_test()
