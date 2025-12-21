from llm import analyze_user_input
from rag import load_dataset, retrieve_songs

def agent_response(user_input: str):
    parsed = analyze_user_input(user_input)
    print("DEBUG LLM PARSED:", parsed)  

    moods = parsed.get("moods", [])
    n_songs = parsed.get("n_songs", 10)

    df = load_dataset()
    songs = retrieve_songs(df, moods, n_songs)
    print("DEBUG SONG COUNT:", len(songs))

    return songs
