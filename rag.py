import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "music_dataset.csv")

MOOD_TO_LABEL = {
    "sad": 0,
    "happy": 1,
    "energetic": 2,
    "calm": 3
}

def load_dataset():
    """Load CSV and return dataframe"""
    df = pd.read_csv(CSV_PATH)
    df["labels"] = df["labels"].astype(int)  
    return df

def retrieve_songs(df, moods, n_songs=10):
    """Filter songs by moods"""
    labels = [MOOD_TO_LABEL[m] for m in moods if m in MOOD_TO_LABEL]
    if not labels:
        return []
    filtered = df[df["labels"].isin(labels)]
    if filtered.empty:
        return []
    return filtered.sample(min(len(filtered), n_songs))["url"].tolist()
