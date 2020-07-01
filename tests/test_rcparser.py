import pytest


from ..file_sorter.modules.rcparser import rcparser

def test_check_rc_exist():
    rcparser.check_rc
def test_checkrc():
    assert rcparser.check_rc("./tests/testFiles/.organizerc") == True
    assert rcparser.check_rc("./tests/testFiles/.non_existing_file") == False

