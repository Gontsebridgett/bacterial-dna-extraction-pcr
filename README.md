# Bacterial DNA Isolation, Purification & Quantification for PCR

A protocol write-up for extracting and purifying genomic DNA from bacterial culture,
paired with a Python script that evaluates NanoDrop spectrophotometer readings
(concentration + A260/A280 purity ratio) to flag which samples are suitable as
PCR template DNA.

## Overview

Bacterial DNA extraction involves three core stages: (1) cell lysis to release DNA,
(2) removal of protein, RNA, and debris, and (3) precipitation and washing of the
purified DNA. Because PCR is highly sensitive to inhibitors (residual protein,
phenol, ethanol), extracted DNA must be checked for both concentration and purity
before use as template.

## Principle

- **Lysis** — cell wall/membrane broken down (lysozyme for gram-positive strains,
  SDS + Proteinase K for protein digestion)
- **Purification** — phenol-chloroform extraction (or spin-column kit) removes
  protein; RNase A removes RNA
- **Precipitation** — isopropanol precipitates DNA; ethanol wash removes salts
- **Quality control** — A260/A280 ratio and agarose gel check confirm purity
  and integrity before PCR use

## Materials & Reagents

- Overnight bacterial culture
- Lysis buffer + lysozyme (gram-positive strains)
- 10% SDS, Proteinase K, RNase A
- Phenol-chloroform-isoamyl alcohol (25:24:1) or spin-column kit
- Isopropanol, 70% ethanol
- TE buffer / nuclease-free water
- NanoDrop spectrophotometer
- Agarose gel electrophoresis setup (for integrity check)

## Method (Summary)

| Stage | Step |
|---|---|
| Lysis | Pellet cells → resuspend in lysis buffer (+ lysozyme if gram-positive) → SDS + Proteinase K, 55–60°C |
| Purification | RNase A treatment → phenol-chloroform extraction → collect aqueous phase |
| Precipitation | Isopropanol precipitation → centrifuge → 70% ethanol wash → air-dry → resuspend |
| QC | NanoDrop A260/A280 → agarose gel check for intact high-MW band |

## Result Interpretation

| A260/A280 Ratio | Interpretation |
|---|---|
| ~1.8 | High-purity DNA — suitable for PCR |
| < 1.8 | Protein/phenol contamination |
| > 2.0 | Possible RNA contamination |

A single sharp high-molecular-weight band on the agarose gel indicates intact
genomic DNA; smearing indicates degradation, which can reduce PCR efficiency.

## Analysis Script

`dna_quant_analysis.py` reads NanoDrop-style readings (A260, A280, and
concentration in ng/µL) from `sample_data/nanodrop_readings.csv`, calculates the
A260/A280 ratio for each sample, and flags whether each is suitable for PCR,
along with the dilution needed to reach a standard working concentration.

### Usage

```bash
pip install -r requirements.txt
python dna_quant_analysis.py
```

### Sample output

```
Sample       Conc(ng/uL)   A260/A280   Status              Dilution to 20 ng/uL
------------------------------------------------------------------------------
Sample_1     145.2         1.83        Suitable for PCR    1:7.3 in NFW
Sample_2     88.6          1.52        Protein contamination — not recommended
Sample_3     210.4         2.15        Possible RNA contamination
```

## Repository Structure

```
bacterial-dna-extraction-pcr/
├── README.md
├── dna_quant_analysis.py
├── requirements.txt
└── sample_data/
    └── nanodrop_readings.csv
```
