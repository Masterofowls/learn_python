import requests

def test_httpbin_get():
    r = requests.get("https://httpbin.org/get", timeout=5)
    assert r.status_code == 200
    data = r.json()
    assert "url" in data

def test_httpbin_post():
    r = requests.post(
        "https://httpbin.org/post",
        json={"lesson": 8},
        timeout=5,
    )
    assert r.status_code == 200
    assert r.json()["json"]["lesson"] == 8