import streamlit as st
from datetime import datetime

st.title("User Form")

user_form_data = {
    "name": None,
    "age": None,
    "height": None,
    "gender": None,
    "dob": None,

}

min_date = datetime(1970, 1, 1)
max_date = datetime.now()

with st.form(key="user_form"):
    user_form_data["name"] = st.text_input("Enter your name:")
    user_form_data["height"] = st.number_input("Enter your height (cm)", min_value=120, max_value=220)
    user_form_data["gender"] = st.selectbox("Gender", ["Male", "Female"])
    user_form_data["dob"] = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)

    if user_form_data["dob"]:
        # print(f"Max date: {max_date.year} - {user_form_data['dob'].year}")
        user_form_data["age"] = max_date.year - user_form_data['dob'].year

    # Reload once submit button clicked
    submit_button = st.form_submit_button()

# This will be below the form
if submit_button:
    if not all(user_form_data.values()):
        st.warning("Please fill all fields")
    else:
        st.balloons()
        st.write("### Info")
        for (key, value) in user_form_data.items():
            st.write(f"{key}: {value}")
