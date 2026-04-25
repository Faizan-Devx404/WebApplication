# 🎵 MoodWave — AI Mood-Based Music Recommender

> Tell it how you feel. It tells you what to play.

A Flask web app powered by Claude AI that reads your emotional state and curates a personalized playlist of 8 songs.

---

## 🗂️ Project Structure

```
mood-music/
├── app.py                  # Flask backend + Claude API logic
├── templates/
│   └── index.html          # Frontend UI (single-page)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Multi-container orchestration
├── .env.example            # Environment variable template
└── .dockerignore           # Files to exclude from Docker image
```

---

## ⚙️ How It Works

1. User types their mood/feeling into the text box
2. Flask sends the mood to Claude AI via the Anthropic API
3. Claude returns a JSON playlist (8 songs with metadata)
4. The frontend renders the playlist with vibe tags, energy bars, and a Spotify search link

---

## 🚀 Setup & Run

### Prerequisites
- Docker + Docker Compose installed
- An Anthropic API key → https://console.anthropic.com

### Step 1: Clone / navigate to the project folder
```bash
cd mood-music
```

### Step 2: Create your .env file
```bash
cp .env.example .env
# Now open .env and paste your Anthropic API key
```

### Step 3: Build and run with Docker Compose
```bash
docker-compose up --build
```

### Step 4: Open the app
```
http://localhost:5000
```

---

## 🛑 Stop the App
```bash
docker-compose down
```

---

## 🔧 Run Locally (Without Docker)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python app.py
```

---

## 🧠 Tech Stack

| Layer      | Technology            |
|------------|-----------------------|
| Backend    | Python + Flask        |
| AI         | Anthropic Claude API  |
| Frontend   | Vanilla HTML/CSS/JS   |
| Server     | Gunicorn              |
| Container  | Docker + Compose      |

---

## 📸 Features

- 🎭 Interprets any mood description (poetic, literal, complex)
- 🎵 Returns 8 curated songs with artist, genre, vibe tag, energy level
- 🔗 One-click Spotify search for your playlist
- 💡 Example mood chips to get started fast
- ✨ Beautiful dark UI with animated loading state
