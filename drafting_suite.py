def drafts_menu(case):
    while True:
        print(f"\nDrafts for {case['name']}:")
        for idx, draft in enumerate(case["drafts"], 1):
            print(f"{idx}. {draft['title']}")
            print(f"   {draft['body'][:50]}...")  # Show first 50 chars
        print("A. Add Draft")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            title = input("Draft Title: ")
            body = input("Draft Content: ")
            case["drafts"].append({"title": title, "body": body})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
