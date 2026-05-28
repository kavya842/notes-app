# Notes App with Search

A lightweight full-stack notes application built with **Flask**, **HTML**, **CSS**, and **Vanilla JavaScript**. It lets users create, edit, delete, and search notes instantly, with case-insensitive keyword highlighting for a smoother note-browsing experience.

## Features

- Create, edit, and delete notes  
- Real-time search across title and body  
- Case-insensitive keyword highlighting  
- Clean, responsive UI  
- In-memory storage (no database)  

## Tech Stack

- Backend: Python + Flask  
- Frontend: HTML, CSS, Vanilla JavaScript  
- Storage: In-memory  

## Setup

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/notes-app.git
cd notes-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the backend:
```bash
python app.py
```

4. Open in browser:  
**http://127.0.0.1:5000**

## API Endpoints

| Method | Endpoint           | Description      |
|--------|--------------------|------------------|
| GET    | `/api/notes`       | Get all notes    |
| GET    | `/api/notes?q=...` | Search notes     |
| GET    | `/api/notes/<id>`  | Get single note  |
| POST   | `/api/notes`       | Create note      |
| PUT    | `/api/notes/<id>`  | Update note      |
| DELETE | `/api/notes/<id>`  | Delete note      |

## Project Structure

```text
notes-app/
├── app.py           # Flask backend
├── index.html       # Frontend
├── requirements.txt # Dependencies
└── README.md
```

## Notes

- Notes are stored in memory and cleared on restart  
- Perfect for learning Flask CRUD + frontend API integration  
