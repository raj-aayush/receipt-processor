# Receipt Processor

This is a basic **FastAPI-based Python application** that processes receipts using point-based rewards based on specific rules.

The API provides two endpoints:

---

## Endpoints

### `POST /receipts/process`

- Accepts a receipt object (with retailer name, items, total, timestamp, etc.).
- Calculates reward points based on defined rules.
- Returns a unique ID associated with the computed result.

### `GET /receipts/{id}/points`

- Takes a receipt ID.
- Returns the previously calculated points for that receipt.
- Returns a 400 error if the ID is invalid or unknown.

---

## To run the app

1. Make sure Docker is installed.
2. From the project root, run:

```bash
docker compose up --build
```

3. Once the container is running, access the API at:
```
http://localhost:8000
```

4. Visit the FastAPI interactive docs here:

```
http://localhost:8000/docs
```

## Project Structure:

```bash
app/
   main.py      # route definitions
   schemas/     # Pydantic models - Receipt & Item
   services/    # Business logic
   rules/       # Rules store
   db/          # In-memory mock DB interface
tests/
   integration/ # Integration tests to verify endpoint behavior
   rules/       # Unit tests
   services/    # Unit tests
```