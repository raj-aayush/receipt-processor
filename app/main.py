from fastapi import FastAPI, HTTPException
from app.schemas.receipt import Receipt
from app.services import receipt_service
from app.db import mock_db

app = FastAPI()
"""
TODO:
- Dockerize app
- Add unit tests for all cases
"""


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    points = receipt_service.calculate_points(receipt)
    return {"id": points}


@app.get("/receipts/{id}/points")
def read_item(id: int):
    if id is None or mock_db.exists(id) is False:
        raise HTTPException(status_code=400, detail="Receipt not found")
    return {"points": mock_db.get(id)}
