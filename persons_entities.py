entities = []

def add_entity(name, role):
    entities.append({"name": name, "role": role})

def list_entities():
    print("Entities:")
    for idx, ent in enumerate(entities, 1):
        print(f"{idx}. {ent['name']} ({ent['role']})")

if __name__ == "__main__":
    while True:
        print("\n1. Add Entity\n2. List Entities\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            name = input("Name: ")
            role = input("Role (e.g., Plaintiff, Officer, etc.): ")
            add_entity(name, role)
        elif choice == "2":
            list_entities()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
