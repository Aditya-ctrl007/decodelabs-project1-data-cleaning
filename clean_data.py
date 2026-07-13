"""
==========================================================
DecodeLabs Internship - Project 1: Data Cleaning & Preparation
==========================================================
Author : Singh Aditya Manoj Kumar
GitHub : https://github.com/Aditya-ctrl007
LinkedIn: https://www.linkedin.com/in/singhadityamanoj

Goal: Clean the raw e-commerce orders dataset by handling
missing values, duplicates, and inconsistent formatting -
following the 3-phase framework from the internship brief:

    Phase 1 - Strategic Imputation   (handle missing values)
    Phase 2 - The Integrity Audit    (remove duplicates)
    Phase 3 - Speak One Language     (standardize formats)

Every change made below is logged into `change_log` so it
can be turned into a Change Log PDF for stakeholders.
==========================================================
"""

import pandas as pd
from datetime import datetime

# ----------------------------------------------------------
# SETUP: track every change we make (for the Change Log PDF)
# ----------------------------------------------------------
change_log = []


def log_change(change_id, description, impact):
    change_log.append({
        "Change ID": change_id,
        "Description": description,
        "Impact": impact,
        "Status": "Resolved"
    })


# ----------------------------------------------------------
# STEP 0: LOAD THE RAW DATASET
# ----------------------------------------------------------
RAW_FILE = "Dataset_for_Data_Analytics.xlsx"
df = pd.read_excel(RAW_FILE)

print(f"Loaded raw dataset: {df.shape[0]} rows, {df.shape[1]} columns")
rows_before = df.shape[0]

# ----------------------------------------------------------
# STEP 1 (PHASE 1): HANDLE MISSING VALUES - "Strategic Imputation"
# ----------------------------------------------------------
# CouponCode is the only column with nulls. A blank CouponCode
# doesn't mean "unknown" - it means the customer used NO coupon.
# So instead of deleting these rows (which loses 25%+ of the
# data and reduces statistical power - see "Listwise Deletion"
# warning in the brief), we impute a clear categorical label.

missing_coupon_count = df["CouponCode"].isna().sum()
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

log_change(
    "CR001",
    "Imputed missing 'CouponCode' values with category 'No Coupon' "
    "(blank = customer did not use a coupon, not missing data)",
    f"Preserved {missing_coupon_count} records that would otherwise "
    f"have been deleted"
)

# ----------------------------------------------------------
# STEP 2 (PHASE 2): REMOVE DUPLICATES - "The Integrity Audit"
# ----------------------------------------------------------
# Two checks, per the brief's "One Truth, One Record" standard:
#   a) Exact duplicate rows
#   b) Duplicate OrderID (the unique identifier) - even if other
#      fields differ, an OrderID must be truly unique

exact_dupes = df.duplicated().sum()
df = df.drop_duplicates()

order_id_dupes = df.duplicated(subset=["OrderID"]).sum()
df = df.drop_duplicates(subset=["OrderID"], keep="first")

log_change(
    "CR002",
    "Removed exact duplicate rows and duplicate OrderID records",
    f"Removed {exact_dupes} exact duplicate row(s) and "
    f"{order_id_dupes} duplicate OrderID record(s)"
)

# ----------------------------------------------------------
# STEP 3 (PHASE 3): STANDARDIZE FORMATS - "Speak One Language"
# ----------------------------------------------------------

# 3a. Trim whitespace + Proper Case on text/category columns
text_cols = ["Product", "ShippingAddress", "PaymentMethod",
             "OrderStatus", "CouponCode", "ReferralSource"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# 3b. Uppercase, trimmed IDs (identifiers should not be case-sensitive)
id_cols = ["OrderID", "CustomerID", "TrackingNumber"]
for col in id_cols:
    df[col] = df[col].astype(str).str.strip().str.upper()

# 3c. Dates -> ISO 8601 (YYYY-MM-DD), the international standard
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# 3d. Numeric precision -> 2 decimal places for currency fields
df["UnitPrice"] = df["UnitPrice"].round(2)
df["TotalPrice"] = df["TotalPrice"].round(2)

log_change(
    "CR003",
    "Standardized text casing/whitespace, uppercased ID fields, "
    "converted dates to ISO 8601 (YYYY-MM-DD), rounded currency "
    "fields to 2 decimal places",
    "Ensured a single consistent format across all 1,200 records"
)

rows_after = df.shape[0]

# ----------------------------------------------------------
# STEP 4: VALIDATION GATE (must pass before Project 2 unlocks)
# ----------------------------------------------------------
# Per the brief: "You must prove there are zero duplicate IDs
# and zero incorrectly formatted dates."

duplicate_ids = df["OrderID"].duplicated().sum()
bad_dates = (~df["Date"].str.match(r"^\d{4}-\d{2}-\d{2}$")).sum()
remaining_nulls = df.isna().sum().sum()

print("\n--- VALIDATION GATE ---")
print(f"Duplicate OrderIDs remaining : {duplicate_ids}")
print(f"Incorrectly formatted dates  : {bad_dates}")
print(f"Remaining null values        : {remaining_nulls}")

assert duplicate_ids == 0, "FAILED: duplicate OrderIDs still present"
assert bad_dates == 0, "FAILED: dates not in ISO 8601 format"
assert remaining_nulls == 0, "FAILED: null values still present"
print("PASSED - 0% error rate on unique identifiers and date formats.")

# ----------------------------------------------------------
# STEP 5: SAVE THE CLEANED DATASET
# ----------------------------------------------------------
OUTPUT_FILE = "Dataset_Cleaned.xlsx"
df.to_excel(OUTPUT_FILE, index=False)
print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")
print(f"Rows before: {rows_before} | Rows after: {rows_after}")

# ----------------------------------------------------------
# STEP 6: EXPORT THE CHANGE LOG (used to build the PDF report)
# ----------------------------------------------------------
log_df = pd.DataFrame(change_log)
log_df.to_csv("change_log.csv", index=False)
print("\nChange log:")
print(log_df.to_string(index=False))
