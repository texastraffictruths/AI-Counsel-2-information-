incidents = []

def add_incident(desc, date=None):
    incidents.append({"desc": desc, "date": date})

def list_incidents():
    print("Incident Log:")
    for idx, inc in enumerate(incidents, 1):
        print(f"{idx}. {inc['date'] or 'No date'} - {inc['desc']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Incident\n2. List Incidents\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            desc = input("Incident Description: ")
            date = input("Date (optional): ")
            add_incident(desc, date)
        elif choice == "2":
            list_incidents()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
