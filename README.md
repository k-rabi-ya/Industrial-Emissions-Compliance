# Industrial Emissions Compliance

This project trains a machine learning model to classify factory emission records as `Compliant` or `Non-Compliant` using greenhouse gas reporting data.

## What It Does

- Combines 2022 and 2023 emissions datasets with historical 2020 and 2021 emissions features
- Creates a binary compliance label using an industry-relative emissions threshold
- Trains a `RandomForestClassifier` with grid search
- Evaluates predictions with a confusion matrix, sensitivity, and specificity
- Provides a Streamlit app for viewing the current model output

## Run

Prepare the merged dataset:

```powershell
python data.py
```

Run evaluation:

```powershell
python confusion_matrix.py
```

Run the Streamlit app:

```powershell
streamlit run app.py
```

## Output

The model reports:

- Confusion matrix
- Sensitivity (recall)
- Specificity for each class
