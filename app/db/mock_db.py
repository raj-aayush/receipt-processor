

db = {}


def insert(val: int) -> int:
    db[len(db)] = val
    return len(db) - 1


def exists(id: int) -> bool:
    return id >= 0 and id < len(db)


def get(id: int) -> int:
    return db[id]