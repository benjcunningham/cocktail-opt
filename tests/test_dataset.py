import pytest

from cocktail_opt.dataset import Dataset, Table


@pytest.mark.parametrize(
    "path",
    [
        "data/cocktails.csv",
        "data/ingredients.csv",
    ],
)
def test_load_table_from_path(path: str) -> None:

    Table.from_path(path)


def test_unique_list_of_cocktails(dataset: Dataset) -> None:

    assert len(dataset.cocktails) == 33


def test_unique_list_of_ingredients(dataset: Dataset) -> None:

    assert len(dataset.ingredients) == 46


def test_iterate_over_cocktails(dataset: Dataset) -> None:

    for cocktail, ingredients in dataset.cocktails:
        assert cocktail
        assert ingredients


def test_iterate_over_ingredients(dataset: Dataset) -> None:

    for ingredient, price in dataset.ingredients:
        assert ingredient
        assert price >= 0


def test_convert_index_to_key(dataset: Dataset) -> None:

    for index in range(len(dataset.cocktails)):
        dataset.cocktails.index_to_key(index)

    for index in range(len(dataset.ingredients)):
        dataset.ingredients.index_to_key(index)


def test_convert_key_to_index(dataset: Dataset) -> None:

    for key in dataset.cocktails.keys:
        dataset.cocktails.key_to_index(key)

    for key in dataset.ingredients.keys:
        dataset.ingredients.key_to_index(key)


def test_create_recipes_matrix(dataset: Dataset) -> None:

    recipes = dataset.recipes()

    assert recipes.shape[0] == len(dataset.cocktails)
    assert recipes.shape[1] == len(dataset.ingredients)
    assert recipes.sum() == len(dataset.cocktails.data)


@pytest.mark.parametrize(
    "ingredient,price",
    [
        ("Absinthe", 50),
        ("Bourbon", 41),
        ("Gin", 29),
    ],
)
def test_ingredients_returns_correct_price(
    dataset: Dataset, ingredient: str, price: float
) -> None:

    assert dataset.ingredients.price(ingredient) == price


def test_prices_array_matches_individual_prices(dataset: Dataset) -> None:

    prices_array = dataset.prices()

    assert prices_array.sum() == dataset.ingredients.data["price"].sum()

    for index, (ingredient, _) in enumerate(dataset.ingredients):

        price = dataset.ingredients.price(ingredient)

        assert price == prices_array[index]
