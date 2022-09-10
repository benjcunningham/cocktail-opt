# pylint: disable=missing-function-docstring

import itertools

from cocktail_opt.dataset import Dataset


def test_unique_list_of_cocktails(dataset: Dataset) -> None:

    assert len(dataset.cocktails) == 33


def test_unique_list_of_ingredients(dataset: Dataset) -> None:

    assert len(dataset.ingredients) == 46


def test_recipes_matrix_has_correct_shape(dataset: Dataset) -> None:

    recipes = dataset.recipes()

    assert recipes.shape[0] == len(dataset.cocktails)
    assert recipes.shape[1] == len(dataset.ingredients)


def test_recipes_matrix_has_correct_values(dataset: Dataset) -> None:

    recipes = dataset.recipes()

    all_ingredients = list(
        itertools.chain(
            *[cocktail.ingredient_names for cocktail in dataset.cocktails.values()]
        )
    )

    assert recipes.sum() == len(all_ingredients)


def test_prices_array_has_correct_shape(dataset: Dataset) -> None:

    prices = dataset.prices()

    assert len(prices) == len(dataset.ingredients)


def test_prices_array_matches_individual_prices(dataset: Dataset) -> None:

    prices = dataset.prices()
    sum_prices = sum(ingredient.price for ingredient in dataset.ingredients.values())

    assert prices.sum() == sum_prices
