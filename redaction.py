def redact(text, word):
    return text.replace(word, "[REDACTED]")

if __name__ == "__main__":
    sample = "This is a secret: my SSN is 123-45-6789."
    print("Before:", sample)
    print("After:", redact(sample, "123-45-6789"))
