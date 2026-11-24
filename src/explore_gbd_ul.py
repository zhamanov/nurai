"""Первичный осмотр набора gbd_ul (ГБД «Юридические лица») на data.egov.kz.

Печатает структуру полей и 3 пробные записи. Ключ берётся из .env (EGOV_API_KEY).
"""
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ["EGOV_API_KEY"]
BASE = "https://data.egov.kz/api/v4"

m = requests.get(f"{BASE}/mapping/gbd_ul", params={"apiKey": KEY}, timeout=30)
print("mapping:", m.status_code)
print(json.dumps(m.json(), ensure_ascii=False, indent=2)[:3000])

r = requests.get(
    f"{BASE}/gbd_ul/v1",
    params={"source": json.dumps({"size": 3}), "apiKey": KEY},
    timeout=30,
)
print("data:", r.status_code)
print(json.dumps(r.json(), ensure_ascii=False, indent=2)[:3000])
