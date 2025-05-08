import project as pr
import pytest # type: ignore

def test_replace_quotes():
    assert pr.replace_quotes("This is CS50's intro to python") == 'This is CS50"s intro to python'
    assert pr.replace_quotes("Hello world's learners") == 'Hello world"s learners'

def test_name_exist():
    with pytest.raises(ValueError):
         pr.name_exist("Omlette", "_Book1.csv")
    with pytest.raises(ValueError):
        pr.name_exist("Maggie", "_Book1.csv")
    assert pr.name_exist("Avogado", "_Book1.csv") == "Avogado"
    assert pr.name_exist("maggie", "_Book1.csv") == "maggie"

def test_get_recipe_list():
    assert pr.get_recipes_list("_Book1.csv", list=True) == ["Maggie", "Omlette"]
    assert pr.get_recipes_list("_Book1.csv") == "\nYour Book has the following recipes: \n\n- Maggie: 2\n- Omlette: 3\n\n"
