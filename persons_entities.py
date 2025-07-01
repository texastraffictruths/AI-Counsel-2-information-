def entities_menu(case):
    while True:
        print(f"\nEntities for {case['name']}:")
        for idx, ent in enumerate(case["entities"], 1):
            print(f"{idx}. {ent['name']} ({ent['role']})")
        print("A. Add Entity")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            name = input("Name: ")
            role = input("Role: ")
            case["entities"].append({"name": name, "role": role})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
