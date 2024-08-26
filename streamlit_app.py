import streamlit as st
import numpy as np

# Title
st.title("Survival function in lung cancer patients 🎈")
st.write(
    "This app and model were developed by Faculty of Medicine, Chiang Mai University"
)

# Sidebar Inputs
ptname = st.text_input('Enter patient code')

time_to_predict = st.radio(
    "Time to predict (Months)",
    [6, 12, 18],
    index=0
)

bmi_group = st.radio(
    "BMI group",
    options=["<18.5", "18.5-22.9", ">23"],
    index=1
)

bone_metastasis = st.radio(
    "Bone metastasis",
    options=["Without bone metastasis", "With bone metastasis"],
    index=0
)

nlr = st.radio(
    "Neutrophil to lymphocyte ratio",
    options=["<5", ">=5"],
    index=0
)

agr = st.radio(
    "Albumin to globulin ratio",
    options=[">=1", "<1"],
    index=0
)

mpa_size = st.radio(
    "MPA size",
    options=["<29 mm", ">=29 mm"],
    index=0
)

# Mapping input selections to numeric values
bmi_mapping = {"<18.5": 0.2943594, "18.5-22.9": 0, ">23": -0.6491672}
bone_mapping = {"Without bone metastasis": 0, "With bone metastasis": 0.7338159}
nlr_mapping = {"<5": 0, ">=5": 0.8116491}
agr_mapping = {">=1": 0, "<1": 0.7732527}
mpa_mapping = {"<29 mm": 0, ">=29 mm": 1.008189}

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
