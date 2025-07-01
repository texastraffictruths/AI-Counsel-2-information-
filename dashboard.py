from data_store import save_cases, load_cases

def show_dashboard():
    cases = load_cases()
    while True:
        print("\nYour Cases:")
        for idx, case in enumerate(cases, 1):
            print(f"{idx}. {case['name']}")
        print("N. New Case")
        print("Q. Quit")
        choice = input("Pick a case number, N for new, Q to quit: ").strip().lower()
        if choice == "q":
            save_cases(cases)
            break
        elif choice == "n":
            name = input("Enter new case name: ")
            new_case = {
                "name": name,
                "timeline": [],
                "evidence": [],
                "entities": [],
                "notes": [],
                "legal_sources": [],
                "post_filing_log": [],
                "drafts": []
            }
            cases.append(new_case)
            save_cases(cases)
        elif choice.isdigit() and 1 <= int(choice) <= len(cases):
            selected = int(choice) - 1
            case_menu(cases, selected)
        else:
            print("Invalid choice.")
        save_cases(cases)

def case_menu(cases, idx):
    case = cases[idx]
    while True:
        print(f"\n--- {case['name']} ---")
        print("1. Timeline")
        print("2. Evidence")
        print("3. Entities")
        print("4. Notes")
        print("5. Legal Sources")
        print("6. Post-Filing Log")
        print("7. Drafts")
        print("B. Back to dashboard")
        choice = input("Choose a module: ").strip().lower()
        if choice == "1":
            from timeline import timeline_menu
            timeline_menu(case)
        elif choice == "2":
            from evidence_locker import evidence_menu
            evidence_menu(case)
        elif choice == "3":
            from persons_entities import entities_menu
            entities_menu(case)
        elif choice == "4":
            from notes import notes_menu
            notes_menu(case)
        elif choice == "5":
            from legal_sources import sources_menu
            sources_menu(case)
        elif choice == "6":
            from post_filing_log import post_filing_menu
            post_filing_menu(case)
        elif choice == "7":
            from drafting_suite import drafts_menu
            drafts_menu(case)
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
