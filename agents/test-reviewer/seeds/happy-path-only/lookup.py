import json

def load_user(path: str, user_id: str) -> dict:
    with open(path) as f:
        users = json.load(f)
    for u in users:
        if u["id"] == user_id:
            return u
    raise KeyError(f"no user {user_id}")
