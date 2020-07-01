import pytest

from ..file_sorter.modules.rcparser import rcparser


def test_check_rc_exist():
    rcparser.check_rc
def test_checkrc():
    assert rcparser.check_rc("./file_sorter/res/.organizerc") == True
    assert rcparser.check_rc("./tests/testFiles/.non_existing_file") == False

def test_init():
    rc=rcparser("./file_sorter/res/.organizerc")
    assert rc is not None

@pytest.fixture
def rcparser_object():
    rc=rcparser("./file_sorter/res/.organizerc")
    return rc

def test_get_path_to_organizerc_exist(rcparser_object):
    rcparser_object.get_path_to_organizerc()

def test_get_path_to_organizerc(rcparser_object):
    assert rcparser_object.get_path_to_organizerc() == "./file_sorter/res/.organizerc"
