timeline = []

def add_event(event_text, date=None):
    event = {"event": event_text, "date": date}
    timeline.append(event)

def list_timeline():
    print("Timeline Events:")
    for idx, event in enumerate(timeline, 1):
        print(f"{idx}. {event['date'] or 'No date'} - {event['event']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Event\n2. List Timeline\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            text = input("Describe the event: ")
            date = input("Date (optional): ")
            add_event(text, date)
        elif choice == "2":
            list_timeline()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
