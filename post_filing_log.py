def post_filing_menu(case):
    while True:
        print(f"\nIncident Log for {case['name']}:")
        for idx, inc in enumerate(case["post_filing_log"], 1):
            print(f"{idx}. {inc['date'] or 'No date'} - {inc['desc']}")
        print("A. Add Incident")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            desc = input("Incident Description: ")
            date = input("Date (optional): ")
            case["post_filing_log"].append({"desc": desc, "date": date})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
