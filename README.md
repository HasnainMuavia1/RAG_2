# RAG System

A Retrieval-Augmented Generation (RAG) system built with Django that enhances large language model responses with information from your documents.

## Project Overview

This RAG system combines the power of language models with a document retrieval system to provide more accurate, up-to-date, and contextually relevant responses. By integrating document retrieval with generative AI, the system can reference specific documents in your database when answering questions.

## Directory Structure

```
RAG_2/
├── RAG/                  # Main Django app directory
├── data/                 # Storage for document data 
├── project/              # Django project settings
├── static/RAG/           # Static files (CSS, JS, images)
├── templates/RAG/        # HTML templates
├── .gitignore            # Git ignore file
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Features

- Document upload and processing
- Vector embeddings for semantic search
- Integration with language models
- User-friendly interface for queries
- Context-aware responses
- Document citation in answers

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/HasnainMuavia1/RAG_2.git
   cd RAG_2
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

1. Log in to the admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials.
2. Upload documents through the user interface.
3. Ask questions related to your documents through the query interface.
4. Receive answers that incorporate information from your document store.

## Configuration

Customize the RAG system by modifying the settings in `project/settings.py`:

- Adjust vector database settings
- Configure language model integration
- Modify document processing parameters
- Set up authentication options

## Technology Stack

- **Backend**: Django, Python
- **LLM Integration**: Groq cloud , llama model
- **Frontend**: HTML, CSS, JavaScript

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Hasnain Muavia - [GitHub Profile](https://github.com/HasnainMuavia1)

## Acknowledgements
