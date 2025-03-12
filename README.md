# **Text Lemma Extractor and Word Tracking**
This project processes text to extract lemmas (base forms of words) using spaCy and updates a list of known words based on a predefined wordbank. It is designed to help users analyze and track vocabulary usage in any type of text



## **Project Files**

### **1. Text Files**
- **`text.txt`**: A sample text used for lemma extraction.
- **`input.txt`**: A list of useful phrases or sentences for vocabulary tracking.

### **2. JSON Files**
- **`wordsKnown.json`**: Stores a list of words that the user has already learned.
- **`wordbank.json`**: A predefined set of words and phrases used as a reference.

### **3. Python Scripts**
- **`lemma_extractor.py`**: 
  - Reads a text file and extracts lemmas (base word forms) using **spaCy**.
  - Saves the extracted lemmas to a JSON file.
  - Usage:  
    ```bash
    python lemma_extractor.py text.txt
    ```
    This generates `text.json`, containing the lemmas of `text.txt`.

- **`wordsKnown.py`**: 
  - Compares words from a user-provided text with `wordbank.json` and updates `wordsKnown.json` with newly learned words.
  - Usage:  
    ```bash
    python wordsKnown.py wordbank.json wordsKnown.json input.txt
    ```
    This updates `wordsKnown.json` with any new words found in `input.txt`.

## **Installation & Setup**
1. Install dependencies:
   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```
2. Run the scripts as described above to process text and track known words.

## **How It Works**
- The project reads **any given text**, extracts **lemmas**, and determines if the words are already known.
- The **wordbank** provides a reference for essential terms.
- The **words known** file helps track a user's vocabulary progress.

## **Use Case**
- Useful for **language learners**, **students**, and **researchers** who want to analyze text and monitor vocabulary growth.
