from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class Ingredient:
    r"""Ingredient dataclass.

    A representation of an ingredient, including the name of the ingredient and the
    price. While not explicitly required, the canonical way to serialize multiple
    ingredients as JSON is in the following structure:

    .. code-block:: json

        [
            {
                "ingredient_name": "Absinthe",
                "price": 50.0
            },
            {
                "ingredient_name": "Angostura Bitters",
                "price": 12.0
            },
        ]

    Args:
        ingredient_name: Name of the ingredient.
        price: Price of the ingredient.

    """

    ingredient_name: str
    price: float


@dataclass
class Cocktail:
    r"""Cocktail dataclass.

    A representation of a cocktail, including the name of the cocktail and the component
    ingredients. While not explicitly required, the canonical way to serialize multiple
    cocktails as JSON is in the following structure:

    .. code-block:: json

        [
            {
                "cocktail_name": "Alexander",
                "ingredient_names": [
                    "Cognac",
                    "Dark Creme de Cacao",
                    "Light Cream"
                ]
            },
            {
                "cocktail_name": "Americano",
                "ingredient_names": [
                    "Campari",
                    "Sweet Red Vermouth",
                    "Soda"
                ]
            }
        ]

    Args:
        cocktail_name: Name of the cocktail:
        ingredient_names: List of names of ingredients.

    """

    cocktail_name: str
    ingredient_names: List[str]


class Dataset:
    r"""Dataset converter for linear programming.

    A class for converting hash maps of :class:`cocktail_opt.dataset.Cocktail` and hash
    maps of :class:`cocktail_opt.dataset.Ingredient` into numerical matrices appropriate
    for use in a linear programming formulation.

    Args:
        cocktails: Dictionary of (cocktail name, :class:`cocktail_opt.dataset.Cocktail`)
            key-value pairs.
        ingredients: Dictionary of (ingredient name,
            :class:`cocktail_opt.dataset.Ingredient`) key-value pairs.

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
