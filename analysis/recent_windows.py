"""Korrelasjon gull × olje i korte, ferske vinduer (siste måned / 3-2-1 uker).

Gullproxy for juni–august 2026: GoldBackTrack (zolodio/GoldBackTrack) — implisitt
gullpris fra Goldback-vekslingskursen (1 Goldback = 1/1000 oz). Serien har en
detaljistpremie på ~2,0x som er stabil (1,92–2,09 i 2026) og faller bort i
avkastninger. Validert mot PAXG jan–mai 2026: ukentlig avkastningskorrelasjon
0,98, daglig 0,58 (kursen settes av forhandlere og lagger intradag).

Kjør:  python3 recent_windows.py <sti til rates.json>
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

HERE = Path(__file__).parent
DATA = HERE / "data"

gb_src = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA / "goldback-rates.json"
gb = pd.DataFrame(json.load(open(gb_src)))
gb["Date"] = pd.to_datetime(gb["date"])
gold = gb.set_index("Date")["implied_spot_usd"].astype(float)
gold = gold[~gold.index.duplicated()].sort_index().loc["2026-01-14":]

brent = pd.read_csv(DATA / "brent-daily.csv", parse_dates=["Date"], index_col="Date")["Price"]
wti = pd.read_csv(DATA / "wti-daily.csv", parse_dates=["Date"], index_col="Date")["Price"]

df = pd.concat({"gold": gold, "brent": brent, "wti": wti}, axis=1, sort=True)
end = df.dropna(subset=["gold", "brent"]).index[-1]
print(f"Felles sluttdato: {end:%Y-%m-%d}\n")

windows = [("1 måned", pd.DateOffset(months=1)), ("3 uker", pd.DateOffset(weeks=3)),
           ("2 uker", pd.DateOffset(weeks=2)), ("1 uke", pd.DateOffset(weeks=1))]

rows = []
for name, off in windows:
    start = end - off
    w = df.loc[start:end].dropna(subset=["gold", "brent"])
    ret = np.log(w[["gold", "brent"]]).diff().dropna()
    chg_g = (w["gold"].iloc[-1] / w["gold"].iloc[0] - 1) * 100
    chg_b = (w["brent"].iloc[-1] / w["brent"].iloc[0] - 1) * 100
    if len(ret) >= 4:
        r, p = stats.pearsonr(ret["gold"], ret["brent"])
        rs, _ = stats.spearmanr(ret["gold"], ret["brent"])
        rows.append((name, f"{start:%d.%m}–{end:%d.%m}", len(ret), f"{r:+.2f}", f"{p:.2f}",
                     f"{rs:+.2f}", f"{chg_g:+.1f} %", f"{chg_b:+.1f} %"))
    else:
        rows.append((name, f"{start:%d.%m}–{end:%d.%m}", len(ret), "–", "–", "–",
                     f"{chg_g:+.1f} %", f"{chg_b:+.1f} %"))

print("| Vindu | Periode | N (avk.) | Pearson r | p | Spearman | Gull endring | Brent endring |")
print("|---|---|---|---|---|---|---|---|")
for row in rows:
    print("| " + " | ".join(str(x) for x in row) + " |")

# Gullnivå (implisitt, premie-justert med medianpremie mot PAXG jan-mai 2026)
PREMIUM = 2.00
print(f"\nImplisitt gullspot siste dato ({end:%Y-%m-%d}): "
      f"~{gold.loc[:end].iloc[-1] / PREMIUM:,.0f} USD/oz (Goldback/{PREMIUM:.2f})")
