Copydef timeline_menu(case):
    while True:
        print(f"\nTimeline for {case['name']}:")
        for idx, event in enumerate(case["timeline"], 1):
            print(f"{idx}. {event['date']} - {event['event']}")
        print("A. Add Event")
        print("B. Back")
        choice = input("Choose: ").strip().lower()
        if choice == "a":
            event_text = input("Event description: ")
            date = input("Date (optional): ")
            case["timeline"].append({"event": event_text, "date": date or "No date"})
        elif choice == "b":
            break
        else:
            print("Invalid choice.")
