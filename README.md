# Data Cleaning & Preparation — DecodeLabs Internship Project 1

**Author:** Singh Aditya Manoj Kumar
**LinkedIn:** [linkedin.com/in/singhadityamanoj](https://www.linkedin.com/in/singhadityamanoj)
**GitHub:** [github.com/Aditya-ctrl007](https://github.com/Aditya-ctrl007)

## Overview

This project is the foundation milestone of the DecodeLabs Data Analytics
internship track: **Data Cleaning & Preparation**. The goal is not to build
charts or models, but to prove data integrity — taking a raw, messy
e-commerce orders dataset and transforming it into a reliable, analysis-ready
source of truth.

## Problem Statement

Clean a raw dataset of 1,200 e-commerce orders by:
- Identifying and handling missing values
- Removing duplicate records
- Correcting inconsistent data formats (dates, text casing, numeric precision)

## Approach

The cleaning pipeline follows a 3-phase framework:

| Phase | Name | What it does |
|-------|------|---------------|
| 1 | Strategic Imputation | Handles missing `CouponCode` values by labeling them `"No Coupon"` instead of deleting the row (deleting would have discarded 309 valid records and reduced statistical power) |
| 2 | Integrity Audit | Checks and removes exact duplicate rows and duplicate `OrderID` values, ensuring every unique identifier is truly unique |
| 3 | Format Standardization | Trims whitespace, applies consistent casing, converts dates to ISO 8601 (`YYYY-MM-DD`), and rounds currency fields to 2 decimal places |

Every change is logged and validated against a verification gate requiring
**0% error rate** on duplicate IDs and date formats before the data is
considered production-ready.

## Repository Structure

```
├── Dataset_for_Data_Analytics.xlsx   # Raw input dataset
├── clean_data.py                     # Main cleaning pipeline (Python + pandas)
├── generate_change_log_pdf.py        # Builds the Change Log PDF report
├── change_log.csv                    # Raw log of every change made
├── Change_Log.pdf                    # Stakeholder-facing change log report
├── Dataset_Cleaned.xlsx              # Final cleaned, validated dataset
└── README.md                         # This file
```

## How to Run

```bash
pip install pandas openpyxl reportlab
python clean_data.py                 # cleans the data, writes Dataset_Cleaned.xlsx
python generate_change_log_pdf.py    # builds Change_Log.pdf from the log
```

## Results

| Metric | Before | After |
|--------|--------|-------|
| Total records | 1,200 | 1,200 |
| Missing values | 309 (`CouponCode`) | 0 |
| Duplicate OrderIDs | 0 | 0 |
| Inconsistent date formats | Mixed | 100% ISO 8601 |
| Currency precision | Variable | 2 decimal places |

## Key Takeaway

Real-world data analysis is roughly 80% cleaning and preparation, and only
20% analysis and modeling. This project demonstrates the discipline of
building that reliable 80% — the foundation every dashboard, model, and
business decision depends on.

---
*Part of the DecodeLabs Data Analytics Internship, 2026 Batch.*
