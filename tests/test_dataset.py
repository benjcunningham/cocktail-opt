import pytest

from cocktail_opt.dataset import Table


@pytest.mark.parametrize(
    "path",
    [
        "data/cocktails.csv",
        "data/ingredients.csv",
    ],
)
def test_load_table_from_path(path):

    Table.from_path(path)


def test_unique_list_of_cocktails(dataset):

    assert len(dataset.cocktails) == 33


def test_unique_list_of_ingredients(dataset):

    assert len(dataset.ingredients) == 46


def test_iterate_over_recipes(dataset):

    for cocktail, ingredients in dataset.cocktails:
        assert cocktail
        assert ingredients


def test_convert_index_to_key(dataset):

    for index in range(len(dataset.cocktails)):
        dataset.cocktails.index_to_key(index)

    for index in range(len(dataset.ingredients)):
        dataset.ingredients.index_to_key(index)


def test_convert_key_to_index(dataset):

    for key in dataset.cocktails.keys:
        dataset.cocktails.key_to_index(key)

    for key in dataset.ingredients.keys:
        dataset.ingredients.key_to_index(key)