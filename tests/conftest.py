import pytest
from app.schemas.receipt import Receipt, Item

@pytest.fixture
def make_receipt():
    def _make(**overrides):
        return Receipt(
            retailer=overrides.get("retailer", "..."),
            purchaseDate=overrides.get("purchaseDate", "2022-02-02"),
            purchaseTime=overrides.get("purchaseTime", "12:00"),
            items=overrides.get("items", [Item(shortDescription="Ap", price="2.99")]),
            total=overrides.get("total", "2.99"),
        )
    return _make
