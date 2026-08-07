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

# Rullerende 10-dagers korrelasjon gjennom sommeren + figur
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ret_all = np.log(df[["gold", "brent"]].dropna()).diff().dropna()
roll10 = ret_all["gold"].rolling(10).corr(ret_all["brent"]).dropna().loc["2026-03-01":]
print(f"\nRullerende 10-dagers korrelasjon, siste verdi ({roll10.index[-1]:%Y-%m-%d}): {roll10.iloc[-1]:+.2f}")

C_OIL, INK, GRID, SURFACE = "#2a78d6", "#0b0b0b", "#e1e0d9", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "xtick.color": "#898781", "ytick.color": "#898781", "font.size": 10})
fig, ax = plt.subplots(figsize=(9, 4))
ax.axhline(0, color="#c3c2b7", lw=1)
ax.plot(roll10.index, roll10.values, color=C_OIL, lw=1.8)
ax.fill_between(roll10.index, 0, roll10.values, color=C_OIL, alpha=0.12, linewidth=0)
ax.set_ylim(-1, 1)
ax.set_title("Rullerende 10-dagers korrelasjon, daglige avkastninger (gull × Brent, mars–aug 2026)",
             loc="left", fontweight="bold", color=INK)
ax.annotate(f"{roll10.index[-1]:%d.%m}: {roll10.iloc[-1]:+.2f}", xy=(roll10.index[-1], roll10.iloc[-1]),
            xytext=(8, 0), textcoords="offset points", color=C_OIL, fontweight="bold", va="center")
ax.set_xlim(roll10.index[0], roll10.index[-1] + pd.Timedelta(days=18))
fig.tight_layout()
fig.savefig(HERE / "output" / "05_rullerende_korrelasjon_10d_2026.png", dpi=150)
