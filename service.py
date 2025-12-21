from llm import analyze_user_input
from rag import load_dataset, retrieve_songs

MOOD_MAP = {
    "sad": 0,
    "happy": 1,
    "energetic": 2,
    "calm": 3
}

def get_song_urls(user_input):
    result = analyze_user_input(user_input)

    moods = result.get("moods", [])
    n_songs = result.get("n_songs", 10)

    labels = [MOOD_MAP[m] for m in moods if m in MOOD_MAP]

    if not labels:
        return []

    df = load_dataset()
    return retrieve_songs(df, labels, n_songs)
