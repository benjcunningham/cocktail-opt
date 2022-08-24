# pylint: disable=missing-function-docstring

import itertools

from cocktail_opt.dataset import Dataset


def test_unique_list_of_cocktails(dataset: Dataset) -> None:

    assert len(dataset.cocktails) == 33


def test_unique_list_of_ingredients(dataset: Dataset) -> None:

    assert len(dataset.ingredients) == 46


def test_create_recipes_matrix(dataset: Dataset) -> None:

    recipes = dataset.recipes()

    assert recipes.shape[0] == len(dataset.cocktails)
    assert recipes.shape[1] == len(dataset.ingredients)

    all_ingredients = list(
        itertools.chain(
            *[cocktail.ingredient_names for cocktail in dataset.cocktails.values()]
        )
    )

    assert recipes.sum() == len(all_ingredients)


def test_prices_array_matches_individual_prices(dataset: Dataset) -> None:

    prices = dataset.prices()
    sum_prices = sum(ingredient.price for ingredient in dataset.ingredients.values())

    assert len(prices) == len(dataset.ingredients)
    assert prices.sum() == sum_prices
