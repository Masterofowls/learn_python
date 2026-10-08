from app import banner

def test_banner_default():
    assert banner("Dan") == "Welcome, Dan!"

def test_banner_with_env(monkeypatch):
    monkeypatch.setenv("APP_BANNER", "Hello")
    assert banner("Dan") == "Hello, Dan!"