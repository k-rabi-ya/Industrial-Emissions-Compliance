import pandas as pd
import streamlit as st


st.set_page_config(page_title="Industrial Emissions Compliance", layout="centered")


def check_range(value, limits):
    if value < limits[0]:
        return "Low"
    if value < limits[1]:
        return "Moderate"
    if value < limits[2]:
        return "High"
    return "Very High"


def check_audit_risk(co2, ch4, n2o, total):
    notes = []
    gas_sum = co2 + ch4 + n2o

    if total > 0 and gas_sum > total:
        notes.append("Gas values are higher than total direct emissions.")
    if total > 0 and total < (gas_sum * 0.5):
        notes.append("Total direct emissions look unusually low compared with the gas values.")
    if co2 >= 900_000 or ch4 >= 9_000 or n2o >= 4_500:
        notes.append("One or more values are close to a non-compliant threshold.")

    if notes:
        return "High", notes
    return "Low", ["No obvious reporting discrepancy was found."]


st.title("Industrial Emissions Compliance")
st.caption("SDG Goal: SDG 13 Climate Action")
st.write(
    "Classify factory emission logs as compliant or non-compliant with climate regulations."
)

with st.expander("View Threshold Guide"):
    st.table(
        pd.DataFrame(
            {
                "Gas": ["CO2", "Methane (CH4)", "Nitrous Oxide (N2O)"],
                "Low": ["< 10,000", "< 100", "< 100"],
                "Moderate": ["10,000 - 99,999", "100 - 999", "100 - 999"],
                "High": ["100,000 - 999,999", "1,000 - 9,999", "1,000 - 4,999"],
                "Very High": [">= 1,000,000", ">= 10,000", ">= 5,000"],
            }
        )
    )

with st.form("emissions_form"):
    facility_name = st.text_input("Facility Name", value="Sample Factory")
    country = st.text_input("Country", value="India")
    reporting_year = st.number_input(
        "Reporting Year", min_value=2020, max_value=2035, value=2023, step=1
    )
    co2 = st.number_input("CO2 Emissions (tons/year)", min_value=0.0, value=0.0)
    ch4 = st.number_input("Methane CH4 Emissions (tons/year)", min_value=0.0, value=0.0)
    n2o = st.number_input("Nitrous Oxide N2O Emissions (tons/year)", min_value=0.0, value=0.0)
    total = st.number_input("Total Direct Emissions (tons/year)", min_value=0.0, value=0.0)
    submitted = st.form_submit_button("Check Compliance")

if submitted:
    co2_level = check_range(co2, [10_000, 100_000, 1_000_000])
    ch4_level = check_range(ch4, [100, 1_000, 10_000])
    n2o_level = check_range(n2o, [100, 1_000, 5_000])

    reasons = []
    non_compliant = False

    if co2 >= 1_000_000:
        non_compliant = True
        reasons.append("CO2 is above 1,000,000 tons/year.")
    if ch4 >= 10_000:
        non_compliant = True
        reasons.append("Methane is above 10,000 tons/year.")
    if n2o >= 5_000:
        non_compliant = True
        reasons.append("Nitrous oxide is above 5,000 tons/year.")
    if total >= 1_000_000:
        non_compliant = True
        reasons.append("Total direct emissions are very high.")

    audit_risk, audit_notes = check_audit_risk(co2, ch4, n2o, total)
    status = "Non-Compliant" if non_compliant else "Compliant"

    st.subheader("Result")
    st.write(f"Facility: `{facility_name}`")
    st.write(f"Country: `{country}`")
    st.write(f"Reporting Year: `{reporting_year}`")

    if non_compliant:
        st.error(status)
    else:
        st.success(status)

    left, right = st.columns(2)
    left.metric("CO2 Level", co2_level)
    left.metric("CH4 Level", ch4_level)
    right.metric("N2O Level", n2o_level)
    right.metric("Audit Risk", audit_risk)

    st.subheader("Why")
    st.write(f"- CO2 entered: {co2:,.0f} tons/year ({co2_level})")
    st.write(f"- Methane entered: {ch4:,.0f} tons/year ({ch4_level})")
    st.write(f"- Nitrous oxide entered: {n2o:,.0f} tons/year ({n2o_level})")

    if reasons:
        for reason in reasons:
            st.write(f"- {reason}")
    else:
        st.write("- All gases are below the non-compliant threshold values.")

    st.subheader("Audit Notes")
    for note in audit_notes:
        st.write(f"- {note}")

    summary_df = pd.DataFrame(
        {
            "Facility": [facility_name],
            "Country": [country],
            "Reporting Year": [reporting_year],
            "CO2": [co2],
            "CH4": [ch4],
            "N2O": [n2o],
            "Total Direct Emissions": [total],
            "CO2 Level": [co2_level],
            "CH4 Level": [ch4_level],
            "N2O Level": [n2o_level],
            "Audit Risk": [audit_risk],
            "Compliance Status": [status],
        }
    )

