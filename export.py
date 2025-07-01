import json

def export_case(case):
    filename = input("Enter filename to export (e.g., my_case_export.json): ").strip()
    if not filename:
        print("Export cancelled (no filename given).")
        return
    try:
        with open(filename, "w") as f:
            json.dump(case, f, indent=2)
        print(f"Case exported to {filename}")
    except Exception as e:
        print(f"Export failed: {e}")
