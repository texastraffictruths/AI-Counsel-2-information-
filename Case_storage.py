import os, json
from utils import encryption

CASES_DIR = "./cases/"

def init_case_storage():
    os.makedirs(CASES_DIR, exist_ok=True)

def get_cases():
    # Loads all case metadata (not full data) for dashboard display
    cases = {}
    for fname in os.listdir(CASES_DIR):
        if fname.endswith(".json"):
            with open(os.path.join(CASES_DIR, fname), "r") as f:
                data = json.load(f)
                cases[data["case_id"]] = data
    return cases

def create_case(title):
    import uuid, datetime
    case_id = "AIC-" + str(uuid.uuid4())[:8]
    data = {
        "case_id": case_id,
        "title": title,
        "last_modified": datetime.datetime.now().isoformat(),
        # Add further fields as needed
    }
    with open(os.path.join(CASES_DIR, f"{case_id}.json"), "w") as f:
        json.dump(data, f)

def set_active_case(case_id):
    # Store in session state
    import streamlit as st
    st.session_state.active_case_id = case_id
