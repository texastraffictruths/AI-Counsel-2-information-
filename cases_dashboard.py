cases = []

def add_case(case_name):
    cases.append({"name": case_name})

def list_cases():
    print("All Cases:")
    for idx, case in enumerate(cases, 1):
        print(f"{idx}. {case['name']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Case\n2. List Cases\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            name = input("Case Name: ")
            add_case(name)
        elif choice == "2":
            list_cases()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
