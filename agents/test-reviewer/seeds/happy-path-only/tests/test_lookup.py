import json, tempfile
from lookup import load_user

def test_finds_user():
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([{"id": "u1", "name": "A"}, {"id": "u2", "name": "B"}], f)
    assert load_user(f.name, "u2")["name"] == "B"
