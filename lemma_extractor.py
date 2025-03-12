
import sys
import json
import spacy

def read_text_file(filename):
    """Read text from a .txt file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def text_to_lemmas(text):
    """Convert text to a list of lemmas using spaCy."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_space]

def main():
    # Check if filename is provided
    if len(sys.argv) < 2:
        print("Usage: python lemma_extractor.py input.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    text = read_text_file(input_filename)

    lemmas = text_to_lemmas(text)

    # Output JSON filename (same name as input but with .json extension)
    output_filename = input_filename.replace(".txt", ".json")

    # Save lemmas as a JSON file
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(lemmas, f, ensure_ascii=False, indent=2)

    print(f"Lemmas saved to {output_filename}")

if __name__ == "__main__":
    main()
