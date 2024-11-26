# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Initial Data Explorations
#
# This notebook is intended for the initial exploration of the dataset. It includes steps for data loading, and preliminary analysis to understand the structure and key characteristics of the data.

# %% [markdown]
# ## Import Modules

# %%
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from heart_failure_prediction.dataset import load_raw_data

# %% [markdown]
# ## Dataset Information

# %%
raw_data: pd.DataFrame = load_raw_data()

raw_data

# %%
raw_data.info()

# %% [markdown]
# ### Check for Duplicate Values

# %%
raw_data.duplicated().sum()

# %% [markdown]
# ### Check for Missing Values

# %%
missing_number = raw_data.isna().sum().sort_values(ascending=False)
missing_percent = (raw_data.isna().sum() / raw_data.isna().count()).sort_values(
    ascending=False
)
pd.concat(
    [missing_number, missing_percent],
    axis=1,
    keys=["No. Missing", "% Missing"],
)

# %% [markdown]
# ## Exploratory Data Analysis

# %%
describe_heart_disease = raw_data[raw_data["HeartDisease"] == 1].describe().T
describe_no_heart_disease = raw_data[raw_data["HeartDisease"] == 0].describe().T

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(5, 5))
plt.subplot(1, 2, 1)
sns.heatmap(
    describe_heart_disease[["mean"]],
    annot=True,
    linewidths=0.4,
    linecolor="black",
    cbar=False,
    fmt=".2f",
)
plt.title("Heart Disease")
plt.subplot(1, 2, 2)
sns.heatmap(
    describe_no_heart_disease[["mean"]],
    annot=True,
    linewidths=0.4,
    linecolor="black",
    cbar=False,
    fmt=".2f",
)
plt.title("No Heart Disease")
fig.tight_layout(pad=2)

# %% [markdown]
# ### Numerical Columns

# %%
numerical = raw_data.drop(["HeartDisease"], axis=1).select_dtypes("number").columns
round(raw_data[numerical].describe(), 2)

# %% [markdown]
# ### Categorical Columns

# %%
categorical = raw_data.select_dtypes("object").columns
round(
    raw_data[categorical].describe(),
    2,
)

# %%
heart_disease = raw_data["HeartDisease"]

heart_disease.plot(kind="hist")

# %%
