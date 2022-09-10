# pylint: disable=missing-function-docstring

import mip
import pytest

from cocktail_opt.dataset import Dataset
from cocktail_opt.model import Model


@pytest.fixture(name="model")
def fixture_model(dataset: Dataset) -> Model:

    return Model(dataset, max_spend=0)


def test_model_is_created(model: Model) -> None:

    # pylint: disable=protected-access

    assert isinstance(model._model, mip.Model)


def test_making_variables_are_created(model: Model) -> None:

    # pylint: disable=protected-access

    assert isinstance(model._making, list)
    assert all(isinstance(var, mip.Var) for var in model._making)


def test_purchases_variables_are_created(model: Model) -> None:

    # pylint: disable=protected-access

    assert isinstance(model._purchases, list)
    assert all(isinstance(var, mip.Var) for var in model._purchases)


def test_model_can_be_solved(model: Model) -> None:

    model.solve()


@pytest.mark.parametrize(
    "method_name",
    [
        "feasible_cocktails",
        "ingredients_to_purchase",
    ],
)
def test_reports_require_solved_model(model: Model, method_name: str) -> None:

    with pytest.raises(Exception, match=r""):
        getattr(model, method_name)()


def test_feasible_cocktails(model: Model) -> None:

    model.solve()
    cocktails = model.feasible_cocktails()

    assert cocktails == []


def test_ingredients_to_purchase(model: Model) -> None:

    model.solve()
    ingredients = model.ingredients_to_purchase()

    assert ingredients == []
