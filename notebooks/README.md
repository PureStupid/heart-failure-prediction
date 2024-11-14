# Notebooks
To keep things organized and legible, the `notebooks` folder has been subdivided by the analysis step.

## Naming Convention
When naming notebooks, we use a naming convention that shows the order the analysis was done in.

We use the format:

`<step>.<notebook>-<description>.ipynb`

`<notebook>` is just the Nth notebook in that phase to be created.

## Step Scheme
- **0 - Data exploration** - often just for exploratory work
- **1 - Data preparation** - often writes data to `data/processed` or `data/interim`
- **2 - Visualizations** - often writes report-ready visualizations to `reports`
- **3 - Modeling**- training machine learning models
- **4 - Reporting** - Notebooks that get turned directly into reports
