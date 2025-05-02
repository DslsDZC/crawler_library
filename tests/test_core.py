import pytest
from crawler.core.spider import Crawler
from crawler.config.settings import merge_config
from crawler.utils.validator import validate_proxy
from crawler.pipelines.storage import DataStorage

def test_merge_config():
    base = {"request": {"timeout": 10}}
    custom = {"request": {"timeout": 20}}
    merged = merge_config(base, custom)
    assert merged["request"]["timeout"] == 20

def test_validate_proxy():
    assert validate_proxy("http://user:pass@127.0.0.1:8080") == True
    assert validate_proxy("invalid-proxy") == False

def test_data_storage():
    data = [{"url": "http://example.com", "content": "test"}]
    storage = DataStorage()
    csv_path = storage.save_to_csv(data)
    assert Path(csv_path).exists()

# tests/test_exceptions.py
def test_invalid_proxy_connection(mocker):
    mocker.patch("requests.get", side_effect=requests.exceptions.ProxyError())
    crawler = Crawler("http://example.com", proxy="http://invalid-proxy")
    
    with pytest.raises(ProxyError):
        crawler.fetch("http://example.com")