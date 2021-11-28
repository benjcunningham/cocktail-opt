import pytest

from cocktail_opt.dataset import Dataset


@pytest.fixture
def dataset():

    return Dataset.from_paths("data/cocktails.csv", "data/ingredients.csv")
