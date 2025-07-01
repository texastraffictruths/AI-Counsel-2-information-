personas = ["Strategist", "Guide", "Razor", "Ally"]

def choose_persona():
    print("Available Personas:")
    for idx, p in enumerate(personas, 1):
        print(f"{idx}. {p}")
    choice = input("Choose a persona number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(personas):
            print(f"You chose: {personas[idx]}")
            return personas[idx]
        else:
            print("Invalid number.")
    except:
        print("Not a number.")
    return None

if __name__ == "__main__":
    choose_persona()
