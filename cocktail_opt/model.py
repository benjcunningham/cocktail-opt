from __future__ import annotations

from typing import Dict, List

import mip
import numpy as np

from cocktail_opt.dataset import Dataset


class Model:
    r"""

    Args:
        dataset:
        max_spend:

    """

    def __init__(
        self,
        dataset: Dataset,
        max_spend: float = 0.0,
    ) -> None:

        self.dataset = dataset
        self.max_spend = max_spend

        self._recipes = dataset.recipes()
        self._prices = dataset.prices()

        self._model = self.create_model()
        self._making: List[mip.Var]
        self._purchases: List[mip.Var]

    def create_model(self) -> mip.Model:
        r"""

        Returns:

        """

        model = mip.Model()

        # Recipes matrix has shape (n_cocktails, n_ingredients)
        rows = range(self._recipes.shape[0])
        cols = range(self._recipes.shape[1])

        # Ingredient purchases, making cocktail are binary
        self._making = [model.add_var(var_type=mip.BINARY) for _ in rows]
        self._purchases = [model.add_var(var_type=mip.BINARY) for _ in cols]

        # Total price of all ingredients less than or equal to max spend
        total_price = mip.xsum(
            self._prices[col_idx] * self._purchases[col_idx] for col_idx in cols
        )
        model.add_constr(total_price <= self.max_spend)

        # Must have all ingredients to make cocktail
        for row_idx in rows:

            purchased_ingredients = mip.xsum(
                self._recipes[row_idx][col_idx] * self._purchases[col_idx]
                for col_idx in cols
            )

            required_ingredients = mip.xsum(
                self._recipes[row_idx][col_idx] * self._making[row_idx]
                for col_idx in cols
            )

            model.add_constr(purchased_ingredients >= required_ingredients)

        # Maximize total number of cocktails
        model.objective = mip.maximize(
            mip.xsum(self._making[row_idx] for row_idx in rows)
        )

        return model

    def solve(self) -> Model:
        r"""

        Returns:

        """

        self._model.optimize()

        return self

    def feasible_cocktails(self) -> Dict:
        r"""

        Returns:

        """

        cocktail_names = list(self.dataset.cocktails.keys())
        cocktail_idxs = np.where([var.x for var in self._making])[0]
        cocktail_keys = [cocktail_names[idx] for idx in cocktail_idxs]
        cocktails = {key: self.dataset.cocktails[key] for key in cocktail_keys}

        return cocktails

    def ingredients_to_purchase(self) -> Dict:
        r"""

        Returns:

        """

        ingredient_names = list(self.dataset.ingredients.keys())
        ingredient_idxs = np.where([var.x for var in self._purchases])[0]
        ingredient_keys = [ingredient_names[idx] for idx in ingredient_idxs]
        ingredients = {key: self.dataset.ingredients[key] for key in ingredient_keys}

        return ingredients
