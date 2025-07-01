sources = []

def add_source(name, link="", summary=""):
    sources.append({"name": name, "link": link, "summary": summary})

def list_sources():
    print("Legal Sources:")
    for idx, src in enumerate(sources, 1):
        print(f"{idx}. {src['name']}")
        if src["link"]:
            print(f"   Link: {src['link']}")
        if src["summary"]:
            print(f"   Summary: {src['summary']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Source\n2. List Sources\n3. Quit")
        choice = input("Choose option: ")
        if choice == "1":
            name = input("Source Name: ")
            link = input("Link (optional): ")
            summary = input("Summary (optional): ")
            add_source(name, link, summary)
        elif choice == "2":
            list_sources()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
