"""Korrelasjonsanalyse: gullpris vs. oljepris.

Datakilder (lastet ned 2026-08-07):
  - Brent/WTI daglig:   datasets/oil-prices (EIA via datahub.io), t.o.m. 2026-08-03
  - Gull daglig (proxy): PAXG (Paxos Gold, 1 token = 1 troy oz) fra coinmetrics/data,
                         t.o.m. 2026-05-23. Valideres mot gullfutures (GC=F).
  - Gullfutures daglig:  FeziweMelvin/XAUUSD-Gold-Price, t.o.m. 2025-06-06 (kun validering)
  - Gull månedlig:       datasets/gold-prices (World Bank Pink Sheet), t.o.m. 2026-07

Kjør:  python3 gold_oil_correlation.py
Output: output/*.png + output/resultater.md
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)

# Palett (validert med dataviz-validatoren, lys modus)
C_OIL = "#2a78d6"     # blå
C_GOLD = "#c98500"    # mørk gull/gul
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
SURFACE = "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "axes.edgecolor": "#c3c2b7",
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": "sans-serif",
    "text.color": INK,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "font.size": 10,
})


def load() -> dict[str, pd.Series]:
    brent = pd.read_csv(DATA / "brent-daily.csv", parse_dates=["Date"], index_col="Date")["Price"]
    wti = pd.read_csv(DATA / "wti-daily.csv", parse_dates=["Date"], index_col="Date")["Price"]
    paxg = pd.read_csv(DATA / "paxg-daily.csv", parse_dates=["Date"], index_col="Date")["PriceUSD"]
    xau = pd.read_csv(DATA / "xau-futures-daily.csv", parse_dates=["Date"], index_col="Date")["Close"]
    gold_m = pd.read_csv(DATA / "gold-monthly.csv")
    gold_m["Date"] = pd.PeriodIndex(gold_m["Date"], freq="M").to_timestamp("M")
    gold_m = gold_m.set_index("Date")["Price"]
    return {"brent": brent, "wti": wti, "paxg": paxg, "xau": xau, "gold_m": gold_m}


def validate_paxg_proxy(paxg: pd.Series, xau: pd.Series) -> dict:
    """Hvor godt følger PAXG gullprisen? Sammenlign mot GC=F i overlappende periode."""
    df = pd.concat({"paxg": paxg, "xau": xau}, axis=1, sort=True).dropna()
    diff_pct = (df["paxg"] / df["xau"] - 1) * 100
    ret = np.log(df).diff().dropna()
    r, _ = stats.pearsonr(ret["paxg"], ret["xau"])
    return {
        "n": len(df),
        "period": f"{df.index[0]:%Y-%m-%d} – {df.index[-1]:%Y-%m-%d}",
        "median_abs_diff_pct": float(diff_pct.abs().median()),
        "p95_abs_diff_pct": float(diff_pct.abs().quantile(0.95)),
        "return_corr": float(r),
    }


def window_corr(gold: pd.Series, oil: pd.Series, months: int, end=None, freq: str | None = None) -> dict:
    """Pearson/Spearman-korrelasjon av logavkastninger i et vindu (daglig, evt. ukentlig)."""
    df = pd.concat({"gold": gold, "oil": oil}, axis=1, sort=True).dropna()
    end = end or df.index[-1]
    start = end - pd.DateOffset(months=months)
    df = df.loc[start - pd.Timedelta(days=14):end]
    if freq:
        df = df.resample(freq).last().dropna()
    ret = np.log(df).diff().dropna().loc[start:end]
    if len(ret) < 20:
        return {}
    pr, pp = stats.pearsonr(ret["gold"], ret["oil"])
    sr, sp = stats.spearmanr(ret["gold"], ret["oil"])
    level = df.loc[start:end]
    lr, _ = stats.pearsonr(level["gold"], level["oil"])
    return {"months": months, "n": len(ret), "start": ret.index[0], "end": ret.index[-1],
            "pearson": pr, "p_pearson": pp, "spearman": sr, "level_corr": lr}


def main() -> None:
    s = load()
    proxy = validate_paxg_proxy(s["paxg"], s["xau"])

    daily = pd.concat({"gold": s["paxg"], "oil": s["brent"]}, axis=1, sort=True).dropna()
    ret = np.log(daily).diff().dropna()
    end = daily.index[-1]

    windows = [window_corr(s["paxg"], s["brent"], m) for m in (3, 6, 12, 24)]
    windows_wti = [window_corr(s["paxg"], s["wti"], m) for m in (3, 6, 12, 24)]
    windows_weekly = [window_corr(s["paxg"], s["brent"], m, freq="W-FRI") for m in (6, 12, 24)]

    # Månedlig (helt oppdatert t.o.m. juli 2026)
    brent_m = s["brent"].resample("ME").mean()
    gold_m = s["gold_m"]
    m = pd.concat({"gold": gold_m, "oil": brent_m}, axis=1, sort=True).dropna()
    mret = np.log(m).diff().dropna()
    monthly = {}
    for yrs in (1, 3, 5):
        w = mret.loc[mret.index[-1] - pd.DateOffset(years=yrs):]
        r, p = stats.pearsonr(w["gold"], w["oil"])
        monthly[yrs] = {"n": len(w), "r": r, "p": p, "start": w.index[0], "end": w.index[-1]}

    # ---- Figur 1: indeksert prisutvikling siste 2 år av overlappet ----
    start2y = end - pd.DateOffset(years=2)
    idx = daily.loc[start2y:]
    idx = idx / idx.iloc[0] * 100
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(idx.index, idx["gold"], color=C_GOLD, lw=2)
    ax.plot(idx.index, idx["oil"], color=C_OIL, lw=2)
    ax.annotate(f"Gull (PAXG)  {idx['gold'].iloc[-1]:.0f}", xy=(idx.index[-1], idx["gold"].iloc[-1]),
                xytext=(8, 0), textcoords="offset points", color=C_GOLD, fontweight="bold", va="center")
    ax.annotate(f"Brent  {idx['oil'].iloc[-1]:.0f}", xy=(idx.index[-1], idx["oil"].iloc[-1]),
                xytext=(8, 0), textcoords="offset points", color=C_OIL, fontweight="bold", va="center")
    ax.set_title("Gull vs. Brent, indeksert (100 = %s)" % idx.index[0].strftime("%d.%m.%Y"),
                 loc="left", fontweight="bold", color=INK)
    ax.set_xlim(idx.index[0], idx.index[-1] + pd.Timedelta(days=110))
    fig.tight_layout()
    fig.savefig(OUT / "01_indeksert_prisutvikling.png", dpi=150)

    # ---- Figur 2: rullerende 60-dagers korrelasjon (daglige avkastninger) ----
    roll = ret["gold"].rolling(60).corr(ret["oil"]).dropna()
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.axhline(0, color="#c3c2b7", lw=1)
    ax.plot(roll.index, roll.values, color=C_OIL, lw=1.6)
    ax.fill_between(roll.index, 0, roll.values, color=C_OIL, alpha=0.12, linewidth=0)
    ax.set_ylim(-1, 1)
    ax.set_title("Rullerende 60-dagers korrelasjon, daglige logavkastninger (gull × Brent)",
                 loc="left", fontweight="bold", color=INK)
    ax.annotate(f"siste: {roll.iloc[-1]:+.2f}", xy=(roll.index[-1], roll.iloc[-1]),
                xytext=(8, 0), textcoords="offset points", color=C_OIL, fontweight="bold", va="center")
    ax.set_xlim(roll.index[0], roll.index[-1] + pd.Timedelta(days=140))
    fig.tight_layout()
    fig.savefig(OUT / "02_rullerende_korrelasjon_60d.png", dpi=150)

    # ---- Figur 3: scatter av daglige avkastninger, siste 12 mnd ----
    r12 = ret.loc[end - pd.DateOffset(months=12):] * 100
    pr, _ = stats.pearsonr(r12["gold"], r12["oil"])
    slope, intercept = np.polyfit(r12["oil"], r12["gold"], 1)
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.axhline(0, color=GRID, lw=1)
    ax.axvline(0, color=GRID, lw=1)
    ax.scatter(r12["oil"], r12["gold"], s=22, color=C_OIL, alpha=0.55, edgecolors=SURFACE, linewidths=0.8)
    xs = np.linspace(r12["oil"].min(), r12["oil"].max(), 50)
    ax.plot(xs, slope * xs + intercept, color=C_GOLD, lw=2)
    ax.set_xlabel("Brent, daglig avkastning (%)")
    ax.set_ylabel("Gull, daglig avkastning (%)")
    ax.set_title(f"Daglige avkastninger siste 12 mnd (t.o.m. {end:%d.%m.%Y})\nPearson r = {pr:+.3f}, beta = {slope:+.3f}",
                 loc="left", fontweight="bold", color=INK)
    fig.tight_layout()
    fig.savefig(OUT / "03_scatter_avkastninger_12m.png", dpi=150)

    # ---- Figur 4: rullerende 24-mnd korrelasjon, månedlige avkastninger (lang historikk) ----
    mroll = mret["gold"].rolling(24).corr(mret["oil"]).dropna().loc["2000":]
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.axhline(0, color="#c3c2b7", lw=1)
    ax.plot(mroll.index, mroll.values, color=C_GOLD, lw=1.6)
    ax.set_ylim(-1, 1)
    ax.set_title("Rullerende 24-måneders korrelasjon, månedlige avkastninger (gull × Brent, 2000–)",
                 loc="left", fontweight="bold", color=INK)
    ax.annotate(f"juli 2026: {mroll.iloc[-1]:+.2f}", xy=(mroll.index[-1], mroll.iloc[-1]),
                xytext=(8, 0), textcoords="offset points", color=C_GOLD, fontweight="bold", va="center")
    ax.set_xlim(mroll.index[0], mroll.index[-1] + pd.Timedelta(days=900))
    fig.tight_layout()
    fig.savefig(OUT / "04_rullerende_korrelasjon_24m_lang.png", dpi=150)

    # ---- Resultatfil ----
    lines = []
    lines.append("# Resultater: korrelasjon gull × olje\n")
    lines.append(f"Generert {pd.Timestamp('2026-08-07')}. Daglig analyse t.o.m. {end:%Y-%m-%d} "
                 f"(siste dato med både gull- og oljedata), månedlig analyse t.o.m. {m.index[-1]:%Y-%m}.\n")
    lines.append("## Proxy-validering (PAXG vs. gullfutures GC=F)\n")
    lines.append(f"- Overlapp: {proxy['period']} ({proxy['n']} dager)")
    lines.append(f"- Median absolutt prisavvik: {proxy['median_abs_diff_pct']:.2f} % (95-persentil {proxy['p95_abs_diff_pct']:.2f} %)")
    lines.append(f"- Korrelasjon daglige avkastninger: {proxy['return_corr']:.3f}\n")
    lines.append("## Daglige logavkastninger, gull × Brent\n")
    lines.append("| Vindu | Periode | N | Pearson r | p-verdi | Spearman | Nivåkorr. |")
    lines.append("|---|---|---|---|---|---|---|")
    for w in windows:
        lines.append(f"| {w['months']} mnd | {w['start']:%Y-%m-%d} – {w['end']:%Y-%m-%d} | {w['n']} "
                     f"| {w['pearson']:+.3f} | {w['p_pearson']:.3f} | {w['spearman']:+.3f} | {w['level_corr']:+.2f} |")
    lines.append("\n## Daglige logavkastninger, gull × WTI\n")
    lines.append("| Vindu | Periode | N | Pearson r | p-verdi | Spearman | Nivåkorr. |")
    lines.append("|---|---|---|---|---|---|---|")
    for w in windows_wti:
        lines.append(f"| {w['months']} mnd | {w['start']:%Y-%m-%d} – {w['end']:%Y-%m-%d} | {w['n']} "
                     f"| {w['pearson']:+.3f} | {w['p_pearson']:.3f} | {w['spearman']:+.3f} | {w['level_corr']:+.2f} |")
    lines.append("\n## Ukentlige logavkastninger, gull × Brent (fredag-til-fredag)\n")
    lines.append("| Vindu | Periode | N | Pearson r | p-verdi | Spearman | Nivåkorr. |")
    lines.append("|---|---|---|---|---|---|---|")
    for w in windows_weekly:
        lines.append(f"| {w['months']} mnd | {w['start']:%Y-%m-%d} – {w['end']:%Y-%m-%d} | {w['n']} "
                     f"| {w['pearson']:+.3f} | {w['p_pearson']:.3f} | {w['spearman']:+.3f} | {w['level_corr']:+.2f} |")
    lines.append("\n## Månedlige avkastninger, gull (World Bank) × Brent — oppdatert t.o.m. juli 2026\n")
    lines.append("| Vindu | Periode | N | Pearson r | p-verdi |")
    lines.append("|---|---|---|---|---|")
    for yrs, v in monthly.items():
        lines.append(f"| {yrs} år | {v['start']:%Y-%m} – {v['end']:%Y-%m} | {v['n']} | {v['r']:+.3f} | {v['p']:.3f} |")
    lines.append(f"\nRullerende 60-dagers korrelasjon (daglig), siste verdi: {roll.iloc[-1]:+.3f} "
                 f"(snitt siste 12 mnd: {roll.loc[end - pd.DateOffset(months=12):].mean():+.3f}, "
                 f"min/max siste 12 mnd: {roll.loc[end - pd.DateOffset(months=12):].min():+.2f} / "
                 f"{roll.loc[end - pd.DateOffset(months=12):].max():+.2f})")
    lines.append(f"\nRullerende 24-mnd månedlig korrelasjon, juli 2026: {mroll.iloc[-1]:+.3f}")
    (OUT / "resultater.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
