import sys
import json
import spacy

def main():
    if len(sys.argv) < 4:
        print("Please provide the paths to wordbank.json, wordsKnown.json, and userText.txt.")
        sys.exit(1)

    wordbank_file = sys.argv[1]
    words_known_file = sys.argv[2]
    user_text_file = sys.argv[3]

    # Load the wordbank
    with open(wordbank_file, 'r', encoding='utf-8') as f:
        wordbank = json.load(f)

    # Load words already known
    with open(words_known_file, 'r', encoding='utf-8') as f:
        words_known = json.load(f)

    # Read the user's text
    with open(user_text_file, 'r', encoding='utf-8') as f:
        user_text = f.read()

    # Initialize spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_text.lower())  # Convert text to lowercase for case-insensitive matching

    # Extract lemma tokens (excluding punctuation and spaces)
    lemma_tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]

    # Update known words using the lemmas
    for lemma in lemma_tokens:
        if lemma in wordbank and lemma not in words_known:
            words_known.append(lemma)

    # Save the updated list of known words
    with open(words_known_file, 'w', encoding='utf-8') as f:
        json.dump(words_known, f, ensure_ascii=False, indent=2)

    # Print progress
    print(f"Words known {len(words_known)}/{len(wordbank)}")

if __name__ == "__main__":
    main()
