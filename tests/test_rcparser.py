import pytest
import os
from ..file_sorter.modules.rcparser import rcparser

@pytest.fixture
def rc():
    rc_object=rcparser("./tests/testFiles/folderWithGoodOrganizerc/.organizerc")
    return rc_object

@pytest.fixture
def rc_wrong():
    rc_object=rcparser("./tests/testFiles/folderWithWrongOrganizerc/.organizerc")
    return rc_object

@pytest.fixture
def rc_without():
    rc_object=rcparser("./tests/testFiles/folderWithoutOrganizerc/.organizerc")
    return rc_object


def test_check_rc_exist(rc):
    rc.check_rc

def test_check_rc(rc, rc_without):
    assert rc.check_rc() == True
    assert rc_without.check_rc() == False

def test_init():
    rc=rcparser("./file_sorter/res/.organizerc")
    assert rc is not None


def test_get_path_to_organizerc_exist(rc):
    rc.get_path_to_organizerc()

def test_get_path_to_organizerc(rc):
    assert rc.get_path_to_organizerc() == "./tests/testFiles/folderWithGoodOrganizerc/.organizerc"

def test_copy_orginizerc_exist(rc):
    rc.copy_organizerc

##########

def test_copy_orginizerc(rc):
    rc.copy_organizerc("./tests/testFiles")
    assert rc.check_rc()
    os.remove("./tests/testFiles/.organizerc")

def test_rc_syntax_checking_exist(rc):
    rc.syntax_checking

def test_syntax_checking(rc,rc_wrong):
    #pytest.set_trace()
    assert rc.syntax_checking()

def test_parse_organizerc_by_lines_exist(rc):
    rc.parse_organizerc_by_lines

def test_parse_organizerc_by_lines(rc):
    some_array=["[paths]","somefield","alsofield","[works]","someworkfield"]
    assert rc.parse_organizerc_by_lines("[paths]",some_array) == ["somefield","alsofield"]
    assert rc.parse_organizerc_by_lines("[works]",some_array) == ["someworkfield"]

def test_parse_paths_exist(rc):
    rc.parse_paths()

def test_parse_path(rc):
    #pytest.set_trace()
    assert rc.parse_paths() == 2

def test_parse_patterns_exist(rc):
    rc.parse_patterns

def test_parse_patterns(rc):
    assert rc.parse_patterns() == 2

def test_parse_todo_exist(rc):
    rc.parse_todo

def test_parse_todo(rc):
    assert rc.parse_todo() == 2

def test_parse_works_exist(rc):
    rc.parse_works
def test_parse_works(rc):
    assert rc.parse_works() == 2

def test_get_paths_count_exist(rc):
    rc.get_paths_count()

def test_get_paths_count(rc):
    assert rc.get_paths_count() == 2

def test_get_patterns_count_exist(rc):
    rc.get_patterns_count()

def test_get_patterns_count(rc):
    assert rc.get_patterns_count() == 2

def test_get_todos_count_exist(rc):
    rc.get_todos_count()

def test_get_todos_count(rc):
    assert rc.get_todos_count() == 2

def test_get_works_count_exist(rc):
    rc.get_works_count()

def test_get_works_count(rc):
    assert rc.get_works_count() == 2

def test_get_path_by_number_exist(rc):
    rc.get_path_by_number()

# def test_get_path_by_number(rc):
    # assert rc.get_path_by_number #####
    #
    #
    #


