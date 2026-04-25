from flask import Flask, render_template, request, jsonify
import anthropic
import os
import json

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").strip()

    if not mood:
        return jsonify({"error": "Please describe your mood!"}), 400

    prompt = f"""You are a music expert and mood reader. The user says they feel: "{mood}"

Based on this mood, recommend exactly 8 songs. For each song provide:
- title
- artist
- genre
- why_it_fits (one short sentence, max 10 words)
- energy_level (1-10)
- vibe_tag (one word like: dreamy, hype, melancholic, euphoric, chill, etc.)

Respond ONLY with a valid JSON object like this:
{{
  "mood_summary": "A 1-sentence poetic interpretation of their mood",
  "playlist_name": "A creative playlist name (max 5 words)",
  "color": "A hex color that represents this mood (e.g. #FF6B6B)",
  "songs": [
    {{
      "title": "Song Title",
      "artist": "Artist Name",
      "genre": "Genre",
      "why_it_fits": "Short reason",
      "energy_level": 7,
      "vibe_tag": "euphoric"
    }}
  ]
}}

No markdown, no extra text, just the JSON."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        result = json.loads(raw)
        return jsonify(result)
    except json.JSONDecodeError:
        return jsonify({"error": "Could not parse music recommendations. Try again!"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
