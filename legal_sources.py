def sources_menu(case):
    while True:
        print(f"\nLegal Sources for {case['name']}:")
        for idx, src in enumerate(case["legal_sources"], 1):
            print(f"{idx}. {src['name']}")
            if src["link"]:
                print(f"   Link: {src['link']}")
            if src["summary"]:
                print(f"   Summary: {src['summary']}")
        print("A. Add Source")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            name = input("Source Name: ")
            link = input("Link (optional): ")
            summary = input("Summary (optional): ")
            case["legal_sources"].append({"name": name, "link": link, "summary": summary})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
