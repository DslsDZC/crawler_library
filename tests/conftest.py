# tests/test_exceptions.py
def test_invalid_proxy_connection(mocker):
    mocker.patch("requests.get", side_effect=requests.exceptions.ProxyError())
    crawler = Crawler("http://example.com", proxy="http://invalid-proxy")
    
    with pytest.raises(ProxyError):
        crawler.fetch("http://example.com")

