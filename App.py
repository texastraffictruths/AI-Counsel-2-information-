import streamlit as st
from modules import dashboard, case_storage, navigation, persona_selector, wellness, export, intake, timeline, evidence, legal_intel, drafting, post_filing, chatbot, redaction, verification

def main():
    # App-wide session state initialization
    navigation.init_session_state()
    case_storage.init_case_storage()
    persona_selector.init_persona_state()
    st.set_page_config(page_title="AI Counsel", page_icon="⚖️", layout="wide")

    # Top Navigation Bar
    navigation.top_bar()

    # Left Sidebar Navigation
    selection = navigation.sidebar_menu()

    # Main Content Area Routing
    if selection == "Dashboard":
        dashboard.show()
    elif selection == "Case Intake":
        intake.show()
    elif selection == "Timeline":
        timeline.show()
    elif selection == "Evidence Locker":
        evidence.show()
    elif selection == "Entities":
        evidence.show_entities()
    elif selection == "Legal Intelligence":
        legal_intel.show()
    elif selection == "Drafting Suite":
        drafting.show()
    elif selection == "Post-Filing":
        post_filing.show()
    elif selection == "Wellness":
        wellness.show()
    elif selection == "Export":
        export.show()
    elif selection == "Redaction":
        redaction.show()
    elif selection == "Verification":
        verification.show()
    elif selection == "AI Counsel":
        chatbot.show()
    else:
        st.info("Select a module from the sidebar.")

if __name__ == "__main__":
    main()
