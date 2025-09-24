import requests
from environment import ANIMAL_API_URL, ANIMAL_API_KEY

def fetch_data(name: str, timeout: int = 10) -> list[dict]:
    headers = {"X-Api-Key": ANIMAL_API_KEY}
    params = {"name": name}

    resp = requests.get(ANIMAL_API_URL, headers=headers, params=params, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    return data