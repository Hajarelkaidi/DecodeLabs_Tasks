import pandas as pd 
import numpy as np

# ************************************
# ******** Data Understanding ********
# ************************************

# ====== step 1: Load dataset ======
data = pd.read_excel("Dataset for Data Analytics.xlsx")

# ====== step 2: Data display ======
print(data.head())
data.info()

# ====== step 3: Missing Analysis ======
        # Number of missing values: 
missing_values = data.isnull().sum()
print("Missing values before cleaning are:\n",missing_values)
        # Percentage of missing values:
per_missing_values = data.isnull().mean() * 100
print("\nThe percentages of the missing values are:\n",per_missing_values)
        # I observe that Only "CouponCode" column contains missing values,
        # 309 missing values (25.75% of the dataset),
        # and all other columns have complete data.

# ====== step 4: Duplicate Analysis ======
        # Search duplicate rows:
print("Duplicate rows:", data.duplicated().sum())
        # Search duplicate Order IDs:
print("Duplicate Order IDs:", data["OrderID"].duplicated().sum())

# *******************************
# ******** Data Cleaning ********
# *******************************

# ====== step 5: Handling Missing Values ======
        # Fill missing CouponCode values:
data["CouponCode"] = data["CouponCode"].fillna("Not Used")
        # Missing values in the CouponCode field likely indicate that no coupon was used during the purchase.
        # We will replace these missing values with "Not Used"
        # because this way we keep the information about the CouponCode field and
        # we do not lose any rows from the dataset that contains the CouponCode field.    
         
        # Verify missing values:
print("Missing values after cleaning are:\n",data.isnull().sum())

