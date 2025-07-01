print("Welcome to Your Legal App!")
print("Choose a module to run:")

menu = [
    ("1", "Cases Dashboard"),
    ("2", "Timeline"),
    ("3", "Evidence Locker"),
    ("4", "Persons & Entities"),
    ("5", "Legal Sources"),
    ("6", "Drafting Suite"),
    ("7", "Post-Filing Log"),
    ("8", "AI Counsel Persona"),
    ("9", "Export"),
    ("10", "Redaction"),
    ("11", "Wellness"),
    ("12", "Final Verification"),
    ("13", "Quit"),
]

for num, name in menu:
    print(f"{num}. {name}")

choice = input("Enter the number of the module you want: ")

if choice == "1":
    import cases_dashboard
elif choice == "2":
    import timeline
elif choice == "3":
    import evidence_locker
elif choice == "4":
    import persons_entities
elif choice == "5":
    import legal_sources
elif choice == "6":
    import drafting_suite
elif choice == "7":
    import post_filing_log
elif choice == "8":
    import ai_persona
elif choice == "9":
    import export
elif choice == "10":
    import redaction
elif choice == "11":
    import wellness
elif choice == "12":
    import final_verification
elif choice == "13":
    print("Goodbye!")
else:
    print("Not a valid option.")
