import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment counter"):
    st.session_state.counter += 1
    st.write(f"Increment by: 1")

if st.button("Reset"):
    st.session_state.counter = 0
    st.write(f"Reset to 0")

st.write(f"Counter: {st.session_state.counter}")