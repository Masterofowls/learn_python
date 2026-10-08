import os

def banner(name: str) -> str:
    prefix = os.getenv("APP_BANNER", "Welcome")
    return f"{prefix}, {name}!"