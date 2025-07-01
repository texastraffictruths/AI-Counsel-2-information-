evidence = []

def add_evidence(filename, description=""):
    evidence.append({"file": filename, "description": description})

def list_evidence():
    print("Evidence List:")
    for idx, item in enumerate(evidence, 1):
        print(f"{idx}. {item['file']} - {item['description']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Evidence\n2. List Evidence\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            fname = input("File name: ")
            desc = input("Description: ")
            add_evidence(fname, desc)
        elif choice == "2":
            list_evidence()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
