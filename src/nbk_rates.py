"""Загрузчик официальных курсов валют Нацбанка РК."""
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

import pandas as pd
import requests

URL = "https://nationalbank.kz/rss/get_rates.cfm"


def get_rates(day: date) -> pd.DataFrame:
    fdate = day.strftime("%d.%m.%Y")
    r = requests.get(URL, params={"fdate": fdate}, timeout=30)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    rows = []
    for item in root.findall("item"):
        quant = float(item.findtext("quant") or 1)
        rows.append({
            "date": day.isoformat(),
            "code": item.findtext("title"),
            "name": item.findtext("fullname"),
            "rate_kzt": float(item.findtext("description")) / quant,
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    day = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    df = get_rates(day)
    out = Path("data/raw") / f"rates_{day.isoformat()}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(df[df["code"].isin(["USD", "EUR", "RUB", "CNY"])])
    print(f"Сохранено: {out}")
