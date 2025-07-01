import streamlit as st

# Make a place to remember your cases
if "cases" not in st.session_state:
    st.session_state.cases = []

st.title("My Cases")

# Show the list of cases
if st.session_state.cases:
    for case in st.session_state.cases:
        st.write(f"Case: {case}")
else:
    st.write("No cases yet.")

# Add a new case
new_case = st.text_input("Enter a new case name:")
if st.button("Add Case"):
    if new_case:
        st.session_state.cases.append(new_case)
        st.experimental_rerun()
