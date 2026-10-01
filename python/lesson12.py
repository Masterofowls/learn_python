# Lesson 12 - time and requests

import time

import requests


def main():
    start = time.time()
    try:
        r = requests.get("https://httpbin.org/get", timeout=3)
        r.raise_for_status()
        print(r.status_code)
        data = r.json()
        print(data['url'])
        time.sleep(1)
        elapsed = time.time() - start
        print(f"took {elapsed:.3f}s")
    except requests.RequestException as e:
        print("request failed:", e)


if __name__ == "__main__":
    main()