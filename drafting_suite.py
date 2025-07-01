drafts = []

def add_draft(title, body):
    drafts.append({"title": title, "body": body})

def list_drafts():
    print("Drafts:")
    for idx, draft in enumerate(drafts, 1):
        print(f"{idx}. {draft['title']}")
        print(f"   {draft['body'][:50]}...")  # Show first 50 chars

if __name__ == "__main__":
    while True:
        print("\n1. Add Draft\n2. List Drafts\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            title = input("Draft Title: ")
            body = input("Draft Content: ")
            add_draft(title, body)
        elif choice == "2":
            list_drafts()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
