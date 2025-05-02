# tests/test_validator.py
def test_valid_urls():
    assert validate_url("https://example.com") == True
    assert validate_url("http://localhost:8080") == True
    assert validate_url("https://192.168.1.1") == True

def test_invalid_urls():
    assert validate_url("ftp://example.com") == False
    assert validate_url("example.com") == False
    assert validate_url("") == False
