import json
from typing import Dict

import pytest

from cocktail_opt.dataset import Cocktail, Dataset, Ingredient


@pytest.fixture(name="cocktails")
def fixture_cocktails() -> Dict[str, Cocktail]:

    with open("data/cocktails.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    cocktails = {rec["cocktail_name"]: Cocktail(**rec) for rec in data}

    return cocktails


@pytest.fixture(name="ingredients")
def fixture_ingredients() -> Dict[str, Ingredient]:

    with open("data/ingredients.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    ingredients = {rec["ingredient_name"]: Ingredient(**rec) for rec in data}

    return ingredients


@pytest.fixture(name="dataset")
def fixture_dataset(
    cocktails: Dict[str, Cocktail],
    ingredients: Dict[str, Ingredient],
) -> Dataset:

    return Dataset(cocktails, ingredients)
