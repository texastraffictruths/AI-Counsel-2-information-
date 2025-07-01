def evidence_menu(case):
    while True:
        print(f"\nEvidence for {case['name']}:")
        for idx, item in enumerate(case["evidence"], 1):
            print(f"{idx}. {item['file']} - {item['description']}")
        print("A. Add Evidence")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            fname = input("File name: ")
            desc = input("Description: ")
            case["evidence"].append({"file": fname, "description": desc})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
