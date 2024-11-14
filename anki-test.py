import pdfplumber
import requests
import os
import re

def extract_text_from_pdf(pdf_path):
    all_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text.append(text)
    return '\n'.join(all_text)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\u2013', '-').replace('\u2022', '').replace('–', '-')
    return text.strip()

def create_flashcards(text):
    flashcards = []
    lines = text.split('\n')
    current_topic = ""
    current_subtopic = ""
    current_content = []

    for line in lines:
        line = clean_text(line)
        if not line:
            continue

        if line.isupper() or (len(line) > 3 and line[0].isupper() and not line[1].isupper()):
            # This line is likely a main topic
            if current_topic and current_content:
                flashcards.append((current_topic, current_subtopic, ' '.join(current_content)))
            current_topic = line
            current_subtopic = ""
            current_content = []
        elif line.startswith('•') or line.startswith('-'):
            # This line is likely a subtopic
            if current_subtopic and current_content:
                flashcards.append((current_topic, current_subtopic, ' '.join(current_content)))
            current_subtopic = line
            current_content = []
        else:
            # This line is content
            current_content.append(line)

    # Add the last flashcard if there's any pending
    if current_topic and current_content:
        flashcards.append((current_topic, current_subtopic, ' '.join(current_content)))

    return flashcards

def add_flashcards_to_anki(flashcards, deck_name):
    for topic, subtopic, content in flashcards:
        note = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": deck_name,
                    "modelName": "Basic",
                    "fields": {
                        "Front": f"{topic}\n\n{subtopic}",
                        "Back": content,
                    },
                    "options": {
                        "allowDuplicate": False
                    },
                    "tags": [clean_text(topic).replace(" ", "_")]
                }
            }
        }

        response = requests.post('http://localhost:8765', json=note)
        try:
            response_json = response.json()
            if 'error' in response_json and response_json['error']:
                print(f"Error adding flashcard: {response_json['error']}")
            else:
                print(f"Added flashcard: {topic[:30]}... - {subtopic[:30]}...")
        except ValueError:
            print(f"Failed to parse response as JSON: {response.text}")

def main():
    file_path = input("Enter the path to your PDF file: ").strip()
    deck_name = input("Enter the Anki deck name: ").strip()
    
    if not os.path.exists(file_path):
        print("File does not exist. Please check the path.")
        return

    if not file_path.endswith('.pdf'):
        print("Unsupported file type. Please provide a PDF file.")
        return

    text = extract_text_from_pdf(file_path)
    flashcards = create_flashcards(text)

    if flashcards:
        add_flashcards_to_anki(flashcards, deck_name)
        print(f"Successfully added {len(flashcards)} flashcards to Anki in the '{deck_name}' deck.")
    else:
        print("No flashcards created. Please check the content.")

if __name__ == "__main__":
    main()