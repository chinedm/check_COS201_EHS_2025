import streamlit as st
import pandas as pd

# Load result file
@st.cache_data
def load_data():
    return pd.read_excel("results.xlsx")

df = load_data()

st.title("🎓 Student Result Checker")
st.write("Enter your Matric Number to view your result")

matric = st.text_input("Matric Number")

if st.button("Check Result"):
    student = df[df['MatricNumber'].astype(str).str.strip() == matric.strip()]
    if not student.empty:
        st.success("Result Found ✅")
        st.dataframe(student.T.rename(columns={student.index[0]: "Details"}))
    else:
        st.error("Matric number not found ❌")
