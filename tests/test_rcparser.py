import pytest
import os
from ..file_sorter.modules.rcparser import rcparser

@pytest.fixture
def rc():
    rc_object=rcparser("./file_sorter/res/.organizerc")
    return rc_object

def test_check_rc_exist():
    rcparser.check_rc

def test_check_rc():
    assert rcparser.check_rc("./file_sorter/res/.organizerc") == True
    assert rcparser.check_rc("./tests/testFiles/.non_existing_file") == False

def test_init():
    rc=rcparser("./file_sorter/res/.organizerc")
    assert rc is not None


def test_get_path_to_organizerc_exist(rc):
    rc.get_path_to_organizerc()

def test_get_path_to_organizerc(rc):
    assert rc.get_path_to_organizerc() == "./file_sorter/res/.organizerc"

def test_copy_orginizerc_exist(rc):
    rc.copy_organizerc()

def test_copy_orginizerc(rc):
    rc.copy_organizerc("./tests/testFiles")
    assert rc.check_rc("./tests/testFiles")
    os.remove("./tests/testFiles/.organizerc")

def test_rc_syntax_checking_exist(rc):
    rc.rc_syntax_checking

def test_syntax_checking(rc):
    assert rc.syntax_checking()

def test_parse_paths_exist(rc):
    rc.parse_path

def test_parse_path(rc):
    assert rc.parse_path == 2

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
