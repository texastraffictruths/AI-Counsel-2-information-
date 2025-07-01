def verify_document():
    checklist = [
        "I have read the whole document.",
        "I believe the facts are true.",
        "I understand I am responsible for what I submit."
    ]
    for item in checklist:
        input(f"Check: {item} (Press Enter when done)")
    print("All done! You can now submit your document.")

if __name__ == "__main__":
    verify_document()
