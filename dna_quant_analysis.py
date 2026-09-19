"""
dna_quant_analysis.py

Evaluates NanoDrop-style spectrophotometer readings for extracted bacterial
DNA samples: calculates A260/A280 purity ratio, flags PCR suitability, and
calculates the dilution needed to reach a standard PCR working concentration.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "nanodrop_readings.csv"
TARGET_CONC_NG_UL = 20.0  # standard PCR working concentration


def load_data(path: Path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["concentration_ng_ul"] = float(row["concentration_ng_ul"])
            row["a260"] = float(row["a260"])
            row["a280"] = float(row["a280"])
            rows.append(row)
    return rows


def assess_purity(ratio: float) -> str:
    if 1.75 <= ratio <= 1.90:
        return "Suitable for PCR"
    elif ratio < 1.75:
        return "Protein contamination — not recommended"
    else:
        return "Possible RNA contamination"


def dilution_instruction(conc: float, target: float = TARGET_CONC_NG_UL) -> str:
    if conc <= target:
        return "Already at or below target — use neat"
    factor = conc / target
    return f"1:{factor:.1f} in NFW"


def main():
    rows = load_data(DATA_PATH)

    header = f"{'Sample':<13}{'Conc(ng/uL)':<14}{'A260/A280':<12}{'Status':<38}{'Dilution to 20 ng/uL'}"
    print(header)
    print("-" * len(header))

    for row in rows:
        ratio = round(row["a260"] / row["a280"], 2)
        status = assess_purity(ratio)
        dilution = dilution_instruction(row["concentration_ng_ul"])
        print(f"{row['sample_id']:<13}{row['concentration_ng_ul']:<14}{ratio:<12}{status:<38}{dilution}")


if __name__ == "__main__":
    main()
