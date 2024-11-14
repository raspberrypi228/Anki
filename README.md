# PDF to Anki Flashcard Generator

A Python script that automatically converts PDF documents into Anki flashcards, making study material preparation more efficient. The script extracts text from PDFs and creates structured flashcards based on the document's formatting and hierarchy.

## Features

- Extracts text from PDF documents
- Automatically identifies topics and subtopics based on text formatting
- Creates structured flashcards with topic/subtopic as the front and content as the back
- Directly integrates with Anki via AnkiConnect
- Supports custom deck naming
- Automatic text cleaning and formatting
- Tags flashcards based on topics for better organization

## Prerequisites

Before running this script, you need to have:

1. Python 3.6 or higher installed
2. Anki desktop application installed
3. AnkiConnect add-on installed in Anki
4. Required Python packages:
   ```bash
   pip install pdfplumber requests
   ```

## Installation

1. Install AnkiConnect in Anki:
   - Open Anki
   - Go to Tools → Add-ons → Get Add-ons...
   - Enter code: `2055492159`
   - Restart Anki

2. Clone this repository or download the script:
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure Anki is running with AnkiConnect installed
2. Run the script:
   ```bash
   python anki-test.py
   ```
3. When prompted:
   - Enter the path to your PDF file
   - Enter the name of the Anki deck where you want to store the flashcards

## How it Works

1. **PDF Text Extraction**
   - Uses `pdfplumber` to extract text while preserving formatting
   - Handles multiple pages and maintains text structure

2. **Text Processing**
   - Identifies topics based on text formatting (uppercase or capitalized lines)
   - Recognizes subtopics marked with bullets or hyphens
   - Cleans and normalizes text for better readability

3. **Flashcard Creation**
   - Front of card: Topic and subtopic
   - Back of card: Related content
   - Automatically tags cards based on topics
   - Prevents duplicate cards

4. **Anki Integration**
   - Communicates with Anki through AnkiConnect's API
   - Adds cards to specified deck
   - Provides feedback on successful additions and errors

## File Structure

```
pdf-to-anki/
│
├── anki-test.py          # Main script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Functions

- `extract_text_from_pdf(pdf_path)`: Extracts text from PDF files
- `clean_text(text)`: Cleans and normalizes extracted text
- `create_flashcards(text)`: Generates flashcard content from processed text
- `add_flashcards_to_anki(flashcards, deck_name)`: Adds flashcards to Anki
- `main()`: Orchestrates the entire process

## Error Handling

The script includes error handling for:
- Invalid file paths
- Unsupported file types
- AnkiConnect communication issues
- JSON parsing errors
- Duplicate flashcards

## Limitations

- PDF must have consistent formatting for proper topic/subtopic detection
- Requires Anki to be running with AnkiConnect installed
- Text extraction quality depends on PDF formatting and structure
- Only supports Basic note type in Anki

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]

## Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159) for Anki integration

## Support

For issues, questions, or suggestions, please [open an issue](your-repository-url/issues) on GitHub.
