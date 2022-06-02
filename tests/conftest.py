import pytest

from cocktail_opt.dataset import Dataset


@pytest.fixture
def dataset() -> Dataset:

    return Dataset.from_paths("data/cocktails.csv", "data/ingredients.csv")
