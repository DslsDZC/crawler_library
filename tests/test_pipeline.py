# tests/test_pipeline.py
def test_data_storage(tmpdir):
    data = [{"url": "http://example.com", "content": "test"}]
    storage = DataStorage()
    
    csv_path = storage.save_to_csv(data)
    assert Path(csv_path).exists()
    assert "url,content" in open(csv_path).read()
