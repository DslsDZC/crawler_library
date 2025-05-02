# tests/test_config.py
def test_config_merge():
    base = {"request": {"timeout": 10}}
    custom = {"request": {"timeout": 20}, "logging": {"level": "DEBUG"}}
    
    merged = merge_config(base, custom)
    assert merged["request"]["timeout"] == 20
    assert merged["logging"]["level"] == "DEBUG"
