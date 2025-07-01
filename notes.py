def notes_menu(case):
    while True:
        print(f"\nNotes for {case['name']}:")
        for idx, note in enumerate(case.get("notes", []), 1):
            print(f"{idx}. {note}")
        print("A. Add Note")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            note = input("Enter your note: ")
            case["notes"].append(note)
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
