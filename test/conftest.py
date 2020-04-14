from src.helpers import load_map_40
import pytest


@pytest.fixture
def map_40():
    """Returns a map with 40 nodes initialized"""
    return load_map_40()
