from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class Ingredient:

    ingredient_name: str
    price: float


@dataclass
class Cocktail:

    cocktail_name: str
    ingredient_names: List[str]


class Dataset:
    r"""

    Cocktails...

    .. code-block:: json

        {
            "Americano": [
                "Campari",
                "Sweet Red Vermouth",
                "Soda"
            ],
            "Bellini": [
                "Prosecco",
                "White Peach Puree"
            ]
        }

    Ingredients...

    .. code-block:: json

        {
            "Campari": 0,
            "Soda": 0,
            "Sweet Red Vermouth": 0,
            "Prosecco": 0,
            "White Peach Puree": 0
        }

    """

    def __init__(
        self,
        cocktails: Dict[str, Cocktail],
        ingredients: Dict[str, Ingredient],
    ) -> None:

        self.cocktails = cocktails
        self.ingredients = ingredients

    def recipes(self) -> np.ndarray:
        r"""Create a logical matrix for recipes.

        Creates an :math:`N \times P` logical matrix, where :math:`N` is the number of
        cocktails and :math:`P` is the number of ingredients, representing the
        ingredients required for each cocktail.

        Since the class assumes both ``cocktails`` and ``ingredients`` are ordered
        dictionaries (i.e., regular dictionaries in Python >=3.7), the indexes along
        each axis correspond to the keys at those indices in the respective dictionary.

        Returns:
            The logical matrix.

        """

        n_cocktails = len(self.cocktails)
        n_ingredients = len(self.ingredients)

        recipes = np.zeros((n_cocktails, n_ingredients))

        for cocktail in self.cocktails.values():

            row_index = list(self.cocktails.keys()).index(cocktail.cocktail_name)

            for ingredient_name in cocktail.ingredient_names:

                col_index = list(self.ingredients.keys()).index(ingredient_name)
                recipes[row_index, col_index] = 1

        return recipes

    def prices(self) -> np.ndarray:
        r"""Create an array of ingredient prices.

        Creates a :math:`P`-length array corresponding to the cost of each respective
        index in the ingredient dictionary.

        Returns:
            The price array.

        """

        ingredient_prices = [
            ingredient.price for ingredient in self.ingredients.values()
        ]

        return np.array(ingredient_prices, dtype=np.float_)
