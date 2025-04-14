import pytest
from app.schemas.receipt import Receipt, Item

@pytest.fixture
def default_receipt():
    return Receipt(
        retailer="...",
        purchaseDate="2022-02-02",
        purchaseTime="12:00",
        items=[
            Item(shortDescription="Ap", price="2.99")
        ],
        total="2.99"
    )