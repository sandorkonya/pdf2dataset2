import pytest
from pdf2dataset import download


@pytest.mark.parametrize("message", ["hello", "world"])
def test_hello_world(message):
    print("hello")
