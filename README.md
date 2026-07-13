# 🧹 Data Cleaning & Preparation
### DecodeLabs Data Analytics Internship — Project 1

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-data%20cleaning-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/status-complete-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

| | |
|---|---|
| **Author** | Singh Aditya Manoj Kumar |
| **LinkedIn** | [linkedin.com/in/singhadityamanoj](https://www.linkedin.com/in/singhadityamanoj) |
| **GitHub** | [github.com/Aditya-ctrl007](https://github.com/Aditya-ctrl007) |
| **Program** | DecodeLabs Data Analytics Internship, 2026 Batch |

---

## 📖 Overview

This project is the foundation milestone of the DecodeLabs Data Analytics
internship track: **Data Cleaning & Preparation**. The goal is not to build
charts or models, but to prove data integrity — taking a raw, messy
e-commerce orders dataset and transforming it into a reliable, analysis-ready
source of truth.

## 🎯 Problem Statement

Clean a raw dataset of **1,200 e-commerce orders** by:
- Identifying and handling missing values
- Removing duplicate records
- Correcting inconsistent data formats (dates, text casing, numeric precision)

This isn't about building charts or dashboards — it's the foundation phase.
Before any predictive model or business insight can be trusted, the data
underneath it has to be verifiably clean.

## 🛠️ Approach

The cleaning pipeline follows a structured 3-phase framework:

| Phase | Name | What it does |
|:---:|---|---|
| **1** | 🧩 Strategic Imputation | Handles missing `CouponCode` values by labeling them `"No Coupon"` instead of deleting the row — deleting would have discarded 309 valid records and reduced statistical power |
| **2** | 🔍 Integrity Audit | Checks and removes exact duplicate rows and duplicate `OrderID` values, ensuring every unique identifier is truly unique |
| **3** | 🗣️ Format Standardization | Trims whitespace, applies consistent casing, converts dates to ISO 8601 (`YYYY-MM-DD`), and rounds currency fields to 2 decimal places |

Every change made is logged and validated against a **verification gate**
requiring a **0% error rate** on duplicate IDs and date formats before the
data is considered production-ready.

## 📁 Repository Structure

```
├── Dataset_for_Data_Analytics.xlsx   # Raw input dataset
├── clean_data.py                     # Main cleaning pipeline (Python + pandas)
├── generate_change_log_pdf.py        # Builds the Change Log PDF report
├── change_log.csv                    # Raw log of every change made
├── Change_Log.pdf                    # Stakeholder-facing change log report
├── Dataset_Cleaned.xlsx              # Final cleaned, validated dataset
└── README.md                         # This file
```

## ▶️ How to Run

```bash
# 1. Install dependencies
pip install pandas openpyxl reportlab

# 2. Run the cleaning pipeline (produces Dataset_Cleaned.xlsx + change_log.csv)
python clean_data.py

# 3. Generate the stakeholder-facing Change Log PDF
python generate_change_log_pdf.py
```

## 📊 Results

| Metric | Before | After |
|---|:---:|:---:|
| Total records | 1,200 | 1,200 |
| Missing values | 309 (`CouponCode`) | **0** |
| Duplicate OrderIDs | 0 | **0** |
| Inconsistent date formats | Mixed | **100% ISO 8601** |
| Currency precision | Variable | **2 decimal places** |

✅ **Verification gate: PASSED** — 0% error rate on unique identifiers and date formats.

## 💡 Key Takeaway

Real-world data analysis is roughly **80% cleaning and preparation**, and
only 20% analysis and modeling. This project demonstrates the discipline of
building that reliable 80% — the foundation every dashboard, model, and
business decision depends on.

## 🔗 Connect

Feel free to check out the rest of my work or connect with me:

- 💼 [LinkedIn — Singh Aditya Manoj Kumar](https://www.linkedin.com/in/singhadityamanoj)
- 💻 [GitHub — Aditya-ctrl007](https://github.com/Aditya-ctrl007)

---
*Part of the DecodeLabs Data Analytics Internship, 2026 Batch.*
