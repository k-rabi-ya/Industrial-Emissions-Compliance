import pandas as pd
import streamlit as st
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from model_preparation import prepare_data
from model_training import train_model


st.set_page_config(
    page_title="Industrial Emissions Compliance",
    layout="wide",
)

st.title("Industrial Emissions Compliance Classifier")
st.caption(
    "Classifies facility records as compliant or non-compliant."
)




@st.cache_data
def load_data():
    return prepare_data()


@st.cache_resource
def train_pipeline():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model, scaler = train_model(X_train, y_train)
    X_test_scaled = scaler.transform(X_test)
    y_pred = model.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    return X, y, y_test, y_pred, cm


def class_metrics(cm, class_index):
    tp = cm[class_index, class_index]
    fn = cm[class_index].sum() - tp
    fp = cm[:, class_index].sum() - tp
    tn = cm.sum() - tp - fn - fp

    sensitivity = tp / (tp + fn) if (tp + fn) else 0.0
    specificity = tn / (tn + fp) if (tn + fp) else 0.0
    return sensitivity, specificity


X, y, y_test, y_pred, cm = train_pipeline()

non_compliant_sensitivity, non_compliant_specificity = class_metrics(cm, 1)
compliant_sensitivity, compliant_specificity = class_metrics(cm, 0)

col1, col2, col3 = st.columns(3)
col1.metric("Records", f"{len(X):,}")
col2.metric("Flagged Non-Compliant", f"{int(y.sum()):,}")
col3.metric("Test Records", f"{len(y_test):,}")

metrics_df = pd.DataFrame(
    {
        "Class": ["Compliant (0)", "Non-Compliant (1)"],
        "Sensitivity": [compliant_sensitivity, non_compliant_sensitivity],
        "Specificity": [compliant_specificity, non_compliant_specificity],
    }
)

cm_df = pd.DataFrame(
    cm,
    index=["Actual Compliant", "Actual Non-Compliant"],
    columns=["Predicted Compliant", "Predicted Non-Compliant"],
)

left, right = st.columns(2)

with left:
    st.subheader("Sensitivity and Specificity")
    st.dataframe(
        metrics_df.style.format({"Sensitivity": "{:.4f}", "Specificity": "{:.4f}"}),
        use_container_width=True,
    )

with right:
    st.subheader("Confusion Matrix")
    st.dataframe(cm_df, use_container_width=True)

