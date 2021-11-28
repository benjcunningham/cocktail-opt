from __future__ import annotations

from typing import Generator, List, Tuple, Type, TypeVar

import numpy as np
import pandas as pd


T = TypeVar("T", bound="Table")


class Table:
    def __init__(self, data: pd.DataFrame):

        self.data = data

    @property
    def key(self) -> str:

        return self._key

    @key.setter
    def key(self, value: str) -> None:

        self._key = value
        self._keys = np.sort(self.data[value].unique())

        self._index_to_key = dict(zip(list(range(len(self._keys))), self._keys))
        self._key_to_index = {val: key for key, val in self._index_to_key.items()}

    @property
    def keys(self) -> np.ndarray:

        return self._keys

    def __len__(self) -> int:

        return len(self._index_to_key)

    def index_to_key(self, index: int) -> str:

        return self._index_to_key[index]

    def key_to_index(self, key: str) -> int:

        return self._key_to_index[key]

    @classmethod
    def from_path(cls: Type[T], path: str) -> T:

        data = pd.read_csv(path)

        return cls(data)


class Cocktails(Table):
    def __init__(self, data: pd.DataFrame):

        super().__init__(data)

        self.key = "cocktail"

    def __iter__(self) -> Generator[Tuple[str, List[str]], None, None]:

        recipes = self.data.groupby(self.key).agg({"ingredient": list}).reset_index()

        for cocktail in self.keys:

            ings = recipes["ingredient"][recipes["cocktail"] == cocktail].values[0]

            yield cocktail, ings


class Ingredients(Table):
    def __init__(self, data: pd.DataFrame):

        super().__init__(data)

        self.key = "ingredient"


class Dataset:
    def __init__(self, cocktails: Cocktails, ingredients: Ingredients):

        self.cocktails = cocktails
        self.ingredients = ingredients

    def recipes(self) -> np.ndarray:

        recipes = np.zeros((len(self.cocktails), len(self.ingredients)))

        for cocktail, ingredients in self.cocktails:

            row_index = self.cocktails.key_to_index(cocktail)

            for ingredient in ingredients:

                col_index = self.cocktails.key_to_index(ingredient)
                recipes[row_index, col_index] = 1

        return recipes

    @classmethod
    def from_paths(cls, cocktails_path: str, ingredients_path: str) -> Dataset:

        cocktails = Cocktails.from_path(cocktails_path)
        ingredients = Ingredients.from_path(ingredients_path)

        return cls(cocktails, ingredients)
