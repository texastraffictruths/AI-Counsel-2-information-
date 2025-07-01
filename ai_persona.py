PERSONAS = [
    {
        "name": "Strategist",
        "description": "Clear, concise, and objective. A no-nonsense professional focused on the facts and the most direct path to building your case."
    },
    {
        "name": "Guide",
        "description": "Patient, empathetic, and supportive. Acts as a calm mentor, reduces stress, and guides you step by step."
    },
    {
        "name": "Razor",
        "description": "Witty, blunt, and fiercely strategic with a touch of dark humor. Keeps you motivated by treating the law like a competitive sport."
    },
    {
        "name": "Ally",
        "description": "Relatable, modern, and direct. Communicates like a tech-savvy peer, using plain English and modern expressions."
    }
]

def persona_menu(case):
    print("\nAI Persona Selection:")
    for idx, persona in enumerate(PERSONAS, 1):
        print(f"{idx}. {persona['name']}: {persona['description']}")
    print("C. Current Persona")
    print("B. Back")
    choice = input("Choose a persona number, C to view current, or B to go back: ").strip().lower()
    if choice == "b":
        return
    elif choice == "c":
        if "persona" in case and case["persona"] is not None:
            p = PERSONAS[case["persona"]]
            print(f"Current Persona: {p['name']} - {p['description']}")
        else:
            print("No persona set for this case.")
        input("Press Enter to continue.")
    elif choice.isdigit() and 1 <= int(choice) <= len(PERSONAS):
        idx = int(choice) - 1
        case["persona"] = idx
        print(f"Persona set to {PERSONAS[idx]['name']} for this case.")
        input("Press Enter to continue.")
    else:
        print("Invalid choice.")
        input("Press Enter to continue.")

def get_persona_description(case):
    idx = case.get("persona")
    if idx is not None and 0 <= idx < len(PERSONAS):
        return PERSONAS[idx]["description"]
    else:
        return "No persona selected."

# For testing
if __name__ == "__main__":
    test_case = {"name": "Test Case"}
    persona_menu(test_case)
    print(get_persona_description(test_case))
