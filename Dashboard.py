import streamlit as st
from modules import case_storage

def show():
    st.title("⚖️ My Cases")
    st.write("Welcome to your pro se litigation command center.")

    # List user cases
    cases = case_storage.get_cases()
    if not cases:
        st.info("No cases yet. Create one to get started.")
    else:
        for case_id, case_data in cases.items():
            st.markdown(f"**{case_data['title']}**  \nID: {case_id}  \n_Last Modified: {case_data['last_modified']}_")
            if st.button(f"Open '{case_data['title']}'", key=f"open_{case_id}"):
                case_storage.set_active_case(case_id)
                st.experimental_rerun()

    st.markdown("---")
    st.subheader("Start a New Case")
    new_title = st.text_input("Case Title")
    if st.button("Create New Case"):
        if new_title.strip():
            case_storage.create_case(new_title)
            st.success("Case created!")
            st.experimental_rerun()
        else:
            st.warning("Please enter a title.")
          
