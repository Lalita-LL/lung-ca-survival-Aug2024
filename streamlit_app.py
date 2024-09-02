import streamlit as st
import numpy as np

# Title
st.title("Survival prediction in advanced EGFR mutated NSCLC")
st.write(
    "This app and model were developed by Faculty of Medicine, Chiang Mai University"
)

# Sidebar Inputs
ptname = st.text_input('Enter patient code')

time_to_predict = st.radio(
    "Time to predict",
    options=["6 months", "12 months", "18 months"],
    index=0
)

bmi_group = st.radio(
    "BMI group",
    options=["Less than 18.5", "18.5-22.9", "More than 23"],
    index=1
)

bone_metastasis = st.radio(
    "Bone metastasis",
    options=["Absence", "Presence"],
    index=0
)

nlr = st.radio(
    "Neutrophil to lymphocyte ratio",
    options=["Less than 5", "Equal to or more than 5"],
    index=0
)

agr = st.radio(
    "Albumin to globulin ratio",
    options=["Equal to or more than 1", "Less than 1"],
    index=0
)

mpa_size = st.radio(
    "MPA size",
    options=["Less than 29 mm", "Equal to or more than 29 mm"],
    index=0
)

# Mapping input selections to numeric values
time_to_predict_mapping = {"6 months": 6, "12 months": 12, "18 months": 18}
bmi_mapping = {"Less than 18.5": 0.2943594, "18.5-22.9": 0, "More than 23": -0.6491672}
bone_mapping = {"Absence": 0, "Presence": 0.7338159}
nlr_mapping = {"Less than 5": 0, "Equal to or more than 5": 0.8116491}
agr_mapping = {"Equal to or more than 1": 0, "Less than 1": 0.7732527}
mpa_mapping = {"Less than 29 mm": 0, "Equal to or more than 29 mm": 1.008189}

# Calculate Linear Predictor (LP)
LP = (bmi_mapping[bmi_group] +
      bone_mapping[bone_metastasis] +
      nlr_mapping[nlr] +
      agr_mapping[agr] +
      mpa_mapping[mpa_size])

# Calculate survival probability at specific time points
if time_to_predict == 6:
    surv_prob_cal = 0.95749615 ** np.exp(LP)
elif time_to_predict == 12:
    surv_prob_cal = 0.89750459 ** np.exp(LP)
else:
    surv_prob_cal = 0.76757468 ** np.exp(LP)

# Display the survival probability for the specific patient
st.subheader("Survival probability value")
st.write(f"The survival probability of {ptname} at {time_to_predict} months is "
         f"{round(surv_prob_cal * 100, 2)}% ")
