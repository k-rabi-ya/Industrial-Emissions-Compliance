# Industrial Emissions Compliance

SDG Goal: `SDG 13 Climate Action`

This is a small Streamlit project that checks whether a factory is `Compliant` or `Non-Compliant` based on simple greenhouse gas threshold values.

## Project Description

The app classifies factory emission logs using basic rules for:

- `CO2`
- `Methane (CH4)`
- `Nitrous Oxide (N2O)`
- `Total Direct Emissions`

It is designed as a simple beginner-friendly demo for climate compliance screening.

## Features

- Enter facility name, country, and reporting year
- Input `CO2`, `CH4`, `N2O`, and total direct emissions
- Check gas values against fixed threshold ranges
- Show a final `Compliant` or `Non-Compliant` result
- Display gas severity levels such as `Low`, `Moderate`, `High`, and `Very High`
- Show simple audit-risk notes for suspicious reporting values
- Download the result as a CSV file

## Threshold Rules

### CO2

- Below `10,000` tons/year: Low
- `10,000` to `99,999` tons/year: Moderate
- `100,000` to `999,999` tons/year: High
- `1,000,000` tons/year and above: Very High and non-compliant

### Methane (CH4)

- Below `100` tons/year: Low
- `100` to `999` tons/year: Moderate
- `1,000` to `9,999` tons/year: High
- `10,000` tons/year and above: Very High and non-compliant

### Nitrous Oxide (N2O)

- Below `100` tons/year: Low
- `100` to `999` tons/year: Moderate
- `1,000` to `4,999` tons/year: High
- `5,000` tons/year and above: Very High and non-compliant

## Run the App

```powershell
streamlit run app.py
```

## Output

The app shows:

- Facility details
- Compliance result
- Gas-level summaries
- Audit-risk notes
- A downloadable CSV report

## Note

Some extra data-processing and model-training files are still present in the project folder, but the current app uses a simple rule-based approach instead of a trained machine learning model.
