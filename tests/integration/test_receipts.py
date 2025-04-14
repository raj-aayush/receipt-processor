def test_post_receipt_process_returns_id(client, make_receipt):
    response = client.post("/receipts/process", json=make_receipt().model_dump())
    assert response.status_code == 200
    json = response.json()
    assert "id" in json
    assert isinstance(json["id"], str)


def test_get_points_returns_points_for_valid_id(client, make_receipt):
    # First submit a receipt to get an ID
    post_response = client.post("/receipts/process", json=make_receipt().model_dump())
    receipt_id = post_response.json()["id"]

    # Then request points for that ID
    get_response = client.get(f"/receipts/{receipt_id}/points")
    assert get_response.status_code == 200
    json = get_response.json()
    assert "points" in json
    assert isinstance(json["points"], int)
    assert json["points"] == 0


def test_get_points_returns_valid_points_for_non_zero_value(client, make_receipt):
    response = client.post("/receipts/process", json=make_receipt(**{"retailer": "Target"}).model_dump())
    assert response.status_code == 200
    json = response.json()
    assert "id" in json
    assert isinstance(json["id"], str)
    receipt_id = json["id"]
    # Then request points for that ID
    get_response = client.get(f"/receipts/{receipt_id}/points")
    assert get_response.status_code == 200
    json = get_response.json()
    assert "points" in json
    assert isinstance(json["points"], int)
    assert json["points"] == 6


def test_get_points_raises_400_for_invalid_id(client):
    response = client.get("/receipts/999999/points")
    assert response.status_code == 400
    assert response.json()["detail"] == "Receipt not found"
