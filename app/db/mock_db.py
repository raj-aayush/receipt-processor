

db = {}


def insert(val: int) -> int:
    db[len(db)] = val
    return len(db) - 1


def exists(id: int) -> bool:
    return 0 <= id < len(db)


def get(id: int) -> int:
    if not exists(id):
        raise KeyError("Receipt with ID {id} not found")
    return db[id]