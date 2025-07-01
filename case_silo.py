def create_case_silo(case_name):
    return {
        "name": case_name,
        "timeline": [],
        "evidence": [],
        "entities": [],
        "notes": [],
        "legal_sources": [],
        "post_filing_log": []
    }

# Example:
if __name__ == "__main__":
    case = create_case_silo("Sample Case")
    print(case)
